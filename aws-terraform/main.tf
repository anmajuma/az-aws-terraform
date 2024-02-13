
terraform {
  required_version = "~> 1.7.3"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.3.0"
    }
  }
}
# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}
resource "aws_vpc" "primary" {
 cidr_block = "10.0.0.0/16"
 
 tags = {
   Name = "primary-vpc"
 }
}
resource "aws_subnet" "subnet_private_01" {
 vpc_id            =  aws_vpc.primary.id
 cidr_block        = "10.0.1.0/24"
 availability_zone = "us-east-1a"
 
 tags = {
   Name = "subnet_private_01"
 }
}
 
resource "aws_subnet" "subnet_private_02" {
 vpc_id            =  aws_vpc.primary.id
 cidr_block        = "10.0.2.0/24"
 availability_zone = "us-east-1b"
 
 tags = {
   Name = "subnet_private_02"
 }
}
 
