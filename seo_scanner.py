#!/usr/bin/env python3
"""
Enhanced SEO Hugo File Scanner with CSV Output and Directory Organization
Better checks for meta descriptions, keywords, and content issues
Now outputs both .md and .csv files with same timestamp in /seo_analysis directory
"""

import os
import re
import csv
from datetime import datetime
from pathlib import Path

def ensure_analysis_directory():
    """Create seo_analysis directory if it doesn't exist"""
    analysis_dir = "seo_analysis"
    if not os.path.exists(analysis_dir):
        os.makedirs(analysis_dir)
        print(f"📁 Created directory: {analysis_dir}/")
    return analysis_dir

def parse_front_matter_detailed(content):
    """Extract detailed front matter including SEO fields"""
    front_matter = {}
    
    # Check for YAML front matter (--- at start)
    if content.startswith('---'):
        try:
            # Find the end of front matter
            end_marker = content.find('---', 3)
            if end_marker != -1:
                front_matter_text = content[3:end_marker].strip()
                
                # Parse all front matter fields
                for line in front_matter_text.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        key = key.strip()
                        value = value.strip().strip('"\'')
                        front_matter[key] = value
        except:
            pass
    
    return front_matter

def extract_clean_content_preview(content):
    """Extract content preview and highlight CSS if present"""
    if content.startswith('---'):
        # Skip front matter
        end_marker = content.find('---', 3)
        if end_marker != -1:
            actual_content = content[end_marker + 3:].strip()
        else:
            actual_content = content
    else:
        actual_content = content
    
    # Check for CSS in content before cleaning
    has_css = '<style>' in actual_content or 'background-color:' in actual_content or '.theme-bullet' in actual_content
    
    if has_css:
        # Highlight CSS code with triple alerts
        highlighted_content = actual_content
        highlighted_content = re.sub(r'<style>', '🚨🚨🚨 <style>', highlighted_content, flags=re.IGNORECASE)
        highlighted_content = re.sub(r'</style>', '</style> 🚨🚨🚨', highlighted_content, flags=re.IGNORECASE)
        highlighted_content = re.sub(r'(background-color:[^;]*;)', r'🚨🚨 \1 🚨🚨', highlighted_content)
        highlighted_content = re.sub(r'(\.theme-bullet[^}]*})', r'🚨🚨 \1 🚨🚨', highlighted_content)
        
        # Get preview with CSS highlighted
        preview = highlighted_content[:300].replace('\n', ' ').strip()
    else:
        # Clean content normally
        clean_content = re.sub(r'<style>.*?</style>', '', actual_content, flags=re.DOTALL | re.IGNORECASE)
        clean_content = re.sub(r'<[^>]+>', '', clean_content)  # Remove HTML tags
        clean_content = re.sub(r'\s+', ' ', clean_content)  # Normalize whitespace
        preview = clean_content[:200].strip()
    
    return preview, has_css

