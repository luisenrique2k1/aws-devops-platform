resource "aws_ecr_repository" "fastapi" {
  name                 = "aws-devops-fastapi"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Project     = "aws-devops-platform"
    Environment = "lab"
    ManagedBy   = "Terraform"
  }
}