# 🎁 Gift Catalog Website Generator

A complete gift catalog website generator with user authentication and gift selection tracking. Creates a responsive, modern website from a CSV catalog file with Hebrew text support.

## ✨ Features

### 🔐 User Authentication System
- **Login Page**: Users must provide email, full name, and address to access the catalog
- **Session Management**: Automatic login state management using localStorage
- **User Validation**: Email format validation and required field checking
- **Logout Functionality**: Secure logout with session cleanup

### 🎯 Gift Selection Tracking
- **Individual Gift Pages**: Detailed view of each gift with photo galleries
- **Selection Button**: Users can select their preferred gift
- **Selection Confirmation**: Success messages and automatic redirection
- **Selection History**: Users can view their current selection
- **Change Selection**: Option to modify gift choice

### 📊 Data Export
- **CSV Export**: Export gift selections to CSV file for tracking
- **Complete User Data**: Captures user details, gift choice, and timestamps
- **Sample Export Script**: Ready-to-use Python script for data export

### 🎨 Modern UI/UX
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Hebrew RTL Support**: Full right-to-left text support
- **Interactive Elements**: Hover effects, animations, and smooth transitions
- **Photo Galleries**: Multiple images per gift with thumbnail navigation
- **Modal Image Viewer**: Click to enlarge images

## 📁 Project Structure

```
galtex/
├── login.html                    # User authentication page
├── generate_gift_website.py      # Main website generator
├── export_selections.py          # CSV export utility
├── gifts-catalog.csv            # Gift catalog data
├── gift_selections.csv          # Generated selections (sample)
├── gift_website/                # Generated website files
│   ├── login.html              # Authentication page
│   ├── index.html              # Main catalog page
│   ├── gift_1.html             # Individual gift pages
│   ├── gift_2.html
│   ├── gift_3.html
│   └── selection.html          # Selection tracking page
├── .gitignore                   # Git ignore file
└── README.md                   # This file
```

## 🚀 Quick Start

### 1. Setup
```bash
# Clone or download the project
cd galtex

# Make sure you have Python 3 installed
python3 --version
```

### 2. Prepare Your Catalog
Edit `gifts-catalog.csv` with your gift data:
```csv
gift_id,gift_name,gift_subtitle,description,price,availability,seller_link,photo1,photo2,photo3,photo4
GIFT001,שם המתנה,כותרת משנה,תיאור המתנה,₪299,במלאי,https://example.com,image1.jpg,image2.jpg,,
```

### 3. Generate Website
```bash
python3 generate_gift_website.py
```

### 4. Access the Website
1. Open `gift_website/login.html` in your browser
2. Enter user details (email, full name, address)
3. Browse the gift catalog
4. Select your preferred gift
5. View your selection on the tracking page

## 📋 CSV Catalog Format

The `gifts-catalog.csv` file should contain the following columns:

| Column | Description | Required | Example |
|--------|-------------|----------|---------|
| `gift_id` | Unique gift identifier | Yes | `GIFT001` |
| `gift_name` | Gift name in Hebrew | Yes | `שעון חכם מתקדם` |
| `gift_subtitle` | Short description | Yes | `עם מעקב פעילות` |
| `description` | Detailed description | Yes | `שעון חכם עם GPS...` |
| `price` | Price in shekels | Yes | `₪899` |
| `availability` | Stock status | Yes | `במלאי` |
| `seller_link` | Store URL | Yes | `https://store.com` |
| `photo1` | Main image URL | Yes | `https://example.com/img1.jpg` |
| `photo2` | Additional image | No | `https://example.com/img2.jpg` |
| `photo3` | Additional image | No | `https://example.com/img3.jpg` |
| `photo4` | Additional image | No | `https://example.com/img4.jpg` |

## 🔐 User Authentication Flow

1. **Login Page**: Users enter email, full name, and address
2. **Validation**: Email format and required fields are validated
3. **Session Storage**: User data is stored in browser localStorage
4. **Catalog Access**: Authenticated users can browse gifts
5. **Gift Selection**: Users can select and track their choices
6. **Logout**: Users can logout and clear session data

## 📊 Gift Selection Tracking

### Selection Data Captured
- Gift ID and name
- Gift price
- User email and full name
- User address
- Selection timestamp
- Export timestamp

### Exporting Selections
```bash
# Run the export script to see sample data
python3 export_selections.py

# The script creates gift_selections.csv with the structure:
gift_id,gift_name,gift_price,user_email,user_full_name,user_address,selection_time,export_time
```

### Manual Data Export
To export real user selections:
1. Open browser developer tools (F12)
2. Go to Console tab
3. Run: `localStorage.getItem('selectedGift')`
4. Copy the JSON data
5. Use the export script to convert to CSV

## 🎨 Customization

### Styling
- All CSS is embedded in the HTML files
- Modern gradient backgrounds and animations
- Responsive design with mobile-first approach
- Hebrew RTL text support

### Adding Features
- Modify `generate_gift_website.py` to add new features
- Update the gift card template in the script
- Add new pages by extending the generator class

## 🔧 Technical Details

### Technologies Used
- **Python 3**: Website generation and CSV processing
- **HTML5**: Semantic markup with Hebrew RTL support
- **CSS3**: Modern styling with gradients and animations
- **JavaScript**: Interactive features and localStorage management
- **CSV**: Data storage and export format

### Browser Compatibility
- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

### Local Storage Structure
```javascript
// User data
{
  "email": "user@example.com",
  "fullName": "שם מלא",
  "address": "כתובת מלאה",
  "loginTime": "2024-12-15T10:30:00.000Z"
}

// Selected gift
{
  "giftId": "GIFT001",
  "giftName": "שם המתנה",
  "giftPrice": "₪299",
  "userEmail": "user@example.com",
  "userFullName": "שם מלא",
  "userAddress": "כתובת מלאה",
  "selectionTime": "2024-12-15T10:30:00.000Z"
}
```

## 📝 Usage Examples

### Basic Usage
```bash
# Generate website from existing catalog
python3 generate_gift_website.py

# Open login page
open gift_website/login.html
```

### Custom Catalog
```bash
# Edit your catalog file
nano gifts-catalog.csv

# Regenerate website
python3 generate_gift_website.py
```

### Export Selections
```bash
# Create sample export
python3 export_selections.py

# View generated CSV
cat gift_selections.csv
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues or questions:
1. Check the documentation above
2. Review the CSV format requirements
3. Test with the sample data provided
4. Open an issue with detailed information

---

**Happy Gift Selecting! 🎁✨** 