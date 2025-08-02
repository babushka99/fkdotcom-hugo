#!/usr/bin/env python3
"""
Hugo Resources Section Generator for Faisal Khan LLC
Creates ONLY the Resources section - does not touch existing solutions
"""

import os
import re
from datetime import datetime

# Base content directory (adjust path as needed)
CONTENT_DIR = "/Users/faisalkhan/Dropbox/Hugoproject/faisalkhan/content"

# Resources data
RESOURCES_DATA = {
    "title": "Resources",
    "description": "Educational resources, tools, and knowledge base for financial services",
    "pages": [
        "Education",
        "Knowledge-Base",
        "Bootcamp", 
        "Online Training",
        "Diagrams",
        "Documents",
        "How-To's",
        "Financial Modeling",
        "Forms",
        "Tools",
        "Case Studies"
    ]
}

def slugify(text):
    """Convert text to URL-friendly slug"""
    # Remove parentheses and their contents
    text = re.sub(r'\([^)]*\)', '', text)
    # Convert to lowercase and replace spaces/special chars with hyphens
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def create_front_matter(title, description):
    """Create Hugo front matter for a resource page"""
    slug = slugify(title)
    date = datetime.now().strftime("%Y-%m-%d")
    
    front_matter = f'''---
title: "{title}"
date: {date}
draft: false
description: "{description}"
keywords: ["{title.lower()}", "resources", "education", "faisal khan"]

# Taxonomies
categories: ["resources"]
tags: ["{slugify(title)}", "resources", "education"]
services: ["consulting", "education"]
jurisdictions: ["global"]

# SEO
canonicalURL: "https://faisalkhan.com/resources/{slug}/"
images: ["/images/resources/{slug}.webp"]

# Page settings
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: false

# Schema markup
type: "article"
provider: "Faisal Khan LLC"
areaServed: "Global"
---'''
    
    return front_matter

def create_page_content(title):
    """Create basic content template for resource pages"""
    content = f'''## Overview

[Brief overview of {title} and how it helps in financial services]

## What You'll Learn

- Key concept 1
- Key concept 2  
- Key concept 3
- Key concept 4

## Who This Is For

This resource is ideal for:

- Financial services professionals
- Fintech entrepreneurs
- Compliance officers
- Business owners seeking licensing

## Topics Covered

1. **Foundation** - Basic concepts and principles
2. **Implementation** - Practical application steps  
3. **Best Practices** - Industry standards and recommendations
4. **Advanced Topics** - Complex scenarios and solutions

## Key Benefits

- Comprehensive understanding of {title.lower()}
- Practical tools and templates
- Expert insights from 15+ years experience
- Real-world case studies and examples

## Getting Started

Ready to dive into {title.lower()}? This resource provides everything you need to understand and implement these concepts in your business.

## Related Resources

Browse our other resources or [contact us](mailto:contact@faisalkhan.com) for personalized guidance on your specific needs.
'''
    return content

def create_resources_index():
    """Create index page for resources section"""
    date = datetime.now().strftime("%Y-%m-%d")
    
    front_matter = f'''---
title: "Resources"
date: {date}
draft: false
description: "Educational resources, tools, and knowledge base for financial services"
keywords: ["resources", "education", "financial services", "faisal khan"]

# Taxonomies  
categories: ["resources"]
tags: ["resources", "education", "financial-services"]

# SEO
canonicalURL: "https://faisalkhan.com/resources/"
images: ["/images/resources/overview.webp"]

# COMPLETELY DISABLE AUTO-LISTING
type: "page"
layout: "single"
_build:
  list: false

# Schema
provider: "Faisal Khan LLC"
---'''

    # Generate bullet list with theme-responsive bullets and links
    solutions_list = ""
    for page_title in RESOURCES_DATA["pages"]:
        slug = slugify(page_title)
        solutions_list += f'<li style="list-style: none; position: relative; padding-left: 20px; margin-bottom: 8px;"><span class="theme-bullet" style="position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 8px; height: 8px; background-color: #000000; display: inline-block;"></span><a href="/resources/{slug}/" style="text-decoration: none; color: inherit;">{page_title}</a></li>\n'

    content = f'''<style>
/* Theme-responsive bullet colors */
.theme-bullet {{
  background-color: #000000 !important; /* Black in light mode */
}}

.dark .theme-bullet {{
  background-color: #ffffff !important; /* White in dark mode */
}}
</style>

## Available Resources

<ul style="padding-left: 0; margin: 20px 0;">
{solutions_list}
</ul>

## Why Use Our Resources

Our educational resources are built from 15+ years of hands-on experience in regulated financial services. Each resource provides practical, actionable guidance you can implement immediately.

## Resource Categories

- **Educational Materials** - Foundational knowledge and advanced concepts
- **Tools & Templates** - Ready-to-use forms, diagrams, and models
- **Case Studies** - Real-world examples and lessons learned
- **Training Programs** - Structured learning paths and bootcamps

## Get Started

Explore our resources above, or [contact us](mailto:contact@faisalkhan.com) for personalized guidance on your specific educational needs.

**[Contact us today →](mailto:contact@faisalkhan.com)**
'''
    
    return front_matter + content

def generate_resources_section():
    """Generate only the resources section"""
    # Create resources directory
    resources_dir = os.path.join(CONTENT_DIR, "resources")
    os.makedirs(resources_dir, exist_ok=True)
    print(f"Created directory: {resources_dir}")
    
    # Create resources index
    resources_index = create_resources_index()
    with open(os.path.join(resources_dir, "_index.md"), "w") as f:
        f.write(resources_index)
    print("Created resources index")
    
    # Create individual resource pages
    for page_title in RESOURCES_DATA["pages"]:
        slug = slugify(page_title)
        front_matter = create_front_matter(page_title, f"Expert {page_title.lower()} resources from Faisal Khan LLC")
        content = create_page_content(page_title)
        
        page_content = front_matter + content
        
        page_file = os.path.join(resources_dir, f"{slug}.md")
        with open(page_file, "w") as f:
            f.write(page_content)
        print(f"Created resource page: {slug}.md")

if __name__ == "__main__":
    print("🚀 Generating Hugo Resources section only...")
    print(f"📁 Target directory: {CONTENT_DIR}")
    
    # Check if content directory exists
    if not os.path.exists(CONTENT_DIR):
        print(f"❌ ERROR: Content directory does not exist: {CONTENT_DIR}")
        print("💡 Please update CONTENT_DIR variable to match your Hugo project path")
        exit(1)
    
    generate_resources_section()
    print("\n✅ Resources section generated successfully!")
    print(f"📁 Created: /resources/ directory")
    print(f"📄 Created: {len(RESOURCES_DATA['pages'])} resource pages")
    print("\n🎯 Features included:")
    print("✅ Theme-responsive black/white bullets")
    print("✅ No automatic Hugo card generation")
    print("✅ Clean bullet list navigation")
    print("✅ Educational content templates")
    print("\n🚀 Ready to test with: hugo server")