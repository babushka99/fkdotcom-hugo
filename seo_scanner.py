#!/usr/bin/env python3
"""
SEO-Enhanced Hugo File Scanner
Scans Hugo content and extracts comprehensive SEO data
"""

import os
import re
from datetime import datetime
from pathlib import Path

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

def extract_content_preview(content):
    """Extract first few lines of actual content (not front matter)"""
    if content.startswith('---'):
        # Skip front matter
        end_marker = content.find('---', 3)
        if end_marker != -1:
            actual_content = content[end_marker + 3:].strip()
        else:
            actual_content = content
    else:
        actual_content = content
    
    # Get first 200 characters of content
    preview = actual_content[:200].replace('\n', ' ').strip()
    return preview

def analyze_seo_data(front_matter, content, file_path):
    """Analyze SEO-related data from page"""
    
    seo_data = {
        # Basic SEO
        'title': front_matter.get('title', 'NO TITLE'),
        'description': front_matter.get('description', ''),
        'summary': front_matter.get('summary', ''),
        'keywords': front_matter.get('keywords', ''),
        'canonical': front_matter.get('canonical', ''),
        
        # Meta tags
        'meta_description': front_matter.get('meta_description', ''),
        'meta_keywords': front_matter.get('meta_keywords', ''),
        'robots': front_matter.get('robots', ''),
        
        # Open Graph (Social Media)
        'og_title': front_matter.get('og_title', ''),
        'og_description': front_matter.get('og_description', ''),
        'og_image': front_matter.get('og_image', ''),
        'og_type': front_matter.get('og_type', ''),
        
        # Twitter Cards
        'twitter_title': front_matter.get('twitter_title', ''),
        'twitter_description': front_matter.get('twitter_description', ''),
        'twitter_image': front_matter.get('twitter_image', ''),
        'twitter_card': front_matter.get('twitter_card', ''),
        
        # Content Analysis
        'word_count': len(content.split()),
        'content_preview': extract_content_preview(content),
        'has_images': 'true' if ('![' in content or '<img' in content) else 'false',
        'has_links': 'true' if ('[' in content and '](' in content) else 'false',
        
        # Hugo-specific
        'weight': front_matter.get('weight', ''),
        'date': front_matter.get('date', ''),
        'lastmod': front_matter.get('lastmod', ''),
        'draft': front_matter.get('draft', ''),
        'featured': front_matter.get('featured', ''),
        'categories': front_matter.get('categories', ''),
        'tags': front_matter.get('tags', ''),
        
        # SEO Issues Detection
        'seo_issues': []
    }
    
    # Detect SEO issues
    if not seo_data['title'] or seo_data['title'] == 'NO TITLE':
        seo_data['seo_issues'].append('Missing title')
    elif len(seo_data['title']) > 60:
        seo_data['seo_issues'].append('Title too long (>60 chars)')
    elif len(seo_data['title']) < 30:
        seo_data['seo_issues'].append('Title too short (<30 chars)')
    
    if not seo_data['description'] and not seo_data['summary'] and not seo_data['meta_description']:
        seo_data['seo_issues'].append('Missing description/summary')
    
    desc_text = seo_data['description'] or seo_data['summary'] or seo_data['meta_description']
    if desc_text and len(desc_text) > 160:
        seo_data['seo_issues'].append('Description too long (>160 chars)')
    
    if seo_data['word_count'] < 200:
        seo_data['seo_issues'].append('Low word count (<200 words)')
    
    if not seo_data['seo_issues']:
        seo_data['seo_issues'].append('No issues detected')
    
    return seo_data

