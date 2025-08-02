#!/usr/bin/env python3
"""
Hugo Solutions Pages Bulk Generator for Faisal Khan LLC - CORRECTED VERSION
Creates all solution pages with proper front matter and structure
Fixed: Date format, layouts, shortcodes
"""

import os
import re
from datetime import datetime

# Base content directory (adjust path as needed)
CONTENT_DIR = "/Users/faisalkhan/Dropbox/Hugoproject/faisalkhan/content"

# Solution categories and their pages
SOLUTIONS_DATA = {
    "licensing": {
        "title": "Licensing & License Sponsorship",
        "description": "Comprehensive licensing solutions for regulated financial services",
        "pages": [
            "Money Transmitter License (MTL)",
            "Money Services Business (MSB)", 
            "Electronic Money Institution (EMI)",
            "Payment Institution (PI)",
            "Small Payment Institution (SPI)",
            "Authorized Payment Institution (API)",
            "Cryptocurrency Licensing",
            "Crypto Exchange License",
            "Crypto Wallet License",
            "License as a Service (LaaS)",
            "Rent-a-License",
            "Bank Sponsorship",
            "Agent of Payee Exemption",
            "International Money Transmitter License",
            "Gambling & Sports Betting Licensing",
            "Marketplace Licensing"
        ]
    },
    "banking": {
        "title": "Banking & Access to Banking",
        "description": "Banking solutions for high-risk and regulated businesses",
        "pages": [
            "MSB-Friendly Bank Accounts",
            "Banking-as-a-Service (BaaS)",
            "Multi-Currency IBANs",
            "SWIFT Access",
            "US Dollar Accounts",
            "Crypto Bank Accounts",
            "High-Risk Banking",
            "Correspondent Banking Relationship (CBR)",
            "Offshore Banking License",
            "Individual Bank Account",
            "Corporate Bank Account"
        ]
    },
    "money-transfer": {
        "title": "Money Transfer & Remittances", 
        "description": "Cross-border payment and remittance solutions",
        "pages": [
            "Money Transfer Business",
            "Cross-Border Payments",
            "Remittance-as-a-Service (RaaS)",
            "Money Transfer as a Service (MTaaS)",
            "Money Transfer Agent",
            "Money Transfer Operator (MTO)"
        ]
    },
    "payments": {
        "title": "Payments & Payment Processing",
        "description": "Comprehensive payment processing and facilitation services",
        "pages": [
            "B2B Payments",
            "Payment Facilitator (PayFac)",
            "Payment Networks",
            "Tax Payment",
            "Tuition Payment", 
            "Payroll FX Solutions",
            "Farm Worker Payment",
            "Major Telco Payments",
            "Healthcare Payments",
            "Seafarer Payment Solutions",
            "Car Auction Payment",
            "Trade Payments",
            "Travel Industry Payments",
            "POBO / COBO"
        ]
    },
    "crypto": {
        "title": "Crypto & Blockchain",
        "description": "Cryptocurrency and blockchain compliance solutions",
        "pages": [
            "Crypto Licensing",
            "Stablecoins Payments",
            "Crypto-based Debit Cards", 
            "Bitcoin Money Transmitter License",
            "Crypto OTC License",
            "DeFi License",
            "Central Bank Digital Currencies (CBDCs)",
            "Initial Coin Offering (ICO)",
            "Decentralized Autonomous Organization (DAO)"
        ]
    },
    "compliance": {
        "title": "Risk & Compliance",
        "description": "AML, KYC, and regulatory compliance solutions",
        "pages": [
            "Anti-Money Laundering (AML)",
            "Know Your Customer (KYC)",
            "Know Your Business (KYB)",
            "Enhanced Due Diligence (EDD)",
            "Politically Exposed Person (PEP)",
            "Sanctions Screening",
            "Risk Assessment",
            "Compliance Training",
            "Surety Bonds"
        ]
    },
    "cards": {
        "title": "Card Services",
        "description": "Card processing, issuance, and merchant services",
        "pages": [
            "Card Processing",
            "Card Issuance", 
            "Merchant Accounts",
            "BIN Sponsorship",
            "Acquiring",
            "Issuing/Issuance"
        ]
    },
    "wallets": {
        "title": "Wallet Solutions",
        "description": "Digital wallet and e-money solutions",
        "pages": [
            "E-Money Wallet",
            "Crypto Wallet",
            "Fiat Wallet",
            "Local Wallet Funding",
            "Readymade Solutions"
        ]
    },
    "fintech": {
        "title": "Fintech & Startups",
        "description": "Solutions for fintech startups and embedded finance",
        "pages": [
            "Build Your Own Bank (BYOB)",
            "Embedded Finance",
            "Crypto-based Projects",
            "Starting a Neo Bank"
        ]
    },
    "industry-specific": {
        "title": "Industry Specific Solutions",
        "description": "Specialized payment solutions for specific industries",
        "pages": [
            "Tax Payment",
            "Bill Payment",
            "Marketplace",
            "Tuition Payment",
            "Payroll",
            "Farm Worker Payments",
            "Local Wallet Funding",
            "Major Telco Payment",
            "Healthcare",
            "Seafarer Payments",
            "Car Auction Payment",
            "POBO/COBO",
            "Trade Payments",
            "Travel Industry"
        ]
    },
    "geographic": {
        "title": "Country Specific Solutions",
        "description": "Jurisdiction-specific licensing and compliance solutions",
        "pages": [
            "USA", "UK", "Canada", "Europe/EEA", "Lithuania", "Estonia", 
            "Turkey", "India", "Pakistan", "Bangladesh", "Nepal", "Japan",
            "South Korea", "China", "Africa", "Sub-Saharan Africa", "South Asia",
            "South-East Asia", "Latin America", "Gulf Cooperation Council (GCC)",
            "NZ/Australia", "Nigeria", "Somalia", "Venezuela", "Georgia",
            "High-Risk Countries", "Sanctioned Countries", "FATF Grey List Countries"
        ]
    },
    "providers": {
        "title": "Solution Providers",
        "description": "Vetted partners and service providers",
        "pages": [
            "Payment Processors & Aggregators",
            "Principle License Holders", 
            "Financial Institutions",
            "Non-Banking Financial Institutions"
        ]
    },
    "high-risk": {
        "title": "High-Risk Businesses",
        "description": "Solutions for high-risk business models",
        "pages": [
            "Licensed Gaming",
            "Sports Betting",
            "Gambling",
            "Cryptocurrency Trading",
            "Check Cashing Business", 
            "Bitcoin ATM Business"
        ]
    },
    "consulting": {
        "title": "Consulting Services",
        "description": "Strategic consulting and advisory services",
        "pages": [
            "Product Development Consulting",
            "Licensing Application Strategy Consulting",
            "Advisory Consultancy Services",
            "Cross-Border Payments Strategy Consulting",
            "Project Evaluation & Advisory Consulting",
            "Global Advisory Program"
        ]
    }
}

