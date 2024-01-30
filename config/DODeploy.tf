variable "DATABASE_URL" {
  description = "Database connection URL"
  type        = string
  sensitive   = true
}

variable "DIGITALOCEAN_ACCESS_TOKEN" {}

terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.DIGITALOCEAN_ACCESS_TOKEN
}

resource "digitalocean_kubernetes_cluster" "kubernetes-api-cluster" {
  name    = "api-cluster"
  region  = "ams3"
  version = "1.29.0-do.0"

  node_pool {
    name       = "api-pool"
    size       = "s-2vcpu-2gb"
    auto_scale = true
    min_nodes  = 1
    max_nodes  = 3
  }
}