def scan_hugo_content_with_seo(content_dir):
    """Scan Hugo content directory and extract SEO data"""
    
    print(f"🔍 Scanning Hugo content with SEO analysis: {content_dir}")
    print("=" * 60)
    
    all_pages = []
    
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                try:
                    # Read the markdown file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Parse front matter
                    front_matter = parse_front_matter_detailed(content)
                    
                    # Create relative path from content directory
                    rel_path = os.path.relpath(file_path, content_dir)
                    
                    # Determine URL path
                    if file == '_index.md':
                        # Section index page
                        url_path = '/' + '/'.join(rel_path.split('/')[:-1]) + '/'
                        if url_path == '//':
                            url_path = '/'  # Root index
                    else:
                        # Regular page
                        url_path = '/' + rel_path.replace('.md', '/').replace('\\', '/')
                    
                    # Clean up URL path
                    url_path = url_path.replace('//', '/').rstrip('/') + '/'
                    if url_path == '//':
                        url_path = '/'
                    
                    # Extract SEO data
                    seo_data = analyze_seo_data(front_matter, content, file_path)
                    
                    page_info = {
                        'file_path': rel_path,
                        'url_path': url_path,
                        'section': rel_path.split('/')[0] if '/' in rel_path else 'root',
                        'seo': seo_data
                    }
                    
                    all_pages.append(page_info)
                    
                    # Show progress with SEO status
                    issues_count = len([i for i in seo_data['seo_issues'] if i != 'No issues detected'])
                    status = "✅" if issues_count == 0 else f"⚠️({issues_count})"
                    print(f"📄 {status} {rel_path} → {url_path}")
                    
                except Exception as e:
                    print(f"❌ Error reading {file_path}: {e}")
    
    return all_pages