def slugify(text):
    """Convert text to URL-friendly slug"""
    # Remove parentheses and their contents
    text = re.sub(r'\([^)]*\)', '', text)
    # Convert to lowercase and replace spaces/special chars with hyphens
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def create_front_matter(title, category, description, parent_section):
    """Create Hugo front matter for a solution page"""
    slug = slugify(title)
    date = datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD format (Hugo standard)
    
    # Determine service type and jurisdictions based on content
    services = ["licensing", "compliance", "payments"]
    jurisdictions = ["usa", "uk", "eu"] if "International" in title else ["usa"]
    
    if "crypto" in title.lower() or "bitcoin" in title.lower():
        services.append("crypto")
    if "bank" in title.lower():
        services.append("banking")
    if "compliance" in category or "aml" in title.lower() or "kyc" in title.lower():
        services = ["compliance", "risk-management"]
        
    front_matter = f'''---
title: "{title}"
date: {date}
draft: false
description: "{description}"
keywords: ["{title.lower()}", "{category}", "licensing", "compliance", "faisal khan"]

# Taxonomies
categories: ["{category}"]
tags: ["{slugify(title)}", "{category}", "financial-services"]
services: {services}
jurisdictions: {jurisdictions}

# SEO
canonicalURL: "https://faisalkhan.com/solutions/{category}/{slug}/"
images: ["/images/solutions/{category}/{slug}.webp"]

# Page settings
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: false

# Schema markup
type: "service"
provider: "Faisal Khan LLC"
areaServed: "Global"

# Contact CTA
showContactCTA: true
contactText: "Ready to get started with {title.lower()}? Contact Faisal Khan LLC for expert consultation."
---'''
    
    return front_matter

