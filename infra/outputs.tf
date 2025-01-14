output "s3_bucket_name" {
  value = aws_s3_bucket.data_bucket.bucket
}

output "s3_role_arn" {
  value = aws_iam_role.s3_access_role.arn
}