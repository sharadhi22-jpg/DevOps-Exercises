# Exercise 03 – Docker, Docker Hub & Kubernetes ReplicaSet

## Objective

The objective of this exercise is to containerize a Flask-based flash sale application using Docker, push the Docker image to Docker Hub, and deploy the application on Kubernetes using a ReplicaSet and Service.

The exercise also demonstrates scaling the ReplicaSet and verifying multiple running Pods.

---

## Technologies Used

- Python
- Flask
- Docker
- Docker Hub
- Kubernetes
- Minikube
- kubectl
- Gunicorn

---

## Project Structure

```text
Exercise-03-Docker-ReplicaSet-FlashSale/
├── app.py
├── Dockerfile
├── flashsale-replicaset.yaml
├── README.md
└── screenshots/
    ├── 01-replicaset-pods.png
    ├── 02-minikube-restart.png
    ├── 03-scale-replicaset.png
    ├── 04-pod-details.png
    └── 05-final-pods.png