def create_page_content(title, category, description):
    """Create basic content template for solution pages"""
    content = f'''
# {title}

{description}

## Overview

[Brief overview of {title} and how Faisal Khan LLC can help]

## Key Features

- Feature 1
- Feature 2  
- Feature 3
- Feature 4

## Who This Is For

This solution is ideal for:

- Business type 1
- Business type 2
- Business type 3

## Process

1. **Initial Consultation** - We assess your specific needs
2. **Strategy Development** - Custom approach for your situation  
3. **Implementation** - Execute the solution with our partners
4. **Ongoing Support** - Continued guidance and support

## Why Choose Faisal Khan LLC

- 15+ years of experience in regulated financial services
- Global network of trusted partners and providers
- Deep expertise in cross-border payments and licensing
- Track record of successful implementations

## Getting Started

Ready to explore {title.lower()} options? Contact Faisal Khan LLC for expert consultation and implementation support.

**[Contact us today →](mailto:contact@faisalkhan.com)**

## Related Solutions

Browse our other solutions in this category or [view all solutions](/solutions/) to find the right fit for your business.
'''
    return content

def create_category_index(category, data):
    """Create index page for each solution category"""
    title = data["title"]
    description = data["description"]
    date = datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD format (Hugo standard)
    
    front_matter = f'''---
title: "{title}"
date: {date}
draft: false
description: "{description}"
keywords: ["{category}", "{title.lower()}", "faisal khan", "consulting"]

# Taxonomies  
categories: ["{category}"]
tags: ["{category}", "solutions", "financial-services"]

# SEO
canonicalURL: "https://faisalkhan.com/solutions/{category}/"
images: ["/images/solutions/{category}/overview.webp"]

# Page settings
ShowToc: true
TocOpen: true
ShowBreadCrumbs: true

# Schema
type: "CollectionPage"
provider: "Faisal Khan LLC"
---'''

    content = f'''
# {title}

{description}

## Available Solutions

*Solutions in this category will be listed below - check back soon or contact us for specific options.*

## Why Choose Our {title}

[Category-specific value proposition]

## Get Started

Contact Faisal Khan LLC to discuss which {title.lower()} option is right for your business.

**[Contact us today →](mailto:contact@faisalkhan.com)**
'''
    
    return front_matter + content

def create_directory_structure():
    """Create the directory structure for all solutions"""
    solutions_dir = os.path.join(CONTENT_DIR, "solutions")
    
    # Create main solutions directory
    os.makedirs(solutions_dir, exist_ok=True)
    
    # Create category directories
    for category in SOLUTIONS_DATA.keys():
        category_dir = os.path.join(solutions_dir, category)
        os.makedirs(category_dir, exist_ok=True)
        print(f"Created directory: {category_dir}")
    
    return solutions_dir