def create_seo_report(pages, output_filename="seo_analysis.md"):
    """Create comprehensive SEO analysis report"""
    
    print(f"\n📝 Creating SEO analysis report: {output_filename}...")
    
    # Filter published pages
    published_pages = [p for p in pages if p['seo']['draft'].lower() != 'true']
    
    # SEO Statistics
    pages_with_titles = len([p for p in published_pages if p['seo']['title'] and p['seo']['title'] != 'NO TITLE'])
    pages_with_descriptions = len([p for p in published_pages if p['seo']['description'] or p['seo']['summary'] or p['seo']['meta_description']])
    pages_with_issues = len([p for p in published_pages if len([i for i in p['seo']['seo_issues'] if i != 'No issues detected']) > 0])
    
    avg_word_count = sum([p['seo']['word_count'] for p in published_pages]) / len(published_pages) if published_pages else 0
    
    report_content = f"""# SEO Analysis Report - Faisal Khan LLC Website

**Generated on:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}  
**Total Pages Analyzed:** {len(published_pages)}  
**Website:** https://faisalkhanllc.xyz

---

## 📊 SEO Overview

### Quick Stats
- **Total Published Pages:** {len(published_pages)}
- **Pages with Titles:** {pages_with_titles} ({pages_with_titles/len(published_pages)*100:.1f}%)
- **Pages with Descriptions:** {pages_with_descriptions} ({pages_with_descriptions/len(published_pages)*100:.1f}%)
- **Pages with SEO Issues:** {pages_with_issues} ({pages_with_issues/len(published_pages)*100:.1f}%)
- **Average Word Count:** {avg_word_count:.0f} words

### SEO Health Score
"""
    
    # Calculate SEO health score
    title_score = (pages_with_titles / len(published_pages)) * 30
    desc_score = (pages_with_descriptions / len(published_pages)) * 30
    content_score = min(avg_word_count / 300, 1) * 20  # 300+ words = full score
    issue_score = ((len(published_pages) - pages_with_issues) / len(published_pages)) * 20
    
    total_score = title_score + desc_score + content_score + issue_score
    
    report_content += f"""
**Overall SEO Score: {total_score:.0f}/100**

- Titles: {title_score:.0f}/30
- Descriptions: {desc_score:.0f}/30  
- Content Quality: {content_score:.0f}/20
- Issue-Free Pages: {issue_score:.0f}/20

---

## 🔍 Pages with SEO Issues

"""
    
    # List pages with issues
    problematic_pages = [p for p in published_pages if len([i for i in p['seo']['seo_issues'] if i != 'No issues detected']) > 0]
    
    if problematic_pages:
        for page in sorted(problematic_pages, key=lambda x: len([i for i in x['seo']['seo_issues'] if i != 'No issues detected']), reverse=True):
            issues = [i for i in page['seo']['seo_issues'] if i != 'No issues detected']
            report_content += f"### {page['seo']['title']}\n"
            report_content += f"**URL:** `{page['url_path']}`  \n"
            report_content += f"**File:** `{page['file_path']}`  \n"
            report_content += f"**Issues ({len(issues)}):**\n"
            for issue in issues:
                report_content += f"- ❌ {issue}\n"
            report_content += f"**Word Count:** {page['seo']['word_count']} words  \n"
            report_content += "\n"
    else:
        report_content += "🎉 **No SEO issues detected across all pages!**\n\n"
    
    report_content += """---

## 📝 Complete Page Inventory with SEO Data

"""
    
    # Group by section
    sections = {}
    for page in published_pages:
        section = page['section']
        if section not in sections:
            sections[section] = []
        sections[section].append(page)
    
    # Report by section
    for section_name in sorted(sections.keys()):
        pages_in_section = sections[section_name]
        report_content += f"### {section_name.title()} Section ({len(pages_in_section)} pages)\n\n"
        
        for page in sorted(pages_in_section, key=lambda x: x['seo']['title']):
            seo = page['seo']
            issues_count = len([i for i in seo['seo_issues'] if i != 'No issues detected'])
            status = "✅" if issues_count == 0 else f"⚠️({issues_count})"
            
            report_content += f"#### {status} {seo['title']}\n"
            report_content += f"**URL:** `{page['url_path']}`  \n"
            report_content += f"**File:** `{page['file_path']}`  \n"
            
            # SEO Details
            if seo['description'] or seo['summary']:
                desc_text = seo['description'] or seo['summary']
                report_content += f"**Description:** {desc_text[:100]}{'...' if len(desc_text) > 100 else ''}  \n"
            
            report_content += f"**Word Count:** {seo['word_count']} words  \n"
            
            if seo['keywords']:
                report_content += f"**Keywords:** {seo['keywords']}  \n"
            
            if seo['date']:
                report_content += f"**Date:** {seo['date']}  \n"
            
            # Content preview
            if seo['content_preview']:
                report_content += f"**Preview:** {seo['content_preview'][:150]}...  \n"
            
            # SEO Issues
            if issues_count > 0:
                issues = [i for i in seo['seo_issues'] if i != 'No issues detected']
                report_content += f"**SEO Issues:**\n"
                for issue in issues:
                    report_content += f"  - {issue}\n"
            
            report_content += "\n"
    
    report_content += f"""---

## 📈 Recommendations

### High Priority
1. **Fix Missing Titles:** {len(published_pages) - pages_with_titles} pages need titles
2. **Add Descriptions:** {len(published_pages) - pages_with_descriptions} pages need meta descriptions
3. **Content Expansion:** Pages under 200 words should be expanded

### Medium Priority
1. **Optimize Title Lengths:** Keep titles between 30-60 characters
2. **Description Lengths:** Keep descriptions under 160 characters
3. **Add Keywords:** Consider adding keyword tags for better organization

### Low Priority
1. **Social Media Tags:** Add Open Graph and Twitter Card tags
2. **Canonical URLs:** Add canonical URLs where needed
3. **Image Optimization:** Add alt text and optimize images

---

*This SEO analysis was automatically generated by the Hugo SEO Scanner*  
*Last updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*
"""
    
    # Write the report
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(report_content)
        print(f"✅ Successfully created {output_filename}")
        print(f"📊 SEO Score: {total_score:.0f}/100")
        print(f"⚠️ Pages with issues: {pages_with_issues}/{len(published_pages)}")
        return True
    except Exception as e:
        print(f"❌ Error creating {output_filename}: {e}")
        return False

def main():
    """Main function"""
    
    print("🚀 Hugo SEO Analysis Scanner")
    print("=" * 40)
    
    # Hugo project path
    hugo_project_path = "/Users/faisalkhan/Dropbox/Hugoproject/faisalkhan"
    content_dir = os.path.join(hugo_project_path, "content")
    
    # Check if content directory exists
    if not os.path.exists(content_dir):
        print(f"❌ Content directory not found: {content_dir}")
        return
    
    # Scan for all pages with SEO analysis
    pages = scan_hugo_content_with_seo(content_dir)
    
    # Create SEO report
    success = create_seo_report(pages, "seo_analysis.md")
    
    if success:
        print("\n🎉 SEO analysis completed!")
        print(f"📋 Check seo_analysis.md for your complete SEO report")
        print(f"🔍 Analyzed {len(pages)} pages for SEO optimization")
    else:
        print("\n❌ There was an error creating the SEO report")

if __name__ == "__main__":
    main()