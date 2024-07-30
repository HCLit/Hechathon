provider "aws" {
  region = "us-east-1"  # Specify your desired region
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-bucket-name-12345"  # Ensure the bucket name is globally unique
  acl    = "private"
}