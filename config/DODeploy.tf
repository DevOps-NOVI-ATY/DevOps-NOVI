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

variable "DIGITALOCEAN_ACCESS_TOKEN" {}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.DIGITALOCEAN_ACCESS_TOKEN
}

resource "digitalocean_kubernetes_cluster" "kubernetes-api-cluster" {
  name    = "api-cluster2"
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

resource "kubernetes_namespace" "api" {
    metadata {
        name = "novi-api"
    }
}

resource "kubernetes_deployment" "noviAPI" {
	metadata {
		name      = "novi-api-deployment"
		namespace = kubernetes_namespace.api.metadata[0].name
	}

	spec {
		replicas = 5

		selector {
		match_labels = {
			app = "novi-api"
		}
		}

		template {
			metadata {
				labels = {
				app = "novi-api"
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

resource "digitalocean_loadbalancer" "lb" {
  name   = "novi-api-lb"
  region = "ams3"

  forwarding_rule {
    entry_port     = 80
    entry_protocol = "http"

    target_port     = 8000
    target_protocol = "http"
  }

  droplet_ids = digitalocean_kubernetes_cluster.kubernetes-api-cluster.node_pool.*.id
}
