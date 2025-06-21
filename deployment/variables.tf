variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "volume_size" {
  description = "Size of the root volume in GB"
  type        = number
  default     = 20
}

variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "gift-website"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
} 