output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web.id
}

output "public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.web.public_ip
}

output "website_url" {
  description = "URL of the website"
  value       = "http://${aws_instance.web.public_ip}"
}

output "admin_url" {
  description = "URL of the admin dashboard"
  value       = "http://${aws_instance.web.public_ip}/admin.html"
}

output "ssh_command" {
  description = "SSH command to connect to the instance"
  value       = "ssh -i ssh/gift-website-key.pem ubuntu@${aws_instance.web.public_ip}"
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "security_group_id" {
  description = "ID of the security group"
  value       = aws_security_group.web.id
} 