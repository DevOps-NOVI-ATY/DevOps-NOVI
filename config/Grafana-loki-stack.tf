
data "digitalocean_kubernetes_cluster" "kubernetes-api-cluster"{
  name = "api-cluster"
  depends_on = [digitalocean_kubernetes_cluster.kubernetes-api-cluster]
}    

provider "kubernetes" {
  host  = data.digitalocean_kubernetes_cluster.kubernetes-api-cluster.endpoint
  token = data.digitalocean_kubernetes_cluster.kubernetes-api-cluster.kube_config[0].token

  cluster_ca_certificate = base64decode(
    data.digitalocean_kubernetes_cluster.kubernetes-api-cluster.kube_config[0].cluster_ca_certificate
  )

}
 
provider "helm" {

  kubernetes {
    host  = digitalocean_kubernetes_cluster.kubernetes-api-cluster[0].endpoint
    token = digitalocean_kubernetes_cluster.kubernetes-api-cluster[0].kube_config[0].token
    
    cluster_ca_certificate = base64decode(
      digitalocean_kubernetes_cluster.kubernetes-api-cluster[0].kube_config[0].cluster_ca_certificate
    )
  }

}
 
resource "kubernetes_namespace" "loki-stack" {
  metadata {
    annotations = {
      name = "loki-stack"
    }
  
    name = "loki-stack"
  }
    depends_on = [digitalocean_kubernetes_cluster.kubernetes-api-cluster]
}


  resource "helm_release" "loki" {
    name       = "loki"
    repository = "https://grafana.github.io/helm-charts"
    chart      = "loki-stack"
    version    = "2.10.1"
    namespace = "loki-stack"
  
    set {
      name  = "grafana.enabled"
      value = "true"
    }
  
    set {
      name  = "promtail.enabled"
      value = "true"
    }
    depends_on = [kubernetes_namespace.loki-stack]
  }