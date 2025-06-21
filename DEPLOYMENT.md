# AWS Deployment Guide

This guide will help you deploy the Gift Selection Website to AWS EC2 and make it publicly accessible.

## Prerequisites

1. **AWS Account**: You need an active AWS account
2. **AWS CLI**: Install and configure AWS CLI
3. **Python 3.7+**: Required for the deployment script
4. **SSH Key**: The script will create one for you

## Setup Steps

### 1. Install AWS CLI and Configure Credentials

```bash
# Install AWS CLI (macOS)
brew install awscli

# Or download from: https://aws.amazon.com/cli/

# Configure AWS credentials
aws configure
```

You'll need to provide:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., us-east-1)
- Default output format (json)

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Deployment Script

```bash
python3 deploy_to_aws.py
```

## What the Script Does

The deployment script will:

1. **Create Security Group**: Opens ports 22 (SSH), 80 (HTTP), and 443 (HTTPS)
2. **Create Key Pair**: Generates an SSH key for secure access
3. **Launch EC2 Instance**: 
   - Uses Ubuntu 22.04 LTS
   - t2.micro instance (free tier eligible)
   - Installs nginx, Python, and required packages
4. **Upload Application Files**: Copies all necessary files to the server
5. **Configure Web Server**: Sets up nginx and gunicorn
6. **Start Services**: Launches the backend API and web server

## After Deployment

Once deployment is complete, you'll get:

- **Website URL**: `http://[PUBLIC_IP]`
- **Admin URL**: `http://[PUBLIC_IP]/admin.html`
- **Instance ID**: For AWS console management
- **Deployment Info**: Saved in `deployment_info.json`

## Accessing Your Website

1. **Main Website**: Visit `http://[PUBLIC_IP]` to access the cover page
2. **Admin Dashboard**: Visit `http://[PUBLIC_IP]/admin.html` to manage selections
3. **Employee Access**: Employees can enter their ID and select gifts

## Managing Your Deployment

### SSH Access
```bash
ssh -i gift-website-key.pem ubuntu@[PUBLIC_IP]
```

### View Logs
```bash
# Backend logs
sudo journalctl -u gift-website.service -f

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Restart Services
```bash
# Restart backend
sudo systemctl restart gift-website.service

# Restart nginx
sudo systemctl restart nginx
```

### Update Application
```bash
# Upload new files
scp -i gift-website-key.pem -r gift_website/* ubuntu@[PUBLIC_IP]:/var/www/gift-website/gift_website/

# Regenerate website
ssh -i gift-website-key.pem ubuntu@[PUBLIC_IP] "cd /var/www/gift-website && python3 generate_gift_website.py"

# Restart services
ssh -i gift-website-key.pem ubuntu@[PUBLIC_IP] "sudo systemctl restart gift-website.service && sudo systemctl restart nginx"
```

## Cost Considerations

- **t2.micro**: Free tier eligible (750 hours/month for first 12 months)
- **Data Transfer**: First 15GB/month free, then ~$0.09/GB
- **Storage**: EBS storage costs apply (~$0.10/GB/month)

## Security Notes

- The security group allows SSH access from anywhere (0.0.0.0/0)
- Consider restricting SSH access to your IP address for production
- The website runs on HTTP (not HTTPS) - consider adding SSL for production

## Troubleshooting

### Common Issues

1. **Permission Denied**: Make sure the .pem file has correct permissions (400)
2. **Connection Timeout**: Check security group rules and instance status
3. **Service Not Starting**: Check logs with `journalctl -u gift-website.service`

### Useful Commands

```bash
# Check instance status
aws ec2 describe-instances --instance-ids [INSTANCE_ID]

# Check security group
aws ec2 describe-security-groups --group-names gift-website-sg

# Terminate instance (if needed)
aws ec2 terminate-instances --instance-ids [INSTANCE_ID]
```

## Cleanup

To avoid charges, terminate the instance when not needed:

```bash
# Get instance ID from deployment_info.json
aws ec2 terminate-instances --instance-ids [INSTANCE_ID]

# Delete security group
aws ec2 delete-security-group --group-name gift-website-sg

# Delete key pair
aws ec2 delete-key-pair --key-name gift-website-key
```

## Support

If you encounter issues:
1. Check the deployment logs
2. Verify AWS credentials and permissions
3. Ensure your AWS account has EC2 permissions
4. Check that the region supports the AMI used 