# 🎁 Gift Catalog Website Generator

A Python-based tool that generates a beautiful, responsive website for browsing and selecting holiday gifts from a CSV catalog. Perfect for internal company gift selection systems.

## ✨ Features

- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **🌐 Hebrew Support**: Full RTL (right-to-left) text support with Hebrew interface
- **🖼️ Dynamic Image Gallery**: Supports 1-4 images per product with interactive thumbnails
- **🎨 Modern UI**: Beautiful gradient backgrounds, smooth animations, and professional styling
- **📊 CSV Data Source**: Easy to update product catalog using CSV files
- **🔗 Seller Links**: Direct links to product pages on external websites
- **📱 Modal Image Viewer**: Click images to view them enlarged
- **⚡ Fast Generation**: Generates complete website in seconds

## 📁 Project Structure

```
galtex/
├── generate_gift_website.py    # Main Python script
├── gifts-catalog.csv           # Product catalog data
├── gift-card-template.html     # Original template file
├── gift_website/               # Generated website (created after running script)
│   ├── index.html             # Main catalog page
│   ├── gift_1.html            # Individual product pages
│   ├── gift_2.html
│   └── gift_3.html
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required (uses only standard library)

### Installation

1. **Clone or download the project**:
   ```bash
   git clone <your-repository-url>
   cd galtex
   ```

2. **Prepare your catalog data**:
   - Edit `gifts-catalog.csv` with your product information
   - Or create a new CSV file with the same structure

3. **Generate the website**:
   ```bash
   python3 generate_gift_website.py
   ```

4. **View the website**:
   - Open `gift_website/index.html` in your web browser
   - Or serve it using a local web server

## 📊 CSV Format

The CSV file should have the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `gift_id` | Unique product identifier | `1` |
| `gift_name` | Product name (Hebrew) | `שעון חכם מתקדם` |
| `gift_subtitle` | Product subtitle (Hebrew) | `חוויית טכנולוגיה מתקדמת` |
| `description` | Product description (Hebrew) | `שעון חכם עם מעקב בריאות...` |
| `price` | Price in Israeli Shekels | `₪1299.99` |
| `availability` | Stock status (Hebrew) | `במלאי` |
| `seller_link` | Link to product page | `https://example-store.com/product` |
| `photo1` | Main product image URL | `https://images.unsplash.com/...` |
| `photo2` | Additional image URL (optional) | `https://images.unsplash.com/...` |
| `photo3` | Additional image URL (optional) | `https://images.unsplash.com/...` |
| `photo4` | Additional image URL (optional) | `https://images.unsplash.com/...` |

### Example CSV Entry

```csv
1,שעון חכם מתקדם,חוויית טכנולוגיה מתקדמת,"שעון חכם עם מעקב בריאות מתקדם, GPS מובנה, וסוללה של 7 ימים.",₪1299.99,במלאי,https://example-store.com/smartwatch,https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400&h=200&fit=crop,https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=150&h=80&fit=crop,https://images.unsplash.com/photo-1544117519-31a4b719223d?w=150&h=80&fit=crop,,
```

## 🎨 Website Features

### Catalog Page (`index.html`)
- **Grid Layout**: Responsive grid showing all products
- **Product Cards**: Each card shows image, title, description, price, and availability
- **Hover Effects**: Cards lift up on hover with enhanced shadows
- **Click Navigation**: Click any card to view product details

### Product Pages (`gift_X.html`)
- **Detailed View**: Full product information with complete description
- **Image Gallery**: 
  - Main featured image
  - 1-4 thumbnail images below
  - Click thumbnails to replace main image
  - Click main image to view in modal
- **Interactive Elements**:
  - Active thumbnail highlighting
  - Modal image viewer
  - Back to catalog button
  - Direct link to seller website

### Responsive Design
- **Desktop**: Full-featured layout with optimal spacing
- **Tablet**: Adjusted grid and image sizes
- **Mobile**: Single-column layout with compact design

## 🔧 Customization

### Styling
The website uses CSS with:
- **Color Scheme**: Purple gradients with red-orange accents
- **Typography**: Segoe UI font family
- **Animations**: Smooth transitions and entrance effects
- **Shadows**: Layered shadows for depth

### Adding Products
1. Add new rows to `gifts-catalog.csv`
2. Run `python3 generate_gift_website.py`
3. New product pages will be automatically generated

### Modifying the Template
1. Edit the HTML generation functions in `generate_gift_website.py`
2. Update CSS styles within the script
3. Regenerate the website to see changes

## 🌐 Deployment

### Local Development
```bash
# Generate website
python3 generate_gift_website.py

# Serve locally (optional)
python3 -m http.server 8000
# Then visit http://localhost:8000/gift_website/
```

### Web Hosting
1. Upload the `gift_website` folder to your web server
2. Ensure the server supports UTF-8 encoding for Hebrew text
3. The website is completely self-contained (no external dependencies)

### GitHub Pages
1. Push your repository to GitHub
2. Enable GitHub Pages in repository settings
3. Set the source to the `gift_website` folder
4. Your website will be available at `https://username.github.io/repository-name/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:
1. Check the CSV format matches the expected structure
2. Ensure all image URLs are accessible
3. Verify Python 3.6+ is installed
4. Check that the `gifts-catalog.csv` file exists in the project directory

## 🔄 Version History

- **v1.0.0**: Initial release with catalog and product pages
- **v1.1.0**: Added responsive design and Hebrew RTL support
- **v1.2.0**: Enhanced image gallery with modal viewer
- **v1.3.0**: Added flexible image layout (1-4 images per product)

---

**Made with ❤️ for easy gift selection** 