
variable "name" {
  type        = string
  default     = "primeraptor"
  description = "Name for the project"
}

variable "admin_whitelist" {
  type        = list(string)
  description = "IP for admin access"
}

variable "admin_username" {
  type        = string
  description = "Username for admin connection"
  default     = "admin"
}

variable "admin_email" {
  type        = string
  description = "Admin Email (to receive config information)"
}

variable "volume_size" {
  type        = number
  description = "Volume for the instance (GBs)"
  default     = 1000
}

variable "instance_type" {
  type        = string
  description = "Instance type for the server"
  default     = "m5.large"
}
