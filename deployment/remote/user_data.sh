#!/bin/bash
# User data script for EC2 instance initialization

# Update system
apt-get update
apt-get upgrade -y

# Install required packages
apt-get install -y python3 python3-pip python3-venv nginx git unzip

# Create application directory
mkdir -p /var/www/gift-website
cd /var/www/gift-website

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install flask gunicorn

# Create nginx configuration
cat > /etc/nginx/sites-available/gift-website << 'EOF'
server {
    listen 80;
    server_name _;
    root /var/www/gift-website/gift_website;
    index cover.html;

    # Handle static files
    location / {
        try_files $uri $uri/ =404;
    }

    # Proxy API requests to backend
    location /api/ {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
}
EOF

# Enable the site
ln -sf /etc/nginx/sites-available/gift-website /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default

# Test nginx configuration
nginx -t

# Restart nginx
systemctl restart nginx
systemctl enable nginx

# Create systemd service for the backend
cat > /etc/systemd/system/gift-website.service << 'EOF'
[Unit]
Description=Gift Selection Website Backend
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/gift-website
Environment=PATH=/var/www/gift-website/venv/bin
ExecStart=/var/www/gift-website/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 backend:app
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# Set proper permissions
chown -R www-data:www-data /var/www/gift-website

# Enable and start the service
systemctl enable gift-website.service

# Create a simple health check script
cat > /var/www/gift-website/health_check.sh << 'EOF'
#!/bin/bash
if curl -f http://localhost:5000/api/health > /dev/null 2>&1; then
    echo "Backend is healthy"
    exit 0
else
    echo "Backend is not responding"
    exit 1
fi
EOF

chmod +x /var/www/gift-website/health_check.sh

# Create deployment script
cat > /var/www/gift-website/deploy.sh << 'EOF'
#!/bin/bash
cd /var/www/gift-website

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
pip install -r requirements.txt

# Regenerate website
python3 generate_gift_website.py

# Restart services
systemctl restart gift-website.service
systemctl restart nginx

echo "Deployment completed!"
EOF

chmod +x /var/www/gift-website/deploy.sh

# Create log directory
mkdir -p /var/log/gift-website
chown www-data:www-data /var/log/gift-website

echo "Instance initialization completed!"
echo "Next steps:"
echo "1. Upload application files to /var/www/gift-website/"
echo "2. Run: cd /var/www/gift-website && ./deploy.sh"
echo "3. Start the backend service: systemctl start gift-website.service" 