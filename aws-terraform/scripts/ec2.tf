provider "aws" {
  region  = "us-east-1"
}

resource "aws_instance" "instance_a" {
    
  ami                         = "ami-0e731c8a588258d0d"
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.private_subnets[0].id
  associate_public_ip_address = true
   lifecycle {
    ignore_changes = [security_groups]
  }
   tags = {
   Name = "Project EC2"
 }
}