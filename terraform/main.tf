provider "aws" {
    region = "eu-west-2"
}

resource "aws_instance" "skylaunch" {
    ami = "ami-0c76bd4580fbef5ff"
    instance_type = "t3.micro"
    tags = {
      name = "skylaunch-server"
    }
}
resource "aws_ecr_repository" "skylaunch" {
  name = "skylaunch"

  tags = {
    Name = "skylaunch"
  }
}

resource "aws_iam_role" "ec2_ecr_role" {
  name = "skylaunch-ec2-ecr-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ecr_access" {
  role       = aws_iam_role.ec2_ecr_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

resource "aws_db_instance" "skylaunch" {
  identifier        = "skylaunch-db"
  engine            = "postgres"
  engine_version    = "17.6"
  instance_class    = "db.t4g.micro"
  allocated_storage = 20
  username          = "postgres"
  password = "var.db_password"
  skip_final_snapshot = true

  tags = {
    Name = "skylaunch-db"
  }
}