def analyze_enhanced_seo(front_matter, content, file_path):
    """Enhanced SEO analysis with better checks"""
    
    # Extract key SEO fields
    title = front_matter.get('title', '')
    description = front_matter.get('description', '')
    meta_description = front_matter.get('meta_description', '')
    summary = front_matter.get('summary', '')
    keywords = front_matter.get('keywords', '')
    meta_keywords = front_matter.get('meta_keywords', '')
    
    # Find the best description field
    best_description = description or meta_description or summary
    best_keywords = keywords or meta_keywords
    
    # Content analysis
    clean_preview, has_css_detected = extract_clean_content_preview(content)
    word_count = len(content.split())
    
    # Check for CSS in content (enhanced detection)
    has_css_in_content = has_css_detected or '<style>' in content or 'background-color:' in content
    has_html_in_content = bool(re.search(r'<[^>]+>', content))
    
    seo_data = {
        # Basic SEO
        'title': title,
        'title_length': len(title) if title else 0,
        'has_title': bool(title),
        
        # Descriptions
        'description': description,
        'meta_description': meta_description,
        'summary': summary,
        'best_description': best_description,
        'description_length': len(best_description) if best_description else 0,
        'has_description': bool(best_description),
        
        # Keywords
        'keywords': keywords,
        'meta_keywords': meta_keywords,
        'best_keywords': best_keywords,
        'has_keywords': bool(best_keywords),
        
        # Content Quality
        'word_count': word_count,
        'clean_preview': clean_preview,
        'has_css_in_content': has_css_in_content,
        'has_html_in_content': has_html_in_content,
        
        # Other SEO fields
        'canonical': front_matter.get('canonical', ''),
        'robots': front_matter.get('robots', ''),
        'date': front_matter.get('date', ''),
        'lastmod': front_matter.get('lastmod', ''),
        'draft': front_matter.get('draft', ''),
        'weight': front_matter.get('weight', ''),
        
        # Issues list
        'seo_issues': [],
        'content_issues': [],
        'priority': 'low'  # Will be calculated
    }
    
    # Analyze SEO Issues
    issues = []
    content_issues = []
    
    # Title Issues
    if not seo_data['has_title']:
        issues.append('❌ MISSING TITLE')
        seo_data['priority'] = 'critical'
    elif seo_data['title_length'] < 30:
        issues.append(f'⚠️ Title too short ({seo_data["title_length"]} chars, need 30+)')
        seo_data['priority'] = 'high'
    elif seo_data['title_length'] > 60:
        issues.append(f'⚠️ Title too long ({seo_data["title_length"]} chars, max 60)')
        seo_data['priority'] = 'medium'
    
    # Description Issues
    if not seo_data['has_description']:
        issues.append('❌ MISSING META DESCRIPTION')
        if seo_data['priority'] == 'low':
            seo_data['priority'] = 'high'
    elif seo_data['description_length'] > 160:
        issues.append(f'⚠️ Description too long ({seo_data["description_length"]} chars, max 160)')
        if seo_data['priority'] == 'low':
            seo_data['priority'] = 'medium'
    elif seo_data['description_length'] < 120:
        issues.append(f'⚠️ Description could be longer ({seo_data["description_length"]} chars, ideal 120-160)')
    
    # Keywords Issues
    if not seo_data['has_keywords']:
        issues.append('⚠️ Missing SEO keywords')
        if seo_data['priority'] == 'low':
            seo_data['priority'] = 'medium'
    
    # Content Issues
    if seo_data['word_count'] < 200:
        content_issues.append(f'📝 Low word count ({seo_data["word_count"]} words, need 200+)')
        if seo_data['priority'] == 'low':
            seo_data['priority'] = 'medium'
    
    if seo_data['has_css_in_content']:
        content_issues.append('🚨 CSS code found in content (should be in theme files)')
        if seo_data['priority'] == 'low':
            seo_data['priority'] = 'high'
    
    if seo_data['has_html_in_content'] and not seo_data['has_css_in_content']:
        content_issues.append('⚠️ HTML tags found in content')
    
    # Set issues
    seo_data['seo_issues'] = issues if issues else ['✅ No SEO issues']
    seo_data['content_issues'] = content_issues if content_issues else ['✅ No content issues']
    
    return seo_data

def scan_hugo_with_enhanced_seo(content_dir):
    """Scan Hugo content with enhanced SEO analysis"""
    
    print(f"🔍 Enhanced SEO Analysis: {content_dir}")
    print("=" * 60)
    
    all_pages = []
    
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    front_matter = parse_front_matter_detailed(content)
                    rel_path = os.path.relpath(file_path, content_dir)
                    
                    # Determine URL path
                    if file == '_index.md':
                        url_path = '/' + '/'.join(rel_path.split('/')[:-1]) + '/'
                        if url_path == '//':
                            url_path = '/'
                    else:
                        url_path = '/' + rel_path.replace('.md', '/').replace('\\', '/')
                    
                    url_path = url_path.replace('//', '/').rstrip('/') + '/'
                    if url_path == '//':
                        url_path = '/'
                    
                    # Enhanced SEO analysis
                    seo_data = analyze_enhanced_seo(front_matter, content, file_path)
                    
                    page_info = {
                        'file_path': rel_path,
                        'url_path': url_path,
                        'section': rel_path.split('/')[0] if '/' in rel_path else 'root',
                        'seo': seo_data
                    }
                    
                    all_pages.append(page_info)
                    
                    # Show progress with priority
                    priority_icon = {
                        'critical': '🔴',
                        'high': '🟠', 
                        'medium': '🟡',
                        'low': '🟢'
                    }
                    icon = priority_icon.get(seo_data['priority'], '🟢')
                    
                    total_issues = len([i for i in seo_data['seo_issues'] if not i.startswith('✅')]) + \
                                 len([i for i in seo_data['content_issues'] if not i.startswith('✅')])
                    
                    status = f"{icon}({total_issues})" if total_issues > 0 else "✅"
                    print(f"📄 {status} {rel_path}")
                    
                except Exception as e:
                    print(f"❌ Error reading {file_path}: {e}")
    
    return all_pages

