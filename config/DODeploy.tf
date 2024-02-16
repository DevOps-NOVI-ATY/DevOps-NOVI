variable "KUBERNETES_CLUSTER_NAME" {
  description = "Kubernetes cluster name"
  type        = string
}

variable "DATABASE_CLUSTER_NAME" {
  description = "Database cluster name"
  type        = string
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
    helm = {
      source  = "hashicorp/helm"
      version = ">= 2.0.1"
    }
  }
}

provider "digitalocean" {
  token = var.DIGITALOCEAN_ACCESS_TOKEN
}

resource "digitalocean_kubernetes_cluster" "kubernetes-api-cluster" {
  depends_on = [ digitalocean_container_registry.container-registry, digitalocean_database_cluster.database-cluster ]
  count = 1
  name  = var.KUBERNETES_CLUSTER_NAME
  region  = "ams3"
  version = "1.29.1-do.0"
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

resource "digitalocean_database_cluster" "database-cluster" {
  count = 1
  name           = var.DATABASE_CLUSTER_NAME
  engine         = "pg"
  version        = "15"
  size           = "db-s-1vcpu-1gb"
  region         = "ams3"
  tags       	 = ["api"]
  node_count     = 1
}

resource "digitalocean_container_registry" "container-registry" {
  count = 1
  name  = var.CONTAINER_REGISTRY_NAME
  region = "ams3"
  subscription_tier_slug = "basic"
}

resource "null_resource" "wait_for_cluster" {
  # This resource depends on the Kubernetes cluster being provisioned
  depends_on = [digitalocean_kubernetes_cluster.kubernetes-api-cluster]

  # Execute a local provisioner
  provisioner "local-exec" {
    command = "sleep 45"  # Wait for 45 sec to startup cluster
  }
}

provider "kubernetes" {
  host  = digitalocean_kubernetes_cluster.kubernetes-api-cluster[0].endpoint
  token = digitalocean_kubernetes_cluster.kubernetes-api-cluster[0].kube_config.0.token

  cluster_ca_certificate = base64decode(
    digitalocean_kubernetes_cluster.kubernetes-api-cluster[0].kube_config.0.cluster_ca_certificate
  )
}

provider "helm" {
  kubernetes {
    host                   = digitalocean_kubernetes_cluster.kubernetes-api-cluster[0].endpoint
    token                  = var.DIGITALOCEAN_ACCESS_TOKEN
    cluster_ca_certificate = base64decode(digitalocean_kubernetes_cluster.kubernetes-api-cluster[0].kube_config.0.cluster_ca_certificate)
  }
}
#loki helm release configuratie 
resource "helm_release" "loki" {
  name       = "loki"
  repository = "https://grafana.github.io/helm-charts"
  chart      = "loki-stack"
  version    = "2.10.1"
  values = [
    "${file("${path.module}/dashboard/values.yaml")}"
  ]
  
  set {
    name  = "grafana.enabled"
    value = "true"
  }
  set {
    name  = "promtail.enabled"
    value = "true"
  }
  
  set {
    name  = "grafana.adminUser"
    value = "admin_username"  # Replace with your desired admin username
  }
  set {
    name  = "grafana.adminPassword"
    value = "admin_password"  # Replace with your desired admin password
  }
  
  count = 1
}

# Prometheus Helm release configuration
resource "helm_release" "prometheus" {
  name       = "prometheus"
  repository = "https://prometheus-community.github.io/helm-charts"
  chart      = "kube-prometheus-stack"
  version    = "56.3.0"
 
   timeout = 2000

  set {
    name  = "podSecurityPolicy.enabled"
    value = true
  }

  set {
    name  = "server.persistentVolume.enabled"
    value = false
  }

  set {
    name  = "prometheus.enabled"
    value = "true"
  }
  set {
    name  = "alertmanager.enabled"
    value = "true"
  }
  set {
    name  = "grafana.enabled"
    value = "false" # If you already have a Grafana instance via the Loki-stack, unless you want a separate one
  }
  # Add more configurations as needed

  count = 1
}

resource "kubernetes_config_map" "grafana-dashboards-custom" {
  metadata {
    name      = "grafana-dashboard-custom"

    labels = {
      grafana_dashboard = 1
    }
 
    annotations = {
      k8s-sidecar-target-directory = "/tmp/dashboards/custom"
    }
  }
 
  data = {
    "monitoring-app.json" = file("${path.module}/dashboard/monitoring-app.json"),
  }
}