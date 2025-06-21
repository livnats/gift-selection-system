#!/usr/bin/env python3
"""
Generate local versions of gift pages with correct backend URL
"""

import os
import re
import json

def update_gift_page_for_local(file_path):
    """Update a gift page to use localhost:5000 for API calls"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace relative API URLs with localhost:5000
    content = re.sub(
        r"fetch\('/api/",
        "fetch('http://localhost:5000/api/",
        content
    )
    
    # Fix giftName strings that might have escaping issues
    # Look for patterns like giftName: 'string with apostrophes'
    content = re.sub(
        r"giftName:\s*'([^']*(?:'[^']*)*)'",
        lambda m: f"giftName: {json.dumps(m.group(1))}",
        content
    )
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated {file_path} for local development")

def main():
    """Generate local versions of all gift pages"""
    print("🔧 Generating local versions of gift pages...")
    
    gift_files = [
        'gift_website/gift_1.html',
        'gift_website/gift_2.html', 
        'gift_website/gift_3.html',
        'gift_website/gift_4.html',
        'gift_website/gift_5.html',
        'gift_website/admin.html'
    ]
    
    for file_path in gift_files:
        if os.path.exists(file_path):
            update_gift_page_for_local(file_path)
        else:
            print(f"⚠️  File not found: {file_path}")
    
    print("🎉 Local development pages ready!")

if __name__ == '__main__':
    main() 