def create_enhanced_csv_report(pages, timestamp, analysis_dir):
    """Create CSV report with all SEO analysis data in seo_analysis directory"""
    
    csv_filename = os.path.join(analysis_dir, f"seo_analysis_{timestamp}.csv")
    csv_latest = os.path.join(analysis_dir, "latest_seo_analysis.csv")
    
    print(f"📊 Creating CSV report: {csv_filename}")
    
    published_pages = [p for p in pages if p['seo']['draft'].lower() != 'true']
    
    # Define CSV columns
    fieldnames = [
        'file_path', 'url_path', 'section', 'priority',
        'title', 'title_length', 'has_title',
        'description', 'meta_description', 'summary', 'best_description', 'description_length', 'has_description',
        'keywords', 'meta_keywords', 'best_keywords', 'has_keywords',
        'word_count', 'clean_preview', 'has_css_in_content', 'has_html_in_content',
        'canonical', 'robots', 'date', 'lastmod', 'draft', 'weight',
        'seo_issues_list', 'content_issues_list', 'total_issues', 'seo_score'
    ]
    
    try:
        # Create timestamped CSV
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for page in published_pages:
                seo = page['seo']
                
                # Calculate total issues and score
                seo_issue_count = len([i for i in seo['seo_issues'] if not i.startswith('✅')])
                content_issue_count = len([i for i in seo['content_issues'] if not i.startswith('✅')])
                total_issues = seo_issue_count + content_issue_count
                
                # Simple SEO score (0-100)
                seo_score = max(0, 100 - (total_issues * 10))
                if seo['priority'] == 'critical':
                    seo_score = min(seo_score, 30)
                elif seo['priority'] == 'high':
                    seo_score = min(seo_score, 60)
                elif seo['priority'] == 'medium':
                    seo_score = min(seo_score, 80)
                
                # Join issues into pipe-separated strings for CSV
                seo_issues_str = ' | '.join(seo['seo_issues'])
                content_issues_str = ' | '.join(seo['content_issues'])
                
                # Clean preview for CSV (remove commas and quotes)
                clean_preview_csv = seo['clean_preview'].replace(',', ';').replace('"', "'").replace('\n', ' ')
                
                row = {
                    'file_path': page['file_path'],
                    'url_path': page['url_path'],
                    'section': page['section'],
                    'priority': seo['priority'],
                    'title': seo['title'],
                    'title_length': seo['title_length'],
                    'has_title': seo['has_title'],
                    'description': seo['description'],
                    'meta_description': seo['meta_description'],
                    'summary': seo['summary'],
                    'best_description': seo['best_description'],
                    'description_length': seo['description_length'],
                    'has_description': seo['has_description'],
                    'keywords': seo['keywords'],
                    'meta_keywords': seo['meta_keywords'],
                    'best_keywords': seo['best_keywords'],
                    'has_keywords': seo['has_keywords'],
                    'word_count': seo['word_count'],
                    'clean_preview': clean_preview_csv,
                    'has_css_in_content': seo['has_css_in_content'],
                    'has_html_in_content': seo['has_html_in_content'],
                    'canonical': seo['canonical'],
                    'robots': seo['robots'],
                    'date': seo['date'],
                    'lastmod': seo['lastmod'],
                    'draft': seo['draft'],
                    'weight': seo['weight'],
                    'seo_issues_list': seo_issues_str,
                    'content_issues_list': content_issues_str,
                    'total_issues': total_issues,
                    'seo_score': seo_score
                }
                
                writer.writerow(row)
        
        # Create latest copy
        with open(csv_latest, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for page in published_pages:
                seo = page['seo']
                
                # Calculate total issues and score
                seo_issue_count = len([i for i in seo['seo_issues'] if not i.startswith('✅')])
                content_issue_count = len([i for i in seo['content_issues'] if not i.startswith('✅')])
                total_issues = seo_issue_count + content_issue_count
                
                # Simple SEO score (0-100)
                seo_score = max(0, 100 - (total_issues * 10))
                if seo['priority'] == 'critical':
                    seo_score = min(seo_score, 30)
                elif seo['priority'] == 'high':
                    seo_score = min(seo_score, 60)
                elif seo['priority'] == 'medium':
                    seo_score = min(seo_score, 80)
                
                # Join issues into pipe-separated strings for CSV
                seo_issues_str = ' | '.join(seo['seo_issues'])
                content_issues_str = ' | '.join(seo['content_issues'])
                
                # Clean preview for CSV (remove commas and quotes)
                clean_preview_csv = seo['clean_preview'].replace(',', ';').replace('"', "'").replace('\n', ' ')
                
                row = {
                    'file_path': page['file_path'],
                    'url_path': page['url_path'],
                    'section': page['section'],
                    'priority': seo['priority'],
                    'title': seo['title'],
                    'title_length': seo['title_length'],
                    'has_title': seo['has_title'],
                    'description': seo['description'],
                    'meta_description': seo['meta_description'],
                    'summary': seo['summary'],
                    'best_description': seo['best_description'],
                    'description_length': seo['description_length'],
                    'has_description': seo['has_description'],
                    'keywords': seo['keywords'],
                    'meta_keywords': seo['meta_keywords'],
                    'best_keywords': seo['best_keywords'],
                    'has_keywords': seo['has_keywords'],
                    'word_count': seo['word_count'],
                    'clean_preview': clean_preview_csv,
                    'has_css_in_content': seo['has_css_in_content'],
                    'has_html_in_content': seo['has_html_in_content'],
                    'canonical': seo['canonical'],
                    'robots': seo['robots'],
                    'date': seo['date'],
                    'lastmod': seo['lastmod'],
                    'draft': seo['draft'],
                    'weight': seo['weight'],
                    'seo_issues_list': seo_issues_str,
                    'content_issues_list': content_issues_str,
                    'total_issues': total_issues,
                    'seo_score': seo_score
                }
                
                writer.writerow(row)
        
        print(f"✅ CSV created: {csv_filename}")
        print(f"✅ Latest CSV: {csv_latest}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating CSV: {e}")
        return False

def create_enhanced_seo_report(pages, timestamp, analysis_dir):
    """Create enhanced SEO report with timestamp in seo_analysis directory"""
    
    # Generate timestamped filename in analysis directory
    timestamped_filename = os.path.join(analysis_dir, f"seo_analysis_{timestamp}.md")
    latest_filename = os.path.join(analysis_dir, "latest_seo_analysis.md")
    
    print(f"\n📝 Creating timestamped SEO report:")
    print(f"📄 Main file: {timestamped_filename}")
    print(f"🔗 Latest copy: {latest_filename}")
    print(f"📊 Analyzing {len(pages)} pages...")
    
    published_pages = [p for p in pages if p['seo']['draft'].lower() != 'true']
    
    # Statistics
    total_pages = len(published_pages)
    pages_with_titles = len([p for p in published_pages if p['seo']['has_title']])
    pages_with_descriptions = len([p for p in published_pages if p['seo']['has_description']])
    pages_with_keywords = len([p for p in published_pages if p['seo']['has_keywords']])
    pages_with_css_issues = len([p for p in published_pages if p['seo']['has_css_in_content']])
    
    # Priority counts
    critical_pages = [p for p in published_pages if p['seo']['priority'] == 'critical']
    high_priority = [p for p in published_pages if p['seo']['priority'] == 'high']
    medium_priority = [p for p in published_pages if p['seo']['priority'] == 'medium']
    low_priority = [p for p in published_pages if p['seo']['priority'] == 'low']
    
    report_content = f"""# 🔍 Enhanced SEO Analysis Report - Faisal Khan LLC

**Generated on:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}  
**Total Pages Analyzed:** {total_pages}  
**Website:** https://faisalkhanllc.xyz

---

## 📊 SEO Health Dashboard

### Critical Stats
- **Pages with Titles:** {pages_with_titles}/{total_pages} ({pages_with_titles/total_pages*100:.1f}%)
- **Pages with Meta Descriptions:** {pages_with_descriptions}/{total_pages} ({pages_with_descriptions/total_pages*100:.1f}%)
- **Pages with SEO Keywords:** {pages_with_keywords}/{total_pages} ({pages_with_keywords/total_pages*100:.1f}%)
- **Pages with CSS Issues:** {pages_with_css_issues}/{total_pages} ({pages_with_css_issues/total_pages*100:.1f}%)

### Priority Breakdown
- 🔴 **Critical Issues:** {len(critical_pages)} pages (missing titles)
- 🟠 **High Priority:** {len(high_priority)} pages (short titles, missing descriptions, CSS issues)  
- 🟡 **Medium Priority:** {len(medium_priority)} pages (minor SEO improvements)
- 🟢 **Good:** {len(low_priority)} pages (no major issues)

---

## 🚨 URGENT: Critical Issues (Fix First)

"""
    
    if critical_pages:
        for page in critical_pages:  # Show ALL critical pages with comprehensive details
            seo = page['seo']
            report_content += f"#### 🔴 {seo['title'] or 'NO TITLE'}\n"
            report_content += f"**URL:** `{page['url_path']}`  \n"
            report_content += f"**File:** `{page['file_path']}`  \n"
            report_content += f"**Description:** {seo['best_description'] or 'No description'}  \n"
            report_content += f"**Word Count:** {seo['word_count']} words  \n"
            report_content += f"**Keywords:** {seo['best_keywords'] or 'No keywords'}  \n"
            report_content += f"**Date:** {seo['date'] or 'No date'}  \n"
            
            # Preview with CSS highlighting if present
            if seo['has_css_in_content']:
                report_content += f"**Preview:** 🚨🚨🚨 CSS DETECTED IN CONTENT 🚨🚨🚨 {seo['clean_preview'][:200]}{'...' if len(seo['clean_preview']) > 200 else ''}  \n"
            else:
                report_content += f"**Preview:** {seo['clean_preview'][:150]}{'...' if len(seo['clean_preview']) > 150 else ''}  \n"
            
            # SEO Field Details
            report_content += f"**Has Meta Description:** {'Yes' if seo['has_description'] else 'No'}  \n"
            if seo['description']:
                report_content += f"**Meta Description:** {seo['description']}  \n"
            if seo['meta_description']:
                report_content += f"**Meta Description Field:** {seo['meta_description']}  \n"
            if seo['summary']:
                report_content += f"**Summary Field:** {seo['summary']}  \n"
            
            report_content += f"**Has SEO Keywords:** {'Yes' if seo['has_keywords'] else 'No'}  \n"
            if seo['keywords']:
                report_content += f"**Keywords Field:** {seo['keywords']}  \n"
            if seo['meta_keywords']:
                report_content += f"**Meta Keywords Field:** {seo['meta_keywords']}  \n"
            
            report_content += f"**Has CSS in Content:** {'Yes' if seo['has_css_in_content'] else 'No'}  \n"
            report_content += f"**Has HTML in Content:** {'Yes' if seo['has_html_in_content'] else 'No'}  \n"
            report_content += f"**Canonical URL:** {seo['canonical'] or 'Not set'}  \n"
            report_content += f"**Robots:** {seo['robots'] or 'Not set'}  \n"
            
            report_content += "**SEO Issues:**\n"
            for issue in seo['seo_issues']:
                if not issue.startswith('✅'):
                    report_content += f"  - {issue}\n"
            for issue in seo['content_issues']:
                if not issue.startswith('✅'):
                    report_content += f"  - {issue}\n"
            report_content += "\n"
    else:
        report_content += "✅ **No critical issues found!**\n\n"
    
    report_content += """---

## 🔴 High Priority Issues (Fix Next)

"""
    
    if high_priority:
        for page in high_priority:  # Show ALL high priority pages with comprehensive details
            seo = page['seo']
            issues_count = len([i for i in seo['seo_issues'] if not i.startswith('✅')]) + \
                         len([i for i in seo['content_issues'] if not i.startswith('✅')])
            
            report_content += f"#### ⚠️({issues_count}) {seo['title'] or 'NO TITLE'}\n"
            report_content += f"**URL:** `{page['url_path']}`  \n"
            report_content += f"**File:** `{page['file_path']}`  \n"
            report_content += f"**Description:** {seo['best_description'] or 'No description'}  \n"
            report_content += f"**Word Count:** {seo['word_count']} words  \n"
            report_content += f"**Keywords:** {seo['best_keywords'] or 'No keywords'}  \n"
            report_content += f"**Date:** {seo['date'] or 'No date'}  \n"
            
            # Preview with CSS highlighting if present
            if seo['has_css_in_content']:
                report_content += f"**Preview:** 🚨🚨🚨 CSS DETECTED IN CONTENT 🚨🚨🚨 {seo['clean_preview'][:200]}{'...' if len(seo['clean_preview']) > 200 else ''}  \n"
            else:
                report_content += f"**Preview:** {seo['clean_preview'][:150]}{'...' if len(seo['clean_preview']) > 150 else ''}  \n"
            
            # SEO Field Details
            report_content += f"**Has Meta Description:** {'Yes' if seo['has_description'] else 'No'}  \n"
            if seo['description']:
                report_content += f"**Meta Description:** {seo['description']}  \n"
            if seo['meta_description']:
                report_content += f"**Meta Description Field:** {seo['meta_description']}  \n"
            if seo['summary']:
                report_content += f"**Summary Field:** {seo['summary']}  \n"
            
            report_content += f"**Has SEO Keywords:** {'Yes' if seo['has_keywords'] else 'No'}  \n"
            if seo['keywords']:
                report_content += f"**Keywords Field:** {seo['keywords']}  \n"
            if seo['meta_keywords']:
                report_content += f"**Meta Keywords Field:** {seo['meta_keywords']}  \n"
            
            report_content += f"**Has CSS in Content:** {'Yes' if seo['has_css_in_content'] else 'No'}  \n"
            report_content += f"**Has HTML in Content:** {'Yes' if seo['has_html_in_content'] else 'No'}  \n"
            report_content += f"**Canonical URL:** {seo['canonical'] or 'Not set'}  \n"
            report_content += f"**Robots:** {seo['robots'] or 'Not set'}  \n"
            
            report_content += "**SEO Issues:**\n"
            for issue in seo['seo_issues']:
                if not issue.startswith('✅'):
                    report_content += f"  - {issue}\n"
            for issue in seo['content_issues']:
                if not issue.startswith('✅'):
                    report_content += f"  - {issue}\n"
            report_content += "\n"
    else:
        report_content += "✅ **No high priority issues!**\n\n"
    
    report_content += f"""---

## 🟡 Medium Priority Issues (Fix When You Have Time)

"""
    
    if medium_priority:
        for page in medium_priority:  # Show ALL medium priority pages with comprehensive details
            seo = page['seo']
            issues_count = len([i for i in seo['seo_issues'] if not i.startswith('✅')]) + \
                         len([i for i in seo['content_issues'] if not i.startswith('✅')])
            
            report_content += f"#### 🟡({issues_count}) {seo['title'] or 'NO TITLE'}\n"
            report_content += f"**URL:** `{page['url_path']}`  \n"
            report_content += f"**File:** `{page['file_path']}`  \n"
            report_content += f"**Description:** {seo['best_description'] or 'No description'}  \n"
            report_content += f"**Word Count:** {seo['word_count']} words  \n"
            report_content += f"**Keywords:** {seo['best_keywords'] or 'No keywords'}  \n"
            report_content += f"**Date:** {seo['date'] or 'No date'}  \n"
            
            # Preview with CSS highlighting if present
            if seo['has_css_in_content']:
                report_content += f"**Preview:** 🚨🚨🚨 CSS DETECTED IN CONTENT 🚨🚨🚨 {seo['clean_preview'][:200]}{'...' if len(seo['clean_preview']) > 200 else ''}  \n"
            else:
                report_content += f"**Preview:** {seo['clean_preview'][:150]}{'...' if len(seo['clean_preview']) > 150 else ''}  \n"
            
            # SEO Field Details
            report_content += f"**Has Meta Description:** {'Yes' if seo['has_description'] else 'No'}  \n"
            if seo['description']:
                report_content += f"**Meta Description:** {seo['description']}  \n"
            if seo['meta_description']:
                report_content += f"**Meta Description Field:** {seo['meta_description']}  \n"
            if seo['summary']:
                report_content += f"**Summary Field:** {seo['summary']}  \n"
            
            report_content += f"**Has SEO Keywords:** {'Yes' if seo['has_keywords'] else 'No'}  \n"
            if seo['keywords']:
                report_content += f"**Keywords Field:** {seo['keywords']}  \n"
            if seo['meta_keywords']:
                report_content += f"**Meta Keywords Field:** {seo['meta_keywords']}  \n"
            
            report_content += f"**Has CSS in Content:** {'Yes' if seo['has_css_in_content'] else 'No'}  \n"
            report_content += f"**Has HTML in Content:** {'Yes' if seo['has_html_in_content'] else 'No'}  \n"
            report_content += f"**Canonical URL:** {seo['canonical'] or 'Not set'}  \n"
            report_content += f"**Robots:** {seo['robots'] or 'Not set'}  \n"
            
            report_content += "**SEO Issues:**\n"
            for issue in seo['seo_issues']:
                if not issue.startswith('✅'):
                    report_content += f"  - {issue}\n"
            for issue in seo['content_issues']:
                if not issue.startswith('✅'):
                    report_content += f"  - {issue}\n"
            
            # If no issues, show what could be improved
            if issues_count == 0:
                report_content += "  - No major issues (minor optimizations possible)\n"
            
            report_content += "\n"
    else:
        report_content += "✅ **No medium priority issues!**\n\n"
    
    report_content += f"""---

## 🟢 Pages in Excellent Shape

"""
    
    if low_priority:
        for page in low_priority:  # Show ALL pages in good shape with comprehensive details
            seo = page['seo']
            
            report_content += f"#### ✅ {seo['title'] or 'NO TITLE'}\n"
            report_content += f"**URL:** `{page['url_path']}`  \n"
            report_content += f"**File:** `{page['file_path']}`  \n"
            report_content += f"**Description:** {seo['best_description'] or 'No description'}  \n"
            report_content += f"**Word Count:** {seo['word_count']} words  \n"
            report_content += f"**Keywords:** {seo['best_keywords'] or 'No keywords'}  \n"
            report_content += f"**Date:** {seo['date'] or 'No date'}  \n"
            
            # Preview with CSS highlighting if present
            if seo['has_css_in_content']:
                report_content += f"**Preview:** 🚨🚨🚨 CSS DETECTED IN CONTENT 🚨🚨🚨 {seo['clean_preview'][:200]}{'...' if len(seo['clean_preview']) > 200 else ''}  \n"
            else:
                report_content += f"**Preview:** {seo['clean_preview'][:150]}{'...' if len(seo['clean_preview']) > 150 else ''}  \n"
            
            # SEO Field Details
            report_content += f"**Has Meta Description:** {'Yes' if seo['has_description'] else 'No'}  \n"
            if seo['description']:
                report_content += f"**Meta Description:** {seo['description']}  \n"
            if seo['meta_description']:
                report_content += f"**Meta Description Field:** {seo['meta_description']}  \n"
            if seo['summary']:
                report_content += f"**Summary Field:** {seo['summary']}  \n"
            
            report_content += f"**Has SEO Keywords:** {'Yes' if seo['has_keywords'] else 'No'}  \n"
            if seo['keywords']:
                report_content += f"**Keywords Field:** {seo['keywords']}  \n"
            if seo['meta_keywords']:
                report_content += f"**Meta Keywords Field:** {seo['meta_keywords']}  \n"
            
            report_content += f"**Has CSS in Content:** {'Yes' if seo['has_css_in_content'] else 'No'}  \n"
            report_content += f"**Has HTML in Content:** {'Yes' if seo['has_html_in_content'] else 'No'}  \n"
            report_content += f"**Canonical URL:** {seo['canonical'] or 'Not set'}  \n"
            report_content += f"**Robots:** {seo['robots'] or 'Not set'}  \n"
            
            # Show SEO strengths instead of issues
            report_content += "**SEO Strengths:**\n"
            if seo['has_title'] and 30 <= seo['title_length'] <= 60:
                report_content += f"  - ✅ Good title length ({seo['title_length']} chars)\n"
            
            if seo['has_description'] and 120 <= seo['description_length'] <= 160:
                report_content += f"  - ✅ Optimal description length ({seo['description_length']} chars)\n"
            elif seo['has_description']:
                report_content += f"  - ✅ Has description ({seo['description_length']} chars)\n"
            
            if seo['has_keywords']:
                report_content += "  - ✅ Has SEO keywords\n"
            
            if seo['word_count'] >= 200:
                report_content += f"  - ✅ Good content length ({seo['word_count']} words)\n"
            
            if not seo['has_css_in_content']:
                report_content += "  - ✅ Clean content (no CSS issues)\n"
            
            if not seo['has_html_in_content']:
                report_content += "  - ✅ No HTML issues\n"
            
            report_content += "\n"
    else:
        report_content += "✅ **All pages need some SEO work!**\n\n"
    
    report_content += f"""---

## 📝 Quick Fix Recommendations

### 1. Fix CSS in Content Issue ({pages_with_css_issues} pages)
**Problem:** CSS styling code appears in your markdown content  
**Example:** `<style> .theme-bullet {{ background-color: #000000 !important; }}`  
**Solution:** Move this CSS to your theme's CSS files  

### 2. Expand Short Titles
**Problem:** Titles under 30 characters don't perform well in Google  
**Examples to fix:**
"""
    
    # Show examples of short titles
    short_title_pages = [p for p in published_pages if p['seo']['has_title'] and p['seo']['title_length'] < 30]
    for page in short_title_pages[:5]:
        old_title = page['seo']['title']
        report_content += f"- '{old_title}' → 'Your Business + Location + Service' (30+ chars)\n"
    
    report_content += f"""

### 3. Add Missing Meta Descriptions ({total_pages - pages_with_descriptions} pages)
**Add to front matter:**
```yaml
description: "Clear 120-160 character description of what this page offers"
```

### 4. Add SEO Keywords ({total_pages - pages_with_keywords} pages)  
**Add to front matter:**
```yaml
keywords: ["main keyword", "secondary keyword", "location", "service"]
```

---

*This enhanced SEO analysis was automatically generated*  
*Last updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*
*Files saved in: seo_analysis/ directory*
"""
    
    # Write the timestamped report
    try:
        # Create timestamped file
        with open(timestamped_filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        # Create "latest" copy for easy access
        with open(latest_filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"✅ Successfully created: {timestamped_filename}")
        print(f"✅ Latest copy saved as: {latest_filename}")
        print(f"📄 File size: {len(report_content):,} characters")
        print(f"🔴 Critical: {len(critical_pages)} | 🟠 High: {len(high_priority)} | 🟡 Medium: {len(medium_priority)} | 🟢 Good: {len(low_priority)}")
        
        # Show file tracking message
        print(f"\n📈 Progress Tracking:")
        print(f"   Keep files in seo_analysis/ to track SEO improvements over time!")
        print(f"   Next run will create: seo_analysis/seo_analysis_{datetime.now().strftime('%Y-%m-%d')}_XX-XX.md")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating {timestamped_filename}: {e}")
        return False

def main():
    """Main function"""
    
    print("🚀 Enhanced Hugo SEO Scanner with CSV Export & Directory Organization")
    print("=" * 70)
    
    hugo_project_path = "/Users/faisalkhan/Dropbox/Hugoproject/faisalkhan"
    content_dir = os.path.join(hugo_project_path, "content")
    
    if not os.path.exists(content_dir):
        print(f"❌ Content directory not found: {content_dir}")
        return
    
    # Ensure analysis directory exists
    analysis_dir = ensure_analysis_directory()
    
    # Enhanced SEO analysis
    pages = scan_hugo_with_enhanced_seo(content_dir)
    
    # Generate timestamp for both files
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    
    # Create both reports with same timestamp in analysis directory
    md_success = create_enhanced_seo_report(pages, timestamp, analysis_dir)
    csv_success = create_enhanced_csv_report(pages, timestamp, analysis_dir)
    
    if md_success and csv_success:
        print("\n🎉 Enhanced SEO analysis completed!")
        print(f"📁 All files saved in: {analysis_dir}/")
        print(f"📋 Check your timestamped files:")
        print(f"   📄 Markdown: {analysis_dir}/seo_analysis_{timestamp}.md")
        print(f"   📊 CSV: {analysis_dir}/seo_analysis_{timestamp}.csv")
        print(f"🔍 Analyzed {len(pages)} pages with priority-based recommendations")
        
        # Show existing SEO analysis files in the directory
        try:
            seo_files = [f for f in os.listdir(analysis_dir) if f.startswith('seo_analysis_') and (f.endswith('.md') or f.endswith('.csv'))]
            if len(seo_files) > 2:
                print(f"\n📚 SEO Analysis History in {analysis_dir}/ ({len(seo_files)} files):")
                for seo_file in sorted(seo_files)[-10:]:  # Show last 10 files
                    file_path = os.path.join(analysis_dir, seo_file)
                    file_size = os.path.getsize(file_path)
                    print(f"   📄 {seo_file} ({file_size:,} bytes)")
                if len(seo_files) > 10:
                    print(f"   ... and {len(seo_files) - 10} older files")
        except Exception as e:
            print(f"⚠️ Could not list existing files: {e}")
            
    elif md_success:
        print("\n⚠️ Markdown report created but CSV failed")
    elif csv_success:
        print("\n⚠️ CSV report created but Markdown failed")
    else:
        print("\n❌ Both reports failed to create")

if __name__ == "__main__":
    main()