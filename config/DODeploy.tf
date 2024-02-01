variable "CREATE_NEW_KUBERNETES_CLUSTER" {
  description = "Set to true if you want to create a new Kubernetes cluster"
  type        = bool
  default     = true
}

variable "CREATE_NEW_DATABASE_CLUSTER" {
  description = "Set to true if you want to create a new Database cluster"
  type        = bool
  default     = true
}

variable "KUBERNETES_CLUSTER_NAME" {
  description = "Kubernetes cluster name"
  type        = string
}

variable "DATABASE_CLUSTER_NAME" {
  description = "Database cluster name"
  type        = string
}

variable "CREATE_NEW_CONTAINER_REGISTRY" {
  description = "Set to true if you want to create a new Container Registry"
  type        = bool
  default     = true
}

variable "CONTAINER_REGISTRY_NAME" {
  description = "Container Registry name"
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

data "digitalocean_kubernetes_cluster" "existing_kubernetes_cluster" {
  count = var.CREATE_NEW_KUBERNETES_CLUSTER ? 0 : 1
  name  = var.KUBERNETES_CLUSTER_NAME
}

resource "digitalocean_kubernetes_cluster" "kubernetes-api-cluster" {
  count = var.CREATE_NEW_KUBERNETES_CLUSTER ? 1 : 0
  name  = var.KUBERNETES_CLUSTER_NAME
  region  = "ams3"
  version = "1.29.0-do.0"
  registry_integration = true

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

data "digitalocean_database_cluster" "existing_database_cluster" {
  count = var.CREATE_NEW_DATABASE_CLUSTER ? 0 : 1
  name  = var.DATABASE_CLUSTER_NAME
}

resource "digitalocean_database_cluster" "database-cluster" {
  count = var.CREATE_NEW_DATABASE_CLUSTER ? 1 : 0
  name           = var.DATABASE_CLUSTER_NAME
  engine         = "pg"
  version        = "15"
  size           = "db-s-1vcpu-1gb"
  region         = "ams3"
  node_count     = var.CREATE_NEW_DATABASE_CLUSTER ? 1 : 0
  tags       	 = ["api"]
}

data "digitalocean_container_registry" "existing_registry" {
  count = var.CREATE_NEW_CONTAINER_REGISTRY ? 0 : 1
  name  = var.CONTAINER_REGISTRY_NAME
}

resource "digitalocean_container_registry" "container-registry" {
  count = var.CREATE_NEW_CONTAINER_REGISTRY ? 1 : 0
  name  = var.CONTAINER_REGISTRY_NAME
  region = "ams3"
  subscription_tier_slug = "basic"
}
