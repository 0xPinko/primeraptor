resource "aws_ses_email_identity" "primeraptor_email_admin" {
  email = var.admin_email
}