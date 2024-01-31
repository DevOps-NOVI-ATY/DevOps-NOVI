variable "CREATE_NEW_CLUSTER" {
  description = "Set to true if you want to create a new cluster"
  type        = bool
  default     = true
}

variable "DATABASE_URL" {
  description = "Database connection URL"
  type        = string
  sensitive   = true
}

variable "CLUSTER_NAME" {
  description = "Kubernetes cluster name"
  type        = string
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

provider "digitalocean" {
  token = var.DIGITALOCEAN_ACCESS_TOKEN
}

data "digitalocean_kubernetes_cluster" "existing_cluster" {
  count = var.CREATE_NEW_CLUSTER ? 0 : 1
  name  = var.CLUSTER_NAME
}

resource "digitalocean_kubernetes_cluster" "kubernetes-api-cluster" {
  count = var.CREATE_NEW_CLUSTER ? 1 : 0
  name  = var.CLUSTER_NAME
  region  = "ams3"
  version = "1.29.0-do.0"

  node_pool {
    name       = "api-pool"
    size       = "s-2vcpu-2gb"
    auto_scale = true
    min_nodes  = 1
    max_nodes  = 3
    tags       = ["api"]
  }
  tags = ["api"]
}