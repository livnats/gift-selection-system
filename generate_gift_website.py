#!/usr/bin/env python3
"""
Gift Catalog Website Generator
Creates a complete HTML website from a CSV catalog file
"""

import csv
import os

class GiftWebsiteGenerator:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.gifts = []
        self.load_gifts()
    
    def load_gifts(self):
        """Load gifts from CSV file"""
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Clean up empty photo fields
                    photos = []
                    for i in range(1, 5):  # photo1 to photo4
                        photo_key = f'photo{i}'
                        if photo_key in row and row[photo_key].strip():
                            photos.append(row[photo_key].strip())
                    
                    gift = {
                        'id': row['gift_id'],
                        'name': row['gift_name'],
                        'subtitle': row['gift_subtitle'],
                        'description': row['description'],
                        'price': row['price'],
                        'availability': row['availability'],
                        'seller_link': row['seller_link'],
                        'photos': photos
                    }
                    self.gifts.append(gift)
            print(f"Loaded {len(self.gifts)} gifts from {self.csv_file}")
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            raise

    def generate_website(self, output_dir="gift_website"):
        """Generate the complete website"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate catalog page
        catalog_html = self.generate_catalog_page()
        with open(os.path.join(output_dir, "index.html"), 'w', encoding='utf-8') as f:
            f.write(catalog_html)
        
        # Generate individual gift pages
        for gift in self.gifts:
            gift_html = self.generate_gift_page(gift)
            filename = f"gift_{gift['id']}.html"
            with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                f.write(gift_html)
        
        print(f"Website generated successfully in '{output_dir}' directory!")
        print("Generated files:")
        print("  - index.html (catalog page)")
        for gift in self.gifts:
            print(f"  - gift_{gift['id']}.html ({gift['name']})")
        print("\nOpen 'index.html' in your browser to view the website.")

    def generate_catalog_page(self):
        """Generate the main catalog page HTML"""
        html = """<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>קטלוג מתנות חג - בחירת מתנות לעובדים</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; }
        .header { text-align: center; color: white; margin-bottom: 40px; padding: 20px; }
        .header h1 { font-size: 2.5rem; margin-bottom: 10px; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3); }
        .header p { font-size: 1.2rem; opacity: 0.9; }
        .catalog-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto; padding: 20px; }
        .catalog-item { background: white; border-radius: 20px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; cursor: pointer; position: relative; }
        .catalog-item:hover { transform: translateY(-10px); box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15); }
        .catalog-item-header { background: linear-gradient(135deg, #ff6b6b, #ee5a24); color: white; padding: 20px; text-align: center; position: relative; }
        .catalog-item-header::before { content: '🎁'; font-size: 1.5rem; position: absolute; top: 10px; right: 15px; opacity: 0.8; }
        .catalog-item-title { font-size: 1.3rem; font-weight: 700; margin-bottom: 5px; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); }
        .catalog-item-subtitle { font-size: 0.9rem; opacity: 0.9; font-weight: 300; }
        .catalog-item-content { padding: 20px; }
        .catalog-item-image { width: 100%; height: 200px; object-fit: cover; border-radius: 15px; margin-bottom: 15px; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); }
        .catalog-item-description { color: #555; line-height: 1.5; margin-bottom: 15px; font-size: 0.9rem; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
        .catalog-item-footer { display: flex; justify-content: space-between; align-items: center; margin-top: 15px; }
        .catalog-item-price { background: linear-gradient(135deg, #4ecdc4, #44a08d); color: white; padding: 8px 15px; border-radius: 20px; font-weight: 700; font-size: 1rem; }
        .catalog-item-availability { background: #2ecc71; color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.8rem; font-weight: 600; }
        .catalog-item-availability.out-of-stock { background: #e74c3c; }
        .view-details-btn { display: inline-block; background: linear-gradient(135deg, #667eea, #764ba2); color: white; text-decoration: none; padding: 10px 20px; border-radius: 25px; font-weight: 600; text-align: center; transition: all 0.3s ease; margin-top: 15px; width: 100%; }
        .view-details-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4); }
        @media (max-width: 768px) { .catalog-grid { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; padding: 10px; } .header h1 { font-size: 2rem; } .header p { font-size: 1rem; } }
        @media (max-width: 480px) { body { padding: 10px; } .catalog-grid { grid-template-columns: 1fr; gap: 15px; } .header h1 { font-size: 1.8rem; } }
        @keyframes slideInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
        .catalog-item { animation: slideInUp 0.6s ease-out; }
        .catalog-item:nth-child(1) { animation-delay: 0.1s; }
        .catalog-item:nth-child(2) { animation-delay: 0.2s; }
        .catalog-item:nth-child(3) { animation-delay: 0.3s; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎁 קטלוג מתנות חג</h1>
        <p>בחרו מתנה מושלמת לעובדים שלכם</p>
    </div>
    <div class="catalog-grid">"""
        
        for gift in self.gifts:
            # Get the first photo for the catalog preview
            preview_image = gift['photos'][0] if gift['photos'] else "https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0?w=400&h=200&fit=crop"
            
            # Truncate description for catalog view
            description = gift['description'][:150] + "..." if len(gift['description']) > 150 else gift['description']
            
            # Determine availability class
            availability_class = "out-of-stock" if "לא במלאי" in gift['availability'] else ""
            
            html += f"""
        <div class="catalog-item" onclick="window.location.href='gift_{gift['id']}.html'">
            <div class="catalog-item-header">
                <h2 class="catalog-item-title">{gift['name']}</h2>
                <p class="catalog-item-subtitle">{gift['subtitle']}</p>
            </div>
            <div class="catalog-item-content">
                <img src="{preview_image}" alt="{gift['name']}" class="catalog-item-image">
                <p class="catalog-item-description">{description}</p>
                <div class="catalog-item-footer">
                    <div class="catalog-item-price">{gift['price']}</div>
                    <div class="catalog-item-availability {availability_class}">{gift['availability']}</div>
                </div>
                <a href="gift_{gift['id']}.html" class="view-details-btn">צפה בפרטים מלאים</a>
            </div>
        </div>"""
        
        html += """
    </div>
    <script>
        document.querySelectorAll('.catalog-item').forEach(item => {
            item.addEventListener('click', function(e) {
                if (e.target.tagName !== 'A') {
                    const link = this.querySelector('.view-details-btn');
                    if (link) {
                        window.location.href = link.href;
                    }
                }
            });
        });
    </script>
</body>
</html>"""
        
        return html

    def generate_gift_page(self, gift):
        """Generate individual gift page HTML"""
        
        # Generate photo gallery HTML
        photo_gallery_html = ""
        if gift['photos']:
            # Main image
            main_image = gift['photos'][0]
            photo_gallery_html += f"""
                <img src="{main_image}" 
                     alt="{gift['name']}" 
                     class="main-image" 
                     id="mainImage"
                     onclick="openModal(this.src)">"""
            
            # Thumbnail gallery
            photo_gallery_html += """
                <div class="image-gallery" id="imageGallery">"""
            
            for i, photo in enumerate(gift['photos']):
                active_class = "active" if i == 0 else ""
                photo_gallery_html += f"""
                    <img src="{photo}" 
                         alt="תצוגת {gift['name']} {i+1}" 
                         class="gallery-image {active_class}" 
                         onclick="replaceMainImage(this.src, this.alt, this)">"""
            
            photo_gallery_html += """
                </div>"""
        
        # Determine availability class
        availability_class = "out-of-stock" if "לא במלאי" in gift['availability'] else ""
        
        html = f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{gift['name']} - קטלוג מתנות חג</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 20px; display: flex; justify-content: center; align-items: center; }}
        .gift-card {{ background: white; border-radius: 20px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1); overflow: hidden; max-width: 400px; width: 100%; transition: transform 0.3s ease, box-shadow 0.3s ease; position: relative; }}
        .gift-card:hover {{ transform: translateY(-10px); box-shadow: 0 30px 60px rgba(0, 0, 0, 0.15); }}
        .gift-header {{ background: linear-gradient(135deg, #ff6b6b, #ee5a24); color: white; padding: 25px; text-align: center; position: relative; }}
        .gift-header::before {{ content: '🎁'; font-size: 2rem; position: absolute; top: 10px; right: 15px; opacity: 0.8; }}
        .gift-title {{ font-size: 1.5rem; font-weight: 700; margin-bottom: 5px; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); }}
        .gift-subtitle {{ font-size: 0.9rem; opacity: 0.9; font-weight: 300; }}
        .gift-content {{ padding: 25px; }}
        .gift-description {{ color: #555; line-height: 1.6; margin-bottom: 20px; font-size: 0.95rem; }}
        .gift-images {{ margin-bottom: 20px; }}
        .image-gallery {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 10px; margin-bottom: 15px; max-width: 100%; }}
        .image-gallery.one-image {{ grid-template-columns: 1fr; max-width: 200px; margin: 0 auto 15px auto; }}
        .image-gallery.two-images {{ grid-template-columns: repeat(2, 1fr); max-width: 200px; margin: 0 auto 15px auto; }}
        .image-gallery.three-images {{ grid-template-columns: repeat(3, 1fr); }}
        .image-gallery.four-images {{ grid-template-columns: repeat(4, 1fr); }}
        .gallery-image {{ width: 100%; height: 80px; object-fit: cover; border-radius: 10px; cursor: pointer; transition: transform 0.3s ease, filter 0.3s ease; border: 2px solid transparent; }}
        .gallery-image:hover {{ transform: scale(1.05); filter: brightness(1.1); border-color: #ff6b6b; }}
        .gallery-image.active {{ border-color: #ff6b6b; box-shadow: 0 0 10px rgba(255, 107, 107, 0.3); }}
        .main-image {{ width: 100%; height: 200px; object-fit: cover; border-radius: 15px; margin-bottom: 15px; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); }}
        .seller-link {{ display: inline-block; background: linear-gradient(135deg, #4ecdc4, #44a08d); color: white; text-decoration: none; padding: 12px 25px; border-radius: 25px; font-weight: 600; text-align: center; transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(78, 205, 196, 0.3); }}
        .seller-link:hover {{ transform: translateY(-2px); box-shadow: 0 8px 25px rgba(78, 205, 196, 0.4); background: linear-gradient(135deg, #44a08d, #4ecdc4); }}
        .price-tag {{ position: absolute; top: 15px; left: 15px; background: rgba(255, 255, 255, 0.95); color: #ff6b6b; padding: 8px 15px; border-radius: 20px; font-weight: 700; font-size: 0.9rem; box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1); }}
        .availability {{ position: absolute; top: 15px; right: 15px; background: #2ecc71; color: white; padding: 5px 12px; border-radius: 15px; font-size: 0.8rem; font-weight: 600; }}
        .availability.out-of-stock {{ background: #e74c3c; }}
        .back-button {{ position: fixed; top: 20px; left: 20px; background: rgba(255, 255, 255, 0.9); color: #667eea; text-decoration: none; padding: 10px 20px; border-radius: 25px; font-weight: 600; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1); transition: all 0.3s ease; z-index: 1000; }}
        .back-button:hover {{ background: white; transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15); }}
        .modal {{ display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.9); backdrop-filter: blur(5px); }}
        .modal-content {{ margin: auto; display: block; max-width: 90%; max-height: 90%; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); border-radius: 10px; }}
        .close {{ position: absolute; top: 15px; right: 35px; color: #f1f1f1; font-size: 40px; font-weight: bold; cursor: pointer; z-index: 1001; }}
        .close:hover {{ color: #bbb; }}
        @media (max-width: 768px) {{ .gift-card {{ max-width: 350px; margin: 10px; }} .gift-header {{ padding: 20px; }} .gift-title {{ font-size: 1.3rem; }} .gift-content {{ padding: 20px; }} .image-gallery {{ grid-template-columns: repeat(auto-fit, minmax(70px, 1fr)); gap: 8px; }} .image-gallery.one-image, .image-gallery.two-images {{ max-width: 180px; }} .gallery-image {{ height: 70px; }} .main-image {{ height: 180px; }} .back-button {{ top: 10px; left: 10px; padding: 8px 15px; font-size: 0.9rem; }} }}
        @media (max-width: 480px) {{ body {{ padding: 10px; }} .gift-card {{ max-width: 100%; border-radius: 15px; }} .gift-header {{ padding: 15px; }} .gift-title {{ font-size: 1.2rem; }} .gift-content {{ padding: 15px; }} .image-gallery {{ grid-template-columns: repeat(auto-fit, minmax(60px, 1fr)); gap: 5px; }} .image-gallery.one-image, .image-gallery.two-images {{ max-width: 160px; }} .gallery-image {{ height: 60px; }} .main-image {{ height: 160px; }} .seller-link {{ padding: 10px 20px; font-size: 0.9rem; }} }}
        @keyframes slideInUp {{ from {{ opacity: 0; transform: translateY(30px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        .gift-card {{ animation: slideInUp 0.6s ease-out; }}
    </style>
</head>
<body>
    <a href="index.html" class="back-button">← חזרה לקטלוג</a>
    <div class="gift-card">
        <div class="price-tag">{gift['price']}</div>
        <div class="availability {availability_class}">{gift['availability']}</div>
        <div class="gift-header">
            <h2 class="gift-title">{gift['name']}</h2>
            <p class="gift-subtitle">{gift['subtitle']}</p>
        </div>
        <div class="gift-content">
            <p class="gift-description">{gift['description']}</p>
            <div class="gift-images">
                {photo_gallery_html}
            </div>
            <a href="{gift['seller_link']}" class="seller-link" target="_blank" rel="noopener noreferrer">צפה באתר החנות</a>
        </div>
    </div>
    <div id="imageModal" class="modal">
        <span class="close" onclick="closeModal()">&times;</span>
        <img class="modal-content" id="modalImage">
    </div>
    <script>
        function openModal(src) {{ const modal = document.getElementById('imageModal'); const modalImg = document.getElementById('modalImage'); modal.style.display = 'block'; modalImg.src = src; }}
        function closeModal() {{ document.getElementById('imageModal').style.display = 'none'; }}
        document.getElementById('imageModal').addEventListener('click', function(e) {{ if (e.target === this) {{ closeModal(); }} }});
        document.addEventListener('keydown', function(e) {{ if (e.key === 'Escape') {{ closeModal(); }} }});
        function updateImageLayout() {{ const gallery = document.getElementById('imageGallery'); if (!gallery) return; const images = gallery.querySelectorAll('.gallery-image'); const visibleImages = Array.from(images).filter(img => img.style.display !== 'none' && img.src && img.src.trim() !== ''); gallery.classList.remove('one-image', 'two-images', 'three-images', 'four-images'); if (visibleImages.length === 1) {{ gallery.classList.add('one-image'); }} else if (visibleImages.length === 2) {{ gallery.classList.add('two-images'); }} else if (visibleImages.length === 3) {{ gallery.classList.add('three-images'); }} else if (visibleImages.length === 4) {{ gallery.classList.add('four-images'); }} }}
        document.addEventListener('DOMContentLoaded', function() {{ updateImageLayout(); }});
        function replaceMainImage(src, alt, element) {{ const mainImage = document.getElementById('mainImage'); mainImage.src = src; mainImage.alt = alt; const galleryImages = document.querySelectorAll('.gallery-image'); galleryImages.forEach(img => {{ if (img === element) {{ img.classList.add('active'); }} else {{ img.classList.remove('active'); }} }}); }}
    </script>
</body>
</html>"""
        
        return html

def main():
    """Main function"""
    csv_file = "gifts-catalog.csv"
    
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found!")
        return
    
    try:
        generator = GiftWebsiteGenerator(csv_file)
        generator.generate_website()
    except Exception as e:
        print(f"Error generating website: {e}")

if __name__ == "__main__":
    main()