def generate_all_pages():
    """Generate all solution pages and category indexes"""
    solutions_dir = create_directory_structure()
    
    # Create main solutions index
    main_index_content = '''---
title: "Solutions"
date: 2025-08-02
draft: false
description: "Comprehensive solutions for licensing, banking, payments, and compliance in regulated financial services"
keywords: ["solutions", "licensing", "banking", "payments", "compliance", "faisal khan"]

ShowToc: true
TocOpen: true
---

# Our Solutions

Faisal Khan LLC provides comprehensive solutions across the regulated financial services spectrum. From licensing and compliance to banking access and payment processing, we help businesses navigate complex regulatory environments globally.

## Solution Categories

- **[Licensing & License Sponsorship](/solutions/licensing/)** - MTL, MSB, EMI, and more
- **[Banking & Access](/solutions/banking/)** - MSB-friendly accounts and banking solutions  
- **[Money Transfer & Remittances](/solutions/money-transfer/)** - Cross-border payment solutions
- **[Payments & Processing](/solutions/payments/)** - B2B payments and payment facilitation
- **[Crypto & Blockchain](/solutions/crypto/)** - Cryptocurrency compliance and licensing
- **[Risk & Compliance](/solutions/compliance/)** - AML, KYC, and regulatory compliance
- **[Card Services](/solutions/cards/)** - Card processing and issuance
- **[Wallet Solutions](/solutions/wallets/)** - Digital wallet implementations
- **[Fintech & Startups](/solutions/fintech/)** - Solutions for emerging fintech companies
- **[Industry Specific](/solutions/industry-specific/)** - Specialized industry solutions
- **[Geographic Solutions](/solutions/geographic/)** - Country-specific licensing and compliance
- **[Solution Providers](/solutions/providers/)** - Vetted partner network
- **[High-Risk Businesses](/solutions/high-risk/)** - Solutions for challenging business models
- **[Consulting Services](/solutions/consulting/)** - Strategic advisory and consulting

## How We Help

- **Strategic Consulting** - Expert guidance on regulatory requirements
- **Implementation Support** - Hands-on help executing solutions  
- **Partner Network** - Access to vetted service providers
- **Ongoing Compliance** - Continued support for regulatory requirements

## Get Started

Ready to explore our solutions? Contact Faisal Khan LLC for expert consultation tailored to your specific needs.

**[Contact us today →](mailto:contact@faisalkhan.com)**
'''
    
    with open(os.path.join(solutions_dir, "_index.md"), "w") as f:
        f.write(main_index_content)
    print("Created main solutions index")
    
    # Generate category pages and individual solution pages
    for category, data in SOLUTIONS_DATA.items():
        category_dir = os.path.join(solutions_dir, category)
        
        # Create category index
        category_index = create_category_index(category, data)
        with open(os.path.join(category_dir, "_index.md"), "w") as f:
            f.write(category_index)
        print(f"Created category index: {category}")
        
        # Create individual solution pages
        for page_title in data["pages"]:
            slug = slugify(page_title)
            front_matter = create_front_matter(page_title, category, f"Expert {page_title.lower()} solutions from Faisal Khan LLC", data["title"])
            content = create_page_content(page_title, category, f"Professional {page_title.lower()} services tailored to your business needs.")
            
            page_content = front_matter + content
            
            page_file = os.path.join(category_dir, f"{slug}.md")
            with open(page_file, "w") as f:
                f.write(page_content)
            print(f"Created page: {category}/{slug}.md")

if __name__ == "__main__":
    print("🚀 Generating Hugo solution pages - CORRECTED VERSION...")
    print(f"📁 Target directory: {CONTENT_DIR}")
    
    # Check if content directory exists
    if not os.path.exists(CONTENT_DIR):
        print(f"❌ ERROR: Content directory does not exist: {CONTENT_DIR}")
        print("💡 Please update CONTENT_DIR variable to match your Hugo project path")
        exit(1)
    
    generate_all_pages()
    print("\n✅ All solution pages generated successfully!")
    print(f"📁 Total categories: {len(SOLUTIONS_DATA)}")
    print(f"📄 Total pages: {sum(len(data['pages']) for data in SOLUTIONS_DATA.values())}")
    print("\n🎯 Features included:")
    print("✅ YYYY-MM-DD date format (Hugo standard)")
    print("✅ No problematic layouts")
    print("✅ No broken shortcodes")
    print("✅ Clean Hugo front matter")
    print("\n🚀 Ready to test with: hugo server")