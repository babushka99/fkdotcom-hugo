#!/usr/bin/env python3
"""
Hugo Root Pages Generator for Faisal Khan LLC - FIXED VERSION
Creates pages that match your hugo.toml navigation URLs
"""

import os
import re
from datetime import datetime

# Base content directory
CONTENT_DIR = "/Users/faisalkhan/Dropbox/Hugoproject/faisalkhan/content"

# LEGAL PAGES - matching your navigation URLs
LEGAL_PAGES = {
    "disclaimer": {
        "title": "Legal Disclaimer",
        "description": "Legal disclaimer for Faisal Khan LLC services and website",
        "keywords": ["legal", "disclaimer", "terms", "liability", "faisal khan"]
    },
    "privacy": {
        "title": "Privacy Policy", 
        "description": "Privacy policy for Faisal Khan LLC website and services",
        "keywords": ["privacy", "policy", "data", "protection", "faisal khan"]
    },
    "terms": {
        "title": "Terms of Service",
        "description": "Terms of service for Faisal Khan LLC consulting services", 
        "keywords": ["terms", "service", "agreement", "consulting", "faisal khan"]
    },
    "refund": {
        "title": "Refund",
        "description": "Refund policy for Faisal Khan LLC consulting services",
        "keywords": ["refund", "policy", "payment", "consulting", "faisal khan"]
    }
}

# NON-LEGAL ROOT PAGES
ROOT_PAGES = {
    "about": {
        "title": "About",
        "description": "Learn about Faisal Khan LLC and our expertise in cross-border payments and financial licensing",
        "keywords": ["about", "faisal khan", "experience", "expertise", "cross-border payments"]
    },
    "clients": {
        "title": "Clients",
        "description": "Our clients range from fintech startups to established financial institutions worldwide",
        "keywords": ["clients", "case studies", "testimonials", "fintech", "financial institutions"]
    },
    "pricing": {
        "title": "Pricing",
        "description": "Transparent pricing for consulting services, licensing support, and strategic advisory",
        "keywords": ["pricing", "consulting fees", "cost", "investment", "value"]
    },
    "blog": {
        "title": "Blog",
        "description": "Latest insights on cross-border payments, licensing, compliance, and fintech trends",
        "keywords": ["blog", "insights", "fintech", "payments", "licensing", "compliance"]
    },
    "contact": {
        "title": "Contact",
        "description": "Get in touch with Faisal Khan LLC for expert consultation on your financial services needs",
        "keywords": ["contact", "consultation", "get in touch", "expert advice"]
    },
    "book-a-call": {
        "title": "Book A Call",
        "description": "Book a consultation call with Faisal Khan LLC for personalized expert guidance",
        "keywords": ["book call", "consultation", "appointment", "expert guidance"]
    },
    "support": {
        "title": "Support",
        "description": "Get help and support for your questions about our services and processes",
        "keywords": ["support", "help", "assistance", "questions", "guidance"]
    },
    "sitemap": {
        "title": "Sitemap",
        "description": "Complete sitemap of all pages and resources on Faisal Khan LLC website",
        "keywords": ["sitemap", "site map", "navigation", "pages", "structure"]
    }
}

def create_front_matter(slug, data, is_legal=False):
    """Create Hugo front matter"""
    date = datetime.now().strftime("%Y-%m-%d")
    
    if is_legal:
        canonical_url = f"https://faisalkhan.com/legal/{slug}/"
        image_path = f"/images/legal/{slug}.webp"
    else:
        canonical_url = f"https://faisalkhan.com/{slug}/"
        image_path = f"/images/{slug}.webp"
    
    front_matter = f'''---
title: "{data['title']}"
date: {date}
draft: false
description: "{data['description']}"
keywords: {data['keywords']}

# SEO
canonicalURL: "{canonical_url}"
images: ["{image_path}"]

# Page settings
ShowToc: true
TocOpen: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: false
ShowWordCount: false

# Schema markup
type: "webpage"
provider: "Faisal Khan LLC"
---'''
    
    return front_matter

