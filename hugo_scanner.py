#!/usr/bin/env python3
"""
Fixed Local Hugo File Scanner
Scans the /content/ directory of Hugo project to find all pages
"""

import os
import re
from datetime import datetime
from pathlib import Path

def parse_front_matter(content):
    """Extract front matter from markdown file"""
    front_matter = {}
    
    # Check for YAML front matter (--- at start)
    if content.startswith('---'):
        try:
            # Find the end of front matter
            end_marker = content.find('---', 3)
            if end_marker != -1:
                front_matter_text = content[3:end_marker].strip()
                
                # Parse basic front matter fields
                for line in front_matter_text.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        key = key.strip()
                        value = value.strip().strip('"\'')
                        front_matter[key] = value
        except:
            pass
    
    return front_matter

def scan_hugo_content(content_dir):
    """Scan Hugo content directory for all markdown files"""
    
    print(f"🔍 Scanning Hugo content directory: {content_dir}")
    print("=" * 50)
    
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
                    front_matter = parse_front_matter(content)
                    
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
                    
                    page_info = {
                        'file_path': rel_path,
                        'url_path': url_path,
                        'title': front_matter.get('title', 'Untitled'),
                        'date': front_matter.get('date', ''),
                        'draft': front_matter.get('draft', '').lower() == 'true',
                        'weight': front_matter.get('weight', ''),
                        'section': rel_path.split('/')[0] if '/' in rel_path else 'root'
                    }
                    
                    all_pages.append(page_info)
                    print(f"📄 Found: {rel_path} → {url_path}")
                    
                except Exception as e:
                    print(f"❌ Error reading {file_path}: {e}")
    
    return all_pages

def create_pages_inventory(pages, output_filename="listofpages.md"):
    """Create a markdown file with all discovered pages"""
    
    print(f"\n📝 Creating {output_filename}...")
    
    # Filter out draft pages
    published_pages = [p for p in pages if not p['draft']]
    draft_pages = [p for p in pages if p['draft']]
    
    markdown_content = f"""# Hugo Content Pages - Complete Inventory

**Generated on:** {datetime.now().strftime('%B %d, %Y at %I:%M %p')}  
**Total Pages Found:** {len(pages)}  
**Published Pages:** {len(published_pages)}  
**Draft Pages:** {len(draft_pages)}  

---

## Published Pages ({len(published_pages)} pages)

"""
    
    # Group published pages by section
    sections = {}
    for page in published_pages:
        section = page['section']
        if section not in sections:
            sections[section] = []
        sections[section].append(page)
    
    # Sort sections
    for section_name in sorted(sections.keys()):
        pages_in_section = sections[section_name]
        
        markdown_content += f"### {section_name.title()} Section ({len(pages_in_section)} pages)\n\n"
        
        # Sort pages in section by weight, then by title
        pages_in_section.sort(key=lambda x: (x['weight'] if x['weight'] else '999', x['title']))
        
        for page in pages_in_section:
            markdown_content += f"- **{page['title']}**  \n"
            markdown_content += f"  File: `{page['file_path']}`  \n"
            markdown_content += f"  URL: `{page['url_path']}`  \n"
            if page['date']:
                markdown_content += f"  Date: {page['date']}  \n"
            if page['weight']:
                markdown_content += f"  Weight: {page['weight']}  \n"
            markdown_content += "\n"
    
    if draft_pages:
        markdown_content += f"""---

## Draft Pages ({len(draft_pages)} pages)

*These pages are not published on the live website*

"""
        
        # Group draft pages by section
        draft_sections = {}
        for page in draft_pages:
            section = page['section']
            if section not in draft_sections:
                draft_sections[section] = []
            draft_sections[section].append(page)
        
        for section_name in sorted(draft_sections.keys()):
            pages_in_section = draft_sections[section_name]
            
            markdown_content += f"### {section_name.title()} Section ({len(pages_in_section)} draft pages)\n\n"
            
            for page in pages_in_section:
                markdown_content += f"- **{page['title']}** (DRAFT)  \n"
                markdown_content += f"  File: `{page['file_path']}`  \n"
                markdown_content += f"  Would be URL: `{page['url_path']}`  \n"
                markdown_content += "\n"
    
    markdown_content += f"""---

## File Structure Summary

"""
    
    # Show sections with page counts
    for section_name in sorted(sections.keys()):
        page_count = len(sections[section_name])
        markdown_content += f"- **{section_name.title()}:** {page_count} pages\n"
    
    markdown_content += f"""

---

## Quick Stats

- **Total markdown files:** {len(pages)}
- **Unique sections:** {len(set(p['section'] for p in pages))}
- **Index pages (_index.md):** {len([p for p in pages if p['file_path'].endswith('_index.md')])}
- **Regular pages:** {len([p for p in pages if not p['file_path'].endswith('_index.md')])}
- **Pages with dates:** {len([p for p in pages if p['date']])}
- **Pages with weights:** {len([p for p in pages if p['weight']])}

---

*This file was automatically generated by the Hugo File Scanner*  
*Last updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*
"""
    
    # Write to the specified output file
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"✅ Successfully created {output_filename}")
        print(f"📊 Found {len(pages)} total pages ({len(published_pages)} published, {len(draft_pages)} drafts)")
        return True
    except Exception as e:
        print(f"❌ Error creating {output_filename}: {e}")
        return False

def main():
    """Main function"""
    
    print("🚀 Hugo Local File Scanner - FIXED VERSION")
    print("=" * 50)
    
    # Default Hugo content directory
    hugo_project_path = "/Users/faisalkhan/Dropbox/Hugoproject/faisalkhan"
    content_dir = os.path.join(hugo_project_path, "content")
    
    # Check if content directory exists
    if not os.path.exists(content_dir):
        print(f"❌ Content directory not found: {content_dir}")
        print("Please update the hugo_project_path in the script or run from your Hugo project directory")
        return
    
    # Scan for all pages
    pages = scan_hugo_content(content_dir)
    
    # Create markdown file with correct filename
    success = create_pages_inventory(pages, "listofpages.md")
    
    if success:
        print("\n🎉 Hugo file scanning completed!")
        print(f"📋 Check listofpages.md for the complete inventory")
        print(f"🗂️ Your website has {len(pages)} total pages!")
    else:
        print("\n❌ There was an error creating the file")

if __name__ == "__main__":
    main()