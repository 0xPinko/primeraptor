locals {
  primeraptor_sanitized_bucket_name = replace(var.name, "/[^A-Za-z0-9-]/", "-")
}

resource "random_string" "primeraptor_random_name" {
  length  = 10
  special = false
  upper   = false
  lower   = true
}

resource "aws_s3_bucket" "primeraptor_s3_bucket" {
  bucket        = "primeraptor-${lower(local.primeraptor_sanitized_bucket_name)}-${random_string.primeraptor_random_name.result}"
  force_destroy = true

  lifecycle {
    prevent_destroy = false
  }
}

data "aws_iam_policy_document" "primeraptor_s3_ssl_only_policy" {
  statement {
    effect = "Deny"

    principals {
      type        = "*"
      identifiers = ["*"]
    }

    actions = [
      "s3:*"
    ]

    resources = [
      "${aws_s3_bucket.primeraptor_s3_bucket.arn}",
      "${aws_s3_bucket.primeraptor_s3_bucket.arn}/*"
    ]

    condition {
      test     = "Bool"
      variable = "aws:SecureTransport"
      values   = ["false"]
    }
  }
}

resource "aws_s3_bucket_policy" "primeraptor_bucket_policy" {
  bucket = aws_s3_bucket.primeraptor_s3_bucket.id
  policy = data.aws_iam_policy_document.primeraptor_s3_ssl_only_policy.json
}
