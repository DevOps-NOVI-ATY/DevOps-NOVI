variable "POSTGRES_USER" {
  description = "Database administrator username"
  type        = string
  sensitive   = true
}

variable "POSTGRES_PASSWORD" {
  description = "Database administrator password"
  type        = string
  sensitive   = true
}

variable "POSTGRES_DB" {
  description = "Database name"
  type        = string
  sensitive   = true
}

variable "DATABASE_URL" {
  description = "Database connection URL"
  type        = string
  sensitive   = true
}