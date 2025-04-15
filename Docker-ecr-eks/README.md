# Docker-ecr-eks

---

# Deploying "Welcome ECR-EKS!" Flask App on AWS EKS with Docker & ECR

This guide walks through containerizing your `Flask` app (`app.py`), pushing it to **AWS ECR**, and deploying it to **Amazon EKS**.

---

## 📁 Project Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── demo-app-deployment.yml
└── demo-app-service.yml
```

---

## 🐍 app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome ECR-EKS"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

---

## 🐳 Docker

### 1. Dockerfile

```Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY app.py .
RUN pip install Flask

EXPOSE 8080
CMD ["python", "app.py"]
```

### 2. Build & Tag the Image
```bash
docker build -t demo-app .
docker tag demo-app:latest 242201301959.dkr.ecr.us-east-1.amazonaws.com/demo-app:latest
```

---

## 🔐 AWS Setup

### 3. Configure AWS CLI
```bash
aws configure
```

Use:
- Access Key
- Secret Key
- Region: `us-east-1`

---

## 📦 Push to ECR

### 4. Authenticate Docker to ECR
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 242201301959.dkr.ecr.us-east-1.amazonaws.com
```

### 5. Create ECR Repository
```bash
aws ecr create-repository --repository-name demo-app
```

### 6. Push Image to ECR
```bash
docker push 242201301959.dkr.ecr.us-east-1.amazonaws.com/demo-app:latest
```

---

## ☸️ Kubernetes on EKS

### 7. Deployment YAML

`demo-app-deployment.yml`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: demo-app
  template:
    metadata:
      labels:
        app: demo-app
    spec:
      containers:
      - name: demo-app
        image: 242201301959.dkr.ecr.us-east-1.amazonaws.com/demo-app:latest
        ports:
        - containerPort: 8080
```

### 8. Service YAML

`demo-app-service.yml`:
```yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-app-service
spec:
  type: LoadBalancer
  selector:
    app: demo-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
```

---

## 🚀 Apply to Cluster

### 9. Deploy to EKS
```bash
kubectl apply -f demo-app-deployment.yml
kubectl apply -f demo-app-service.yml
```

### 10. Get External IP
```bash
kubectl get service demo-app-service
```

Visit:
```
http://<EXTERNAL-IP>/
```

---

## 🎯 Result

If everything is correct, you’ll see:
```
Welcome ECR-EKS!
```

---
http://af66ae2cc4cd940ffb6779330be5a9cf-1232043196.us-east-1.elb.amazonaws.com/
