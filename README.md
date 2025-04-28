# 🚀 Kubernetes Hello World on Minikube

A beginner-friendly Kubernetes deployment of a simple Python Flask microservice that calculates change. Based on [this project](https://github.com/noahgift/flask-change-microservice), it demonstrates building, deploying, and accessing a Flask app using Minikube.

![kubernetes-load-balanced-cluster](https://user-images.githubusercontent.com/58792/111511557-3f45a280-8725-11eb-8e4a-5f5ef787796d.png)

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| [`Makefile`](Makefile) | Automates Docker build process |
| [`Dockerfile`](Dockerfile) | Defines Flask app container |
| [`app.py`](app.py) | Python Flask app logic |
| [`deployment.yaml`](deployment.yaml) | Kubernetes deployment and service definition |

---

## 🔧 Prerequisites

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)

---

## 📦 Build & Deploy

### 1. Start Minikube

```bash
minikube start
```

### 2. Verify Cluster

```bash
kubectl cluster-info
```

### 3. Point Docker to Minikube

```powershell
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

### 4. Build the Docker Image

```bash
docker build -t flask-change:latest .
```

Or using Makefile:

```bash
make build
```

### 5. Check Image Exists

```bash
docker images
```

### 6. Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
```

### 7. Verify Deployment

```bash
kubectl get deployments
kubectl get pods
```

---

## 🌐 Expose & Access the App

### 1. Expose the Deployment as a Service

```bash
kubectl expose deployment hello-python --type=NodePort --port=8080
```

### 2. Get Service URL

```bash
minikube service hello-python --url
```

Example output:

```
http://127.0.0.1:51163
```

### 3. Test the Endpoint

```bash
curl http://127.0.0.1:51163/change/45
```

Sample response:

```json
[
{
"ten_rupee_coins": 4
},
{
"five_rupee_coins": 1
}
]
```

---

## ⚖️ LoadBalancer Service

To simulate a load-balanced setup:

### 1. Check the Service

```bash
kubectl get svc hello-flask-change-service
```

### 2. Get Its URL

```bash
minikube service hello-flask-change-service --url
```

Open the resulting URL in your browser or test via `curl`.

---

## 🔍 Inspect Services

```bash
kubectl describe service hello-python
```

---

## 🧹 Cleanup

```bash
kubectl delete deployment hello-python
kubectl delete service hello-python
minikube stop
```

---

## 📚 References

- [Original flask-change project](https://github.com/noahgift/kubernetes-hello-world-python-flask)
- [Kubernetes.io Hello World guide](https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/)
- [Kubernetes service access docs](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/)
- [Azure Kubernetes deployment strategies](https://azure.microsoft.com/en-us/overview/kubernetes-deployment-strategy/)
