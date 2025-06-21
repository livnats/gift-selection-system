#!/bin/bash
# Terraform Deployment Script for Gift Selection Website

set -e

echo "🚀 Terraform Deployment Script for Gift Selection Website"
echo "=========================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Terraform is installed
if ! command -v terraform &> /dev/null; then
    print_error "Terraform is not installed. Please install Terraform first."
    echo "Visit: https://developer.hashicorp.com/terraform/downloads"
    exit 1
fi

# Check if AWS CLI is configured
if ! aws sts get-caller-identity &> /dev/null; then
    print_error "AWS CLI is not configured. Please run 'aws configure' first."
    exit 1
fi

# Create SSH directory and generate key pair
print_status "Setting up SSH key pair..."
mkdir -p ssh

if [ ! -f "ssh/gift-website-key" ]; then
    ssh-keygen -t rsa -b 4096 -f ssh/gift-website-key -N "" -C "gift-website-deployment"
    print_success "SSH key pair generated"
else
    print_warning "SSH key pair already exists"
fi

# Copy public key to the expected location
chmod 600 ssh/gift-website-key
chmod 644 ssh/gift-website-key.pub

# Initialize Terraform
print_status "Initializing Terraform..."
terraform init

# Plan the deployment
print_status "Planning deployment..."
terraform plan

# Ask for confirmation
echo
read -p "Do you want to proceed with the deployment? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    print_warning "Deployment cancelled"
    exit 0
fi

# Apply the configuration
print_status "Deploying infrastructure..."
terraform apply -auto-approve

# Get the outputs
print_status "Getting deployment information..."
PUBLIC_IP=$(terraform output -raw public_ip)
INSTANCE_ID=$(terraform output -raw instance_id)

print_success "Infrastructure deployed successfully!"
echo
echo "📋 Deployment Information:"
echo "=========================="
echo "Instance ID: $INSTANCE_ID"
echo "Public IP: $PUBLIC_IP"
echo "Website URL: http://$PUBLIC_IP"
echo "Admin URL: http://$PUBLIC_IP/admin.html"
echo "SSH Command: ssh -i ssh/gift-website-key ubuntu@$PUBLIC_IP"

# Wait for instance to be ready
print_status "Waiting for instance to be ready..."
sleep 60

# Upload application files
print_status "Uploading application files..."

# Ensure remote directory exists
print_status "Creating remote directory structure..."
ssh -i ssh/gift-website-key -o StrictHostKeyChecking=no ubuntu@$PUBLIC_IP "sudo mkdir -p /var/www/gift-website && sudo chown -R ubuntu:ubuntu /var/www/gift-website"

# Upload necessary files
scp -i ssh/gift-website-key -o StrictHostKeyChecking=no \
    ../../backend.py \
    ../../generate_gift_website.py \
    ../../gifts-catalog.csv \
    ../../requirements.txt \
    ../../cover.html \
    ../../admin.html \
    ubuntu@$PUBLIC_IP:/var/www/gift-website/

print_success "Application files uploaded"

# Deploy the application
print_status "Deploying application..."
ssh -i ssh/gift-website-key -o StrictHostKeyChecking=no ubuntu@$PUBLIC_IP << 'EOF'
cd /var/www/gift-website
source venv/bin/activate
pip install -r requirements.txt
python3 generate_gift_website.py
sudo systemctl start gift-website.service
sudo systemctl restart nginx
EOF

print_success "Application deployed successfully!"

# Save deployment info
cat > deployment_info.json << EOF
{
  "instance_id": "$INSTANCE_ID",
  "public_ip": "$PUBLIC_IP",
  "website_url": "http://$PUBLIC_IP",
  "admin_url": "http://$PUBLIC_IP/admin.html",
  "ssh_command": "ssh -i ssh/gift-website-key ubuntu@$PUBLIC_IP",
  "deployment_time": "$(date -u +"%Y-%m-%d %H:%M:%S UTC")"
}
EOF

print_success "Deployment information saved to deployment_info.json"

echo
echo "🎉 Deployment completed successfully!"
echo "====================================="
echo "🌐 Website: http://$PUBLIC_IP"
echo "🔧 Admin: http://$PUBLIC_IP/admin.html"
echo "📋 Instance ID: $INSTANCE_ID"
echo
echo "To destroy the infrastructure when done:"
echo "  terraform destroy"
echo
echo "To SSH into the instance:"
echo "  ssh -i ssh/gift-website-key ubuntu@$PUBLIC_IP" 