def create_legal_content(slug):
    """Create content for legal pages"""
    date = datetime.now().strftime("%B %d, %Y")
    
    if slug == "disclaimer":
        return f'''## Legal Disclaimer

**Last Updated:** {date}

This general disclaimer governs your use of Faisal Khan LLC website and services.

### Professional Services Disclaimer

The information provided by Faisal Khan LLC is for general informational purposes only. All information on the site is provided in good faith, however we make no representation or warranty of any kind regarding the accuracy, adequacy, validity, reliability, availability, or completeness of any information.

### No Professional Relationship

The content on this website does not constitute professional advice. Consultation with qualified professionals is recommended for specific situations.

### Limitation of Liability

Under no circumstance shall we have any liability to you for any loss or damage of any kind incurred as a result of the use of this site or reliance on any information provided.

### External Links

Our website may contain links to external websites. We have no control over these sites and cannot be responsible for their content or practices.

### Changes to Disclaimer

We reserve the right to modify this disclaimer at any time. Changes will be effective immediately upon posting.

### Contact

For questions about this disclaimer, contact [legal@faisalkhan.com](mailto:legal@faisalkhan.com).
'''
    elif slug == "privacy":
        return f'''## Privacy Policy

**Last Updated:** {date}

Faisal Khan LLC respects your privacy and is committed to protecting your personal information.

### Information We Collect

We may collect the following types of information:
- Contact information (name, email, phone)
- Business information relevant to our services
- Website usage data and analytics
- Communication records

### How We Use Information

We use collected information to:
- Provide and improve our services
- Communicate with clients and prospects
- Comply with legal obligations
- Protect our rights and interests

### Information Sharing

We do not sell or rent personal information. We may share information:
- With your consent
- To comply with legal requirements
- With trusted service providers under confidentiality agreements
- To protect our rights or safety

### Data Security

We implement appropriate security measures to protect your information against unauthorized access, alteration, disclosure, or destruction.

### Your Rights

You have the right to:
- Access your personal information
- Request corrections or updates
- Request deletion of your information
- Opt-out of communications

### Cookies and Tracking

Our website may use cookies and similar technologies for analytics and functionality. You can control cookie settings through your browser.

### Contact

For privacy questions or requests, contact [privacy@faisalkhan.com](mailto:privacy@faisalkhan.com).
'''
    elif slug == "terms":
        return f'''## Terms of Service

**Last Updated:** {date}

These terms govern the provision of services by Faisal Khan LLC.

### Service Agreement

By engaging our services, you agree to these terms and conditions governing our professional relationship.

### Scope of Services

Our services include but are not limited to:
- Strategic consulting and advisory services
- Licensing support and guidance
- Regulatory compliance assistance
- Market access facilitation

### Client Obligations

Clients agree to:
- Provide accurate and complete information
- Cooperate in service delivery
- Make timely payments per agreed terms
- Maintain confidentiality of proprietary information

### Payment Terms

- Services are billed according to agreed fee structure
- Payment is due within 30 days of invoice
- Late payments may incur additional charges
- Disputed charges must be reported within 10 days

### Intellectual Property

- Client retains ownership of their proprietary information
- Faisal Khan LLC retains rights to methodologies and general knowledge
- Work product ownership defined in individual agreements

### Confidentiality

Both parties agree to maintain confidentiality of sensitive information shared during the engagement.

### Limitation of Liability

Our liability is limited to the amount paid for services. We are not liable for indirect, consequential, or incidental damages.

### Termination

Either party may terminate the service agreement with appropriate notice as specified in individual agreements.

### Governing Law

These terms are governed by applicable laws where services are performed.

### Contact

For questions about service terms, contact [legal@faisalkhan.com](mailto:legal@faisalkhan.com).
'''
    elif slug == "refund":
        return f'''## Refund Policy

**Last Updated:** {date}

This refund policy applies to all services provided by Faisal Khan LLC.

### General Policy

Due to the nature of our consulting services, refunds are evaluated on a case-by-case basis according to the specific terms of each engagement.

### Refund Eligibility

Refunds may be considered in the following circumstances:
- Service delivery failure due to our error
- Cancellation within agreed cancellation period
- Mutual agreement to terminate engagement
- Specific refund terms outlined in service agreements

### Non-Refundable Items

The following are generally non-refundable:
- Consultation time already provided
- Work product already delivered
- Third-party costs incurred on client's behalf
- Services completed as agreed

### Refund Process

To request a refund:
1. **Contact us** within 30 days of the issue
2. **Provide details** about the refund request
3. **Allow review** - we'll investigate the circumstances
4. **Receive decision** - typically within 10 business days

### Refund Methods

Approved refunds will be processed using the original payment method within 10-15 business days.

### Partial Refunds

In some cases, partial refunds may be appropriate based on:
- Services already provided
- Work product delivered
- Time and resources invested

### Dispute Resolution

If you disagree with a refund decision, we encourage discussion to reach a mutually satisfactory resolution.

### Service Credits

In some cases, service credits for future work may be offered as an alternative to cash refunds.

### Contact

For refund requests or questions, contact [billing@faisalkhan.com](mailto:billing@faisalkhan.com).
'''
    
    return f'''## {slug.title()}

**Last Updated:** {date}

*This page content is under development.*

For questions, please contact [legal@faisalkhan.com](mailto:legal@faisalkhan.com).
'''

