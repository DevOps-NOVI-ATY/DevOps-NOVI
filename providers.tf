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
        name = "novi-api-test"
    }
}

resource "kubernetes_deployment" "noviAPI"{
        metadata{
            name = "novi-api"
            labels = {
                test = "novi-api-tag"
            }
            namespace = "novi-api-test"
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
                    image = "devops-novi-api"
                    image_pull_policy = "IfNotPresent"
                    name = "devops-novi-api"
                }
            }
        }
    }
}

resource "kubernetes_service" "LoadBalancer" {
  metadata {
      name = "fastapi"
      namespace = "novi-api-test"
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
