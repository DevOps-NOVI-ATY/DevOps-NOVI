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

terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}
provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "minikube"
}

resource "kubernetes_namespace" "toepassing" {
    metadata {
        name = "novi-api"
    }
}

resource "kubernetes_persistent_volume_claim" "postgres_pvc" {
	metadata {
		name = "postgres-pvc"
		namespace = "novi-api"
	}
	spec {
		access_modes = ["ReadWriteOnce"]
		resources {
			requests = {
				storage = "9Gi"  # Adjust the storage size as needed
			}
		}
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
            replicas = 10

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
                    image = "devops-novi-api"
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

# Define the PostgreSQL Deployment and Service
resource "kubernetes_deployment" "postgres" {
	metadata {
		name = "postgres"
		labels = {
			app = "postgres"
		}
		namespace = "novi-api"
	}

	spec {
		replicas = 2
		selector {
			match_labels = {
				app = "postgres"
			}
		}
		template {
			metadata {
				labels = {
					app = "postgres"
				}
			}
			spec {
				container {
					name  = "postgres"
					image = "postgres:latest"
					env {
						name  = "POSTGRES_USER"
						value = var.POSTGRES_USER
					}
					env {
						name  = "POSTGRES_PASSWORD"
						value = var.POSTGRES_PASSWORD
					}
					env {
						name  = "POSTGRES_DB"
						value = var.POSTGRES_DB
					}
				}
				volume {
					name = "devops-novi-pvc"
					persistent_volume_claim {
						claim_name = kubernetes_persistent_volume_claim.postgres_pvc.metadata[0].name
					}
				}
			}
		}
	}
}

resource "kubernetes_service" "postgres" {
	metadata {
		name = "postgres"
		namespace = "novi-api"
	}

	spec {
		selector = {
			app = "postgres"
		}
		port {
			port        = 5432
			target_port = 5432
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
