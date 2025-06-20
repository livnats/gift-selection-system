#!/usr/bin/env python3
"""
Backend service for gift selection tracking
Receives selections from frontend and stores them for aggregation
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# File to store all selections
SELECTIONS_FILE = "gift_selections_backend.json"

def load_selections():
    """Load existing selections from file"""
    if os.path.exists(SELECTIONS_FILE):
        try:
            with open(SELECTIONS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_selections(selections):
    """Save selections to file"""
    with open(SELECTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(selections, f, ensure_ascii=False, indent=2)

@app.route('/api/select-gift', methods=['POST'])
def select_gift():
    """Receive gift selection from frontend"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['giftId', 'giftName', 'giftPrice', 'employeeId']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Load existing selections
        selections = load_selections()
        
        # Check if employee already has a selection
        employee_id = data['employeeId']
        existing_selection_index = None
        
        for i, selection in enumerate(selections):
            if selection.get('employeeId') == employee_id:
                existing_selection_index = i
                break
        
        # Add timestamp and ID
        selection_data = {
            **data,
            'receivedAt': datetime.now().isoformat(),
            'id': f"selection_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
        }
        
        if existing_selection_index is not None:
            # Update existing selection
            old_gift = selections[existing_selection_index].get('giftName', 'Unknown')
            selections[existing_selection_index] = selection_data
            print(f"✅ Updated selection for {employee_id}: {old_gift} → {selection_data['giftName']}")
            action = 'updated'
        else:
            # Add new selection
            selections.append(selection_data)
            print(f"✅ New selection received: {employee_id} → {selection_data['giftName']}")
            action = 'created'
        
        # Save back to file
        save_selections(selections)
        
        return jsonify({
            'success': True,
            'message': f'Gift selection {action} successfully',
            'selectionId': selection_data['id'],
            'action': action
        })
        
    except Exception as e:
        print(f"❌ Error saving selection: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/selections', methods=['GET'])
def get_selections():
    """Get all selections (for admin/aggregation)"""
    try:
        selections = load_selections()
        return jsonify({
            'success': True,
            'selections': selections,
            'total': len(selections)
        })
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/aggregate', methods=['GET'])
def get_aggregate():
    """Get aggregated statistics"""
    try:
        selections = load_selections()
        
        # Count selections per gift
        gift_counts = {}
        employee_gifts = {}
        
        for selection in selections:
            gift_id = selection['giftId']
            gift_name = selection['giftName']
            employee_id = selection['employeeId']
            
            # Count gifts
            if gift_id not in gift_counts:
                gift_counts[gift_id] = {
                    'giftName': gift_name,
                    'giftPrice': selection['giftPrice'],
                    'count': 0,
                    'employees': []
                }
            gift_counts[gift_id]['count'] += 1
            gift_counts[gift_id]['employees'].append(employee_id)
            
            # Track employee selections
            employee_gifts[employee_id] = {
                'giftId': gift_id,
                'giftName': gift_name,
                'giftPrice': selection['giftPrice'],
                'selectedAt': selection.get('selectionTime', selection.get('receivedAt'))
            }
        
        return jsonify({
            'success': True,
            'totalSelections': len(selections),
            'uniqueEmployees': len(employee_gifts),
            'giftCounts': gift_counts,
            'employeeSelections': employee_gifts,
            'selections': selections
        })
        
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    print("🎁 Gift Selection Backend Service")
    print("=" * 40)
    print("Starting server on http://localhost:5000")
    print("Available endpoints:")
    print("  POST /api/select-gift - Save gift selection")
    print("  GET  /api/selections  - Get all selections")
    print("  GET  /api/aggregate   - Get aggregated statistics")
    print("  GET  /api/health      - Health check")
    print()
    
    app.run(host='0.0.0.0', port=5000, debug=True) 