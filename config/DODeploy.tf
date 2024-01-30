variable "DATABASE_URL" {
  description = "Database connection URL"
  type        = string
  sensitive   = true
}

terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

variable "DIGITALOCEAN_TOKEN" {}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.DIGITALOCEAN_TOKEN
}

resource "digitalocean_kubernetes_cluster" "kubernetes-api-cluster" {
  name    = "eapi-cluster"
  region  = "ams3"
  version = "1.22.2-do.1"

  node_pool {
    name       = "pool-1"
    size       = "s-1vcpu-1gb"  # Change to the smallest droplet size
    node_count = 3
  }
}

resource "kubernetes_namespace" "toepassing" {
    metadata {
        name = "novi-api"
    }
}

resource "kubernetes_deployment" "noviAPI"{
        metadata{
            name = "novi-api"
            labels = {
                test = "novi-api-tag"
            }
            namespace = "novi-api"
        }
        spec {
            replicas = 5

            selector {
                match_labels = {
                    test = "novi-api-tag"
                }
            }
        template {
            metadata {
                labels = {
                    test = "novi-api-tag"

                }
            }

            spec {
                container{
                    image = "registry.digitalocean.com/dev-ops-novi-api/api"
                    image_pull_policy = "IfNotPresent"
                    name = "devops-novi-api"
                    env {
						name  = "DATABASE_URL"
						value = var.DATABASE_URL
                    }
                }
            }
        }
    }
}

resource "kubernetes_service" "LoadBalancer" {
  metadata {
      name = "fastapi"
      namespace = "novi-api"
    }

spec {
    selector = {
          test = "novi-api-tag"
    }

    port {
      port = 80
      target_port = 8000

      }
    type = "LoadBalancer"
  }

}
