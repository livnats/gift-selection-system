#!/usr/bin/env python3
"""
Gift Selection Exporter
Exports gift selections from the website to a CSV file
"""

import csv
import json
import os
from datetime import datetime

def export_selections_to_csv(selections_data, output_file="gift_selections.csv"):
    """
    Export gift selections to CSV file
    
    Args:
        selections_data (list): List of selection dictionaries
        output_file (str): Output CSV filename
    """
    
    # Define CSV headers
    headers = [
        'gift_id',
        'gift_name', 
        'gift_price',
        'user_email',
        'user_full_name',
        'user_address',
        'selection_time',
        'export_time'
    ]
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            
            # Write header
            writer.writeheader()
            
            # Write data
            for selection in selections_data:
                writer.writerow(selection)
        
        print(f"✅ Successfully exported {len(selections_data)} selections to '{output_file}'")
        return True
        
    except Exception as e:
        print(f"❌ Error exporting to CSV: {e}")
        return False

def create_sample_selections():
    """
    Create sample selection data for testing
    """
    return [
        {
            'gift_id': 'GIFT001',
            'gift_name': 'סט כלי מטבח מקצועי',
            'gift_price': '₪299',
            'user_email': 'user1@example.com',
            'user_full_name': 'ישראל ישראלי',
            'user_address': 'רחוב הרצל 123, תל אביב, 12345',
            'selection_time': '2024-12-15T10:30:00.000Z',
            'export_time': datetime.now().isoformat()
        },
        {
            'gift_id': 'GIFT002', 
            'gift_name': 'שעון חכם מתקדם',
            'gift_price': '₪899',
            'user_email': 'user2@example.com',
            'user_full_name': 'שרה כהן',
            'user_address': 'רחוב ויצמן 456, ירושלים, 67890',
            'selection_time': '2024-12-15T14:15:00.000Z',
            'export_time': datetime.now().isoformat()
        },
        {
            'gift_id': 'GIFT003',
            'gift_name': 'אוזניות אלחוטיות איכותיות',
            'gift_price': '₪499',
            'user_email': 'user3@example.com', 
            'user_full_name': 'דוד לוי',
            'user_address': 'רחוב בן גוריון 789, חיפה, 11111',
            'selection_time': '2024-12-15T16:45:00.000Z',
            'export_time': datetime.now().isoformat()
        }
    ]

def main():
    """Main function to demonstrate CSV export"""
    
    print("🎁 Gift Selection Exporter")
    print("=" * 40)
    
    # Create sample data
    selections = create_sample_selections()
    
    # Export to CSV
    success = export_selections_to_csv(selections)
    
    if success:
        print("\n📊 Sample CSV structure created:")
        print("   - gift_id: מזהה המתנה")
        print("   - gift_name: שם המתנה")
        print("   - gift_price: מחיר המתנה")
        print("   - user_email: אימייל המשתמש")
        print("   - user_full_name: שם מלא")
        print("   - user_address: כתובת מלאה")
        print("   - selection_time: זמן הבחירה")
        print("   - export_time: זמן הייצוא")
        
        print("\n💡 To export real selections from the website:")
        print("   1. Open browser developer tools (F12)")
        print("   2. Go to Console tab")
        print("   3. Run: localStorage.getItem('selectedGift')")
        print("   4. Copy the JSON data and use it in this script")
        
        print("\n🔧 Usage in your application:")
        print("   - Call export_selections_to_csv() with your data")
        print("   - Data should be a list of dictionaries with the above fields")
        print("   - CSV will be created in the current directory")

if __name__ == "__main__":
    main() 