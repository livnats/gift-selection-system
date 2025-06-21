# Local Development Guide

This guide explains how to run the Gift Selection Website locally for development.

## 🚀 Quick Start

### Option 1: Using the automated script (Recommended)
```bash
./run_local.sh
```

This script will:
- Create/activate virtual environment
- Install dependencies
- Generate the website
- Generate local development pages (with correct API URLs)
- Start both backend and frontend servers

### Option 2: Manual setup

1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate website:**
   ```bash
   python3 generate_gift_website.py
   ```

4. **Generate local development pages:**
   ```bash
   python3 generate_local_pages.py
   ```

5. **Start backend server:**
   ```bash
   python3 backend.py
   ```

6. **Start frontend server (in another terminal):**
   ```bash
   cd gift_website
   python3 -m http.server 8000
   ```

## 🌐 Access URLs

- **Main Website**: http://localhost:8000
- **Admin Dashboard**: http://localhost:8000/admin.html
- **Backend API**: http://localhost:5000

## 📁 Project Structure

```
galtex/
├── backend.py                 # Flask backend API
├── generate_gift_website.py   # Website generator
├── generate_local_pages.py    # Local development page generator
├── gifts-catalog.csv         # Gift catalog data
├── requirements.txt          # Python dependencies
├── gift_website/            # Generated website files
│   ├── cover.html           # Employee ID entry
│   ├── admin.html           # Admin dashboard
│   ├── index.html           # Gift catalog
│   ├── gift_1.html          # Individual gift pages
│   ├── gift_2.html
│   ├── gift_3.html
│   ├── gift_4.html
│   ├── gift_5.html
│   └── selection.html       # Selection tracking
└── venv/                    # Python virtual environment
```

## 🔧 Development Workflow

1. **Edit gift catalog**: Modify `gifts-catalog.csv`
2. **Regenerate website**: Run `python3 generate_gift_website.py`
3. **Regenerate local pages**: Run `python3 generate_local_pages.py`
4. **Test changes**: Refresh browser at http://localhost:8000

## 🛠️ API Endpoints

- `GET /api/health` - Health check
- `POST /api/select-gift` - Save gift selection
- `GET /api/selections` - Get all selections
- `GET /api/aggregate` - Get aggregated statistics
- `POST /api/reset-selections` - Reset all selections

## 🔄 Local vs Production

The website uses different API URLs for local development vs production:

- **Local Development**: `http://localhost:5000/api/...`
- **Production**: `/api/...` (relative URLs)

The `generate_local_pages.py` script automatically updates the pages for local development.

## 🐛 Troubleshooting

### Port already in use
If you get "Address already in use" errors:
```bash
# Find processes using the ports
lsof -ti:5000  # Backend port
lsof -ti:8000  # Frontend port

# Kill the processes
kill -9 <PID>
```

### Virtual environment issues
```bash
# Remove and recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Website not updating
Make sure to regenerate both the website and local pages:
```bash
python3 generate_gift_website.py
python3 generate_local_pages.py
```

### Gift selection not working
1. Make sure the backend is running on port 5000
2. Make sure you've run `generate_local_pages.py` to update API URLs
3. Check browser console for errors

## 📝 Notes

- The backend stores data in `gift_selections_backend.json` (ignored by git)
- Local development pages use absolute URLs to localhost:5000
- Production pages use relative URLs for the deployed server
- All API calls are made to the backend server running on port 5000 