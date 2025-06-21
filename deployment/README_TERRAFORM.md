# Terraform Deployment for Gift Selection Website

This directory contains Terraform configuration to deploy the Gift Selection Website to AWS EC2 with proper infrastructure as code practices.

## 🏗️ Infrastructure Overview

The Terraform configuration creates:

- **VPC** with public subnet
- **Internet Gateway** for internet access
- **Security Group** with HTTP, HTTPS, and SSH access
- **EC2 Instance** running Ubuntu 22.04 LTS
- **Key Pair** for SSH access
- **Nginx** web server
- **Gunicorn** application server

## 📋 Prerequisites

1. **Terraform** (>= 1.0)
   ```bash
   # macOS
   brew install terraform
   
   # Or download from: https://developer.hashicorp.com/terraform/downloads
   ```

2. **AWS CLI** configured
   ```bash
   aws configure
   ```

3. **SSH Key** (will be generated automatically)

## 🚀 Quick Start

### 1. Generate the Website

First, make sure your website is generated:

```bash
python3 generate_gift_website.py
```

### 2. Deploy with Script

Use the automated deployment script:

```bash
chmod +x deploy.sh
./deploy.sh
```

This script will:
- Generate SSH keys
- Initialize Terraform
- Deploy infrastructure
- Upload application files
- Configure and start services

### 3. Manual Deployment

If you prefer manual deployment:

```bash
# Initialize Terraform
terraform init

# Plan deployment
terraform plan

# Apply configuration
terraform apply

# Get outputs
terraform output
```

## 📁 File Structure

```
.
├── main.tf                 # Main Terraform configuration
├── variables.tf            # Variable definitions
├── outputs.tf              # Output definitions
├── user_data.sh            # EC2 instance initialization script
├── deploy.sh               # Automated deployment script
├── terraform.tfvars.example # Example configuration
└── ssh/                    # SSH keys (generated)
    ├── gift-website-key    # Private key
    └── gift-website-key.pub # Public key
```

## ⚙️ Configuration

### Variables

Create `terraform.tfvars` based on the example:

```bash
cp terraform.tfvars.example terraform.tfvars
```

Edit the variables as needed:

```hcl
aws_region = "us-east-1"
instance_type = "t2.micro"
volume_size = 20
app_name = "gift-website"
environment = "production"
```

### Available Variables

| Variable | Description | Default | Type |
|----------|-------------|---------|------|
| `aws_region` | AWS region | `us-east-1` | string |
| `instance_type` | EC2 instance type | `t2.micro` | string |
| `volume_size` | Root volume size (GB) | `20` | number |
| `app_name` | Application name | `gift-website` | string |
| `environment` | Environment name | `production` | string |

## 🌐 Accessing Your Website

After deployment, you'll get:

- **Website**: `http://[PUBLIC_IP]`
- **Admin Dashboard**: `http://[PUBLIC_IP]/admin.html`
- **SSH Access**: `ssh -i ssh/gift-website-key ubuntu@[PUBLIC_IP]`

## 🔧 Management Commands

### View Infrastructure Status
```bash
terraform show
terraform output
```

### Update Application
```bash
# Upload new files
scp -i ssh/gift-website-key -r gift_website/* ubuntu@[PUBLIC_IP]:/var/www/gift-website/gift_website/

# Deploy on server
ssh -i ssh/gift-website-key ubuntu@[PUBLIC_IP] "cd /var/www/gift-website && ./deploy.sh"
```

### View Logs
```bash
# Backend logs
ssh -i ssh/gift-website-key ubuntu@[PUBLIC_IP] "sudo journalctl -u gift-website.service -f"

# Nginx logs
ssh -i ssh/gift-website-key ubuntu@[PUBLIC_IP] "sudo tail -f /var/log/nginx/access.log"
```

### Restart Services
```bash
ssh -i ssh/gift-website-key ubuntu@[PUBLIC_IP] "sudo systemctl restart gift-website.service && sudo systemctl restart nginx"
```

## 🧹 Cleanup

To destroy all resources and avoid charges:

```bash
terraform destroy
```

This will remove:
- EC2 instance
- VPC and networking
- Security group
- Key pair

## 🔒 Security Considerations

### Current Configuration
- SSH access from anywhere (0.0.0.0/0)
- HTTP/HTTPS access from anywhere
- Basic security headers enabled

### Production Recommendations
1. **Restrict SSH access** to your IP address
2. **Add SSL/TLS** with Let's Encrypt
3. **Use AWS Secrets Manager** for sensitive data
4. **Enable CloudWatch** monitoring
5. **Set up backup strategy**

## 💰 Cost Estimation

- **t2.micro**: Free tier eligible (750 hours/month for first 12 months)
- **EBS Storage**: ~$2/month for 20GB
- **Data Transfer**: First 15GB/month free
- **Total**: ~$2-5/month after free tier

## 🐛 Troubleshooting

### Common Issues

1. **Permission Denied**
   ```bash
   chmod 600 ssh/gift-website-key
   ```

2. **Instance Not Ready**
   ```bash
   # Wait longer for user data script
   sleep 120
   ```

3. **Service Not Starting**
   ```bash
   ssh -i ssh/gift-website-key ubuntu@[PUBLIC_IP] "sudo systemctl status gift-website.service"
   ```

4. **Nginx Issues**
   ```bash
   ssh -i ssh/gift-website-key ubuntu@[PUBLIC_IP] "sudo nginx -t"
   ```

### Useful Commands

```bash
# Check instance status
aws ec2 describe-instances --instance-ids [INSTANCE_ID]

# View Terraform state
terraform state list
terraform state show aws_instance.web

# Force recreation
terraform taint aws_instance.web
terraform apply
```

## 📚 Additional Resources

- [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/)
- [Nginx Configuration](https://nginx.org/en/docs/)
- [Gunicorn Documentation](https://gunicorn.org/)

## 🤝 Contributing

To improve this deployment:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the deployment
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. 