# 🎁 Gift Catalog Website Generator

A complete gift catalog website generator with employee ID tracking and gift selection aggregation. Creates a responsive, modern website from a CSV catalog file with Hebrew text support and backend integration.

## ✨ Features

### 🔐 Employee ID System
- **Cover Page**: Users enter their employee ID to access the catalog
- **Session Management**: Employee ID stored in localStorage for session persistence
- **Backend Integration**: Gift selections sent to backend service for aggregation
- **Admin Dashboard**: Real-time statistics and gift popularity tracking

### 🎯 Gift Selection Tracking
- **Individual Gift Pages**: Detailed view of each gift with photo galleries
- **Selection Button**: Users can select their preferred gift
- **Backend Storage**: Selections automatically sent to backend service
- **Selection History**: Users can view their current selection
- **Change Selection**: Option to modify gift choice

### 📊 Data Aggregation
- **Backend Service**: Flask API for collecting and aggregating selections
- **Real-time Statistics**: Live dashboard showing gift popularity
- **Employee Tracking**: Track which employees selected which gifts
- **JSON Storage**: All data stored in structured JSON format

### 🎨 Modern UI/UX
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Hebrew RTL Support**: Full right-to-left text support
- **Interactive Elements**: Hover effects, animations, and smooth transitions
- **Photo Galleries**: Multiple images per gift with thumbnail navigation
- **Modal Image Viewer**: Click to enlarge images

## 📁 Project Structure

```
galtex/
├── backend.py
├── generate_gift_website.py
├── gifts-catalog.csv
├── requirements.txt
├── gift_website/
├── venv/
├── deployment/
│   ├── local/
│   │   ├── run_local.sh
│   │   └── generate_local_pages.py
│   └── remote/
│       ├── run_remote_build.sh
│       ├── deploy.sh
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       ├── user_data.sh
│       ├── DEPLOYMENT_WORKFLOW.md
│       └── README_TERRAFORM.md
└── README.md
```

## 🚀 Quick Start

### 1. Setup
```bash
# Clone or download the project
cd galtex

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Local Development
```bash
# Run local development environment
./deployment/local/run_local.sh
```

This will:
- Generate local HTML files with localhost URLs
- Start backend server on port 5000
- Start frontend server on port 8000

### 3. Access Local Website
1. Open `http://localhost:8000/cover.html` in your browser
2. Enter employee ID
3. Browse and select gifts
4. View admin dashboard at `http://localhost:8000/admin.html`

## 🚀 Deployment to AWS

### Prerequisites
- AWS account with appropriate permissions
- Terraform installed
- SSH key pair for EC2 access

### Quick Deployment
```bash
# Run the complete build and deploy process
./deployment/remote/run_remote_build.sh
```

This script will:
1. ✅ Generate production HTML files with relative URLs
2. ✅ Verify no localhost references in generated files
3. ✅ Deploy infrastructure using Terraform
4. ✅ Upload application files to AWS EC2
5. ✅ Start backend and nginx services

### Manual Deployment Steps
If you prefer to run steps manually:

```bash
# 1. Generate production files
source venv/bin/activate
python3 generate_gift_website.py

# 2. Verify no localhost references
grep -r "localhost:" gift_website/*.html || echo "✅ No localhost references found"

# 3. Deploy to AWS
./deployment/remote/deploy.sh
```

### Deployment Files
- `deployment/remote/run_remote_build.sh` - Complete build and deploy script
- `deployment/remote/deploy.sh` - AWS deployment script
- `deployment/remote/main.tf` - Terraform infrastructure configuration
- `deployment/remote/user_data.sh` - EC2 instance setup script

### Access Deployed Application
- **Main Website**: `http://[EC2-PUBLIC-IP]/cover.html`
- **Admin Dashboard**: `http://[EC2-PUBLIC-IP]/admin.html`
- **Backend API**: `http://[EC2-PUBLIC-IP]/api/health`

For detailed deployment instructions, see [deployment/remote/README_TERRAFORM.md](deployment/remote/README_TERRAFORM.md).

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

## 🔐 User Flow

1. **Cover Page**: Users enter employee ID
2. **Catalog Access**: Authenticated users can browse gifts
3. **Gift Selection**: Users can select and track their choices
4. **Backend Storage**: Selections sent to backend service
5. **Admin Dashboard**: Real-time aggregation and statistics

## 📊 Backend API

### Endpoints
- `POST /api/select-gift` - Save gift selection
- `GET /api/selections` - Get all selections
- `GET /api/aggregate` - Get aggregated statistics
- `GET /api/health` - Health check

### Data Structure
```json
{
  "giftId": "1",
  "giftName": "שעון חכם מתקדם",
  "giftPrice": "₪1299.99",
  "employeeId": "EMP123",
  "selectionTime": "2024-12-15T10:30:00.000Z",
  "receivedAt": "2024-12-15T10:30:01.000Z",
  "id": "selection_20241215_103001_123456"
}
```

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
- **Python 3**: Website generation and backend service
- **Flask**: Backend API framework
- **HTML5**: Semantic markup with Hebrew RTL support
- **CSS3**: Modern styling with gradients and animations
- **JavaScript**: Interactive features and API communication
- **CSV**: Data storage and export format

### Browser Compatibility
- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

### Local Storage Structure
```javascript
// Employee data
{
  "employeeId": "EMP123"
}

// Selected gift
{
  "giftId": "1",
  "giftName": "שם המתנה",
  "giftPrice": "₪299",
  "employeeId": "EMP123",
  "selectionTime": "2024-12-15T10:30:00.000Z"
}
```

## 📝 Usage Examples

### Basic Usage
```bash
# Start backend
source venv/bin/activate
python3 backend.py

# In another terminal, serve website
cd gift_website
python3 -m http.server 8001

# Open in browser
open http://localhost:8001/cover.html
```

### Custom Catalog
```bash
# Edit your catalog file
nano gifts-catalog.csv

# Regenerate website
python3 generate_gift_website.py
```

### View Aggregated Data
```bash
# API endpoint
curl http://localhost:5000/api/aggregate

# Or use admin dashboard
open http://localhost:8001/admin.html
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