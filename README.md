# kubernetes-hello-world-on-minikube

A Kubernetes Hello World Project for Python Flask. This project uses [a simple Flask app that returns correct change](https://github.com/noahgift/flask-change-microservice) as the base and deploys it to Kubernetes.

![kubernetes-load-balanced-cluster](https://user-images.githubusercontent.com/58792/111511557-3f45a280-8725-11eb-8e4a-5f5ef787796d.png)

---

## 📁 Assets in Repo

- `Makefile`: [Builds project](https://github.com/abhinavsaluja2004/kubernetes_on_minikube/blob/main/Makefile)
- `Dockerfile`: [Container configuration](https://github.com/abhinavsaluja2004/kubernetes_on_minikube/blob/main/Dockerfile)
- `app.py`: [Flask app](https://github.com/abhinavsaluja2004/kubernetes_on_minikube/blob/main/app.py)
- `kube-hello-change.yaml`: [Kubernetes YAML Config](https://github.com/abhinavsaluja2004/kubernetes_on_minikube/blob/main/kube-hello-change.yaml)

---

## 🚀 Get Started

### 🔧 Prerequisites

- [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Install kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Install Docker Desktop](https://www.docker.com/products/docker-desktop)

---

### 🐳 Build and Deploy

1. **Start Minikube**

   ```bash
   minikube start
   ```

2. **Check Kubernetes cluster status**

   ```bash
   kubectl cluster-info
   ```

3. **Point Docker to Minikube’s Docker engine**

   ```powershell
   & minikube -p minikube docker-env --shell powershell | Invoke-Expression
   ```

4. **Build Docker image**

   ```bash
   docker build -t flask-change:latest .
   ```

   Or use the Makefile:

   ```bash
   make build
   ```

5. **Verify image exists**

   ```bash
   docker images
   ```

6. **Deploy to Kubernetes**

   ```bash
   kubectl apply -f kube-hello-change.yaml
   ```

7. **Check deployment and pods**

   ```bash
   kubectl get deployments
   kubectl get pods
   ```

   Sample output:

   ```
   NAME                         READY   STATUS    RESTARTS   AGE
   hello-python-xxxxxxx-xxxxx   1/1     Running   0          5s
   ```

---

### 🌐 Expose and Access App

1. **Expose deployment as a service**

   ```bash
   kubectl expose deployment hello-python --type=NodePort --port=8080
   ```

2. **Get service URL**

   ```bash
   minikube service hello-python --url
   ```

   You’ll get a URL like `http://127.0.0.1:51163`

3. **Test the endpoint**

   ```bash
   curl http://127.0.0.1:8080/change/1/34
   ```

   Sample output:

   ```json
   [
     {
       "5": "quarters"
     }, 
     {
       "1": "nickels"
     }, 
     {
       "4": "pennies"
     }
   ]
   ```

---

### 🔍 Inspect Service

```bash
kubectl describe service hello-python
```

Sample output:

```yaml
Name:                     hello-python
Type:                     NodePort
Port:                     8080/TCP
NodePort:                 32000/TCP
Endpoints:                172.17.0.6:8080, ...
```

---

### 🧹 Cleanup

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
