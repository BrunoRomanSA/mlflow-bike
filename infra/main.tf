provider "aws" {
  region = "us-east-1"
}

# Criar o bucket S3 para armazenar os dados
resource "aws_s3_bucket" "data_bucket" {
  bucket = var.bucket_data
}

# Criar uma política para permitir acesso ao bucket (opcional)
resource "aws_iam_role" "s3_access_role" {
  name = var.role_name

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_policy" "s3_access_policy" {
  name        = var.policy_name
  description = "Policy to allow S3 access for the bucket"
  policy      = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["s3:*"]
        Effect   = "Allow"
        Resource = [
          "arn:aws:s3:::${var.bucket_data}",
          "arn:aws:s3:::${var.bucket_data}/*"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_s3_policy" {
  role       = aws_iam_role.s3_access_role.name
  policy_arn = aws_iam_policy.s3_access_policy.arn
}