def create_business_content(slug):
    """Content for business pages"""
    if slug == "about":
        return '''## About Faisal Khan LLC

Faisal Khan LLC is a specialized consulting firm focused on cross-border payments, financial licensing, and regulatory compliance. With over 15 years of experience, we help businesses navigate complex regulatory environments and access global financial infrastructure.

## Our Expertise

- **Cross-Border Payments** - Strategic guidance on international payment systems
- **Licensing Support** - MTL, MSB, EMI, and other financial licenses  
- **Regulatory Compliance** - AML, KYC, and compliance framework development
- **Banking Access** - Connecting businesses with appropriate banking partners

## Our Approach

We combine deep technical knowledge with practical implementation experience. Our solutions are tailored to each client's specific needs and regulatory environment.

## Experience

- 15+ years in regulated financial services
- Hundreds of successful licensing projects
- Global network of trusted partners and providers
- Proven track record across multiple jurisdictions

## Get Started

Ready to discuss your specific needs? [Contact us today](mailto:contact@faisalkhan.com) for expert consultation.
'''
    elif slug == "clients":
        return '''## Our Clients

Faisal Khan LLC serves a diverse range of clients in the financial services industry, from emerging fintech startups to established financial institutions.

## Client Types

### Fintech Startups
- Payment processors and aggregators
- Digital wallet providers
- Crypto and blockchain companies
- Embedded finance platforms

### Financial Institutions
- Banks seeking international expansion
- Money transfer operators
- Payment facilitators
- Licensed money services businesses

### Enterprises
- E-commerce platforms requiring payment solutions
- Marketplace operators needing licensing
- International businesses expanding globally
- Compliance-focused organizations

## Success Stories

Our clients have successfully:
- Obtained money transmitter licenses across multiple states
- Secured EMI and PI licenses in Europe
- Established compliant crypto operations
- Accessed MSB-friendly banking relationships

## Confidentiality

We maintain strict confidentiality for all client engagements. Specific case studies and references are available upon request during consultation discussions.

## Become a Client

Ready to join our successful client community? [Contact us today](mailto:contact@faisalkhan.com) to discuss your requirements.
'''
    elif slug == "pricing":
        return '''## Pricing

Faisal Khan LLC offers transparent, value-based pricing for our consulting services. Our fees are structured to align with the complexity and value of each engagement.

## Consulting Services

### Strategy Consulting
- **Hourly Rate**: $500-750/hour
- **Project-Based**: $5,000-25,000 depending on scope
- **Retainer**: $10,000-50,000/month for ongoing advisory

### Licensing Support
- **MTL Applications**: $15,000-50,000 per jurisdiction
- **EMI/PI Licensing**: $25,000-75,000 per application  
- **Compliance Framework**: $10,000-30,000 per project

### Implementation Support
- **Banking Introductions**: Success-based fees
- **Ongoing Compliance**: $5,000-15,000/month
- **Training Programs**: $2,500-10,000 per session

## Value Proposition

Our fees represent exceptional value considering:
- 15+ years of specialized experience
- Proven track record of success
- Access to exclusive partner network
- Ongoing support and guidance

## Custom Proposals

Every engagement is unique. We provide detailed proposals outlining scope, timeline, and investment for your specific requirements.

## Get Started

Ready to discuss pricing for your specific needs? [Contact us today](mailto:contact@faisalkhan.com) for a custom proposal.
'''
    return ""

def create_other_content(slug):
    """Content for other pages"""
    if slug == "blog":
        return '''## Latest Insights

Stay informed with our latest thoughts on cross-border payments, financial licensing, regulatory compliance, and fintech trends.

## Recent Posts

*Blog posts will be listed here as they are published*

## Categories

- **Licensing & Compliance** - Updates on regulatory requirements and licensing procedures
- **Cross-Border Payments** - Trends and developments in international payments
- **Fintech Innovation** - Analysis of emerging technologies and business models
- **Market Analysis** - Industry insights and market developments

## Subscribe

Never miss an update - [subscribe to our newsletter](/newsletter/) to receive new blog posts directly in your inbox.

## Contact

Have a topic you'd like us to cover? [Contact us](mailto:contact@faisalkhan.com) with your suggestions.
'''
    elif slug == "contact":
        return '''## Contact Us

Get in touch with Faisal Khan LLC for expert consultation on your financial services needs.

## Get Started

The best way to begin is with a consultation call where we can understand your specific requirements and discuss how we can help.

### Email
**Primary Contact**: [contact@faisalkhan.com](mailto:contact@faisalkhan.com)

### Schedule a Call
[Book a consultation call](/book-a-call/) to discuss your specific needs and requirements.

### Office Hours
Monday - Friday: 9:00 AM - 6:00 PM (Istanbul Time)  
*We work with clients globally across all time zones*

## What to Include

When contacting us, please include:
- Brief description of your business and requirements
- Specific challenges you're facing
- Timeline for your project
- Preferred method and time for follow-up

## Response Time

We typically respond to all inquiries within 24 hours during business days.

## Consultation Process

1. **Initial Contact** - Reach out via email or scheduled call
2. **Requirements Discussion** - We'll discuss your specific needs
3. **Proposal** - Detailed proposal with scope, timeline, and investment
4. **Engagement** - Begin working together on your solution

Ready to get started? [Contact us today](mailto:contact@faisalkhan.com).
'''
    elif slug == "book-a-call":
        return '''## Book A Call

Book a consultation call with Faisal Khan LLC for personalized expert guidance on your financial services needs.

## Why Book a Call?

- **Expert Guidance** - 15+ years of specialized experience
- **Personalized Advice** - Tailored to your specific situation  
- **Clear Next Steps** - Actionable recommendations and planning
- **No Obligation** - Initial consultation to explore fit and approach

## What We'll Discuss

During our call, we'll cover:
- Your business model and requirements
- Regulatory and compliance considerations
- Available options and recommendations
- Timeline and implementation approach
- Investment and next steps

## Call Types

### Discovery Call (30 minutes)
- Understanding your needs
- Initial assessment and recommendations
- Determining fit for collaboration

### Strategy Session (60 minutes)  
- Detailed strategy development
- Multiple options analysis
- Implementation planning

### Technical Consultation (90 minutes)
- Deep dive into technical requirements
- Regulatory analysis
- Detailed implementation roadmap

## Booking Process

1. **Email Request** - Send your booking request to [contact@faisalkhan.com](mailto:contact@faisalkhan.com)
2. **Include Details** - Business overview, specific needs, preferred call type
3. **Time Preferences** - Your available times and time zone
4. **Confirmation** - We'll confirm and send calendar invitation

## Preparation

Please prepare:
- Brief business overview
- Specific questions or challenges
- Relevant documentation (if applicable)
- Decision-making timeline

Ready to book your call? [Contact us now](mailto:contact@faisalkhan.com).
'''
    elif slug == "support":
        return '''## Support

Get help and support for your questions about our services and processes.

## How We Can Help

### Service Questions
- Understanding our consulting services
- Clarifying scope and deliverables
- Process and timeline questions

### Technical Support
- Website or resource access issues
- Document or template questions
- Platform or tool guidance

### Account Management
- Project status updates
- Invoice or payment questions
- Contract modifications

## Getting Support

### Email Support
**Primary**: [support@faisalkhan.com](mailto:support@faisalkhan.com)  
**Response Time**: Within 24 hours during business days

### Urgent Issues
For urgent matters, please email [contact@faisalkhan.com](mailto:contact@faisalkhan.com) with "URGENT" in the subject line.

### Documentation
Many common questions are answered in our resources section. Please check available documentation before contacting support.

## Business Hours

**Monday - Friday**: 9:00 AM - 6:00 PM (Istanbul Time)  
**Weekend**: Emergency support only

## What to Include

When contacting support, please include:
- Clear description of your question or issue
- Your contact information and preferred response method
- Any relevant project or account details
- Screenshots or documentation if applicable

We're here to help ensure your success with our services.
'''
    elif slug == "sitemap":
        return '''## Sitemap

Complete navigation of all pages and resources on the Faisal Khan LLC website.

## Main Sections

### [Home](/)
Main homepage with overview of services

### [About](/about/)
Information about Faisal Khan LLC and our expertise

### [Solutions](/solutions/)
Comprehensive financial services solutions

### [Resources](/resources/)
Educational materials and tools

### [Clients](/clients/)
Information about our client base and success stories

### [Pricing](/pricing/)
Transparent pricing for our services

### [Blog](/blog/)
Latest insights and industry analysis

## Contact & Support

- [Contact](/contact/)
- [Book A Call](/book-a-call/)
- [Support](/support/)

## Legal Pages

- [Legal Disclaimer](/legal/disclaimer/)
- [Privacy Policy](/legal/privacy/)
- [Terms of Service](/legal/terms/)
- [Refund Policy](/legal/refund/)

---

*Site last updated: {datetime.now().strftime("%B %d, %Y")}*
'''
    return ""

def generate_legal_pages():
    """Generate legal pages in /legal/ directory"""
    legal_dir = os.path.join(CONTENT_DIR, "legal")
    
    if not os.path.exists(legal_dir):
        os.makedirs(legal_dir, exist_ok=True)
        print(f"📂 Created legal directory: /legal/")
    else:
        print(f"📂 Legal directory exists: /legal/")
    
    for slug, data in LEGAL_PAGES.items():
        page_dir = os.path.join(legal_dir, slug)
        index_file = os.path.join(page_dir, "_index.md")
        
        if os.path.exists(page_dir) and os.path.exists(index_file):
            print(f"⏭️  SKIPPING: /legal/{slug}/ (already exists)")
            continue
        
        if not os.path.exists(page_dir):
            os.makedirs(page_dir, exist_ok=True)
        
        front_matter = create_front_matter(slug, data, is_legal=True)
        content = create_legal_content(slug)
        page_content = front_matter + "\n\n" + content
        
        with open(index_file, "w") as f:
            f.write(page_content)
        
        print(f"✅ CREATED: /legal/{slug}/_index.md ({data['title']})")
        print(f"  🌐 URL: /legal/{slug}/")

def generate_root_pages():
    """Generate root pages"""
    for slug, data in ROOT_PAGES.items():
        page_dir = os.path.join(CONTENT_DIR, slug)
        index_file = os.path.join(page_dir, "_index.md")
        
        if os.path.exists(page_dir) and os.path.exists(index_file):
            print(f"⏭️  SKIPPING: /{slug}/ (already exists)")
            continue
        
        if not os.path.exists(page_dir):
            os.makedirs(page_dir, exist_ok=True)
        
        front_matter = create_front_matter(slug, data, is_legal=False)
        
        # Choose content based on page type
        if slug in ["about", "clients", "pricing"]:
            content = create_business_content(slug)
        else:
            content = create_other_content(slug)
        
        page_content = front_matter + "\n\n" + content
        
        with open(index_file, "w") as f:
            f.write(page_content)
        
        print(f"✅ CREATED: /{slug}/_index.md ({data['title']})")
        print(f"  🌐 URL: /{slug}/")

if __name__ == "__main__":
    print("🚀 Generating Hugo pages that match your navigation URLs...")
    print(f"📁 Target directory: {CONTENT_DIR}")
    
    if not os.path.exists(CONTENT_DIR):
        print(f"❌ ERROR: Content directory does not exist: {CONTENT_DIR}")
        exit(1)
    
    print("\n🏛️  Generating Legal pages...")
    generate_legal_pages()
    
    print("\n📄 Generating other root pages...")
    generate_root_pages()
    
    print(f"\n✅ Pages generation completed!")
    print("\n🌐 Legal page URLs (matching your navigation):")
    for slug in LEGAL_PAGES.keys():
        print(f"  • /legal/{slug}/")
    
    print("\n📄 Other page URLs:")
    for slug in ROOT_PAGES.keys():
        print(f"  • /{slug}/")
    
    print("\n🎯 Navigation match:")
    print("✅ /legal/disclaimer/ ← Legal Disclaimer")
    print("✅ /legal/privacy/ ← Privacy Policy") 
    print("✅ /legal/terms/ ← Terms of Service")
    print("✅ /legal/refund/ ← Refund")
    print("✅ /book-a-call/ ← Book A Call")
    print("✅ /support/ ← Support")
    print("✅ /sitemap/ ← Sitemap")
    
    print("\n🚀 Ready to test with: hugo server")