# Exercise 02 – Minikube, Kubectl & Flask

## Objective

Deploy a simple Flask web application on a local Kubernetes cluster using Minikube and kubectl.

This exercise demonstrates:

- Creating and managing a Minikube Kubernetes cluster
- Building a Docker image for a Flask application
- Loading the Docker image into Minikube
- Creating a Kubernetes Deployment
- Creating a Kubernetes NodePort Service
- Verifying the Deployment and Pod
- Accessing the Flask application through Minikube

---

## Project Structure

```text
Exercise-02-Minikube-Kubectl-Flask/
├── Dockerfile
├── app.py
├── flask-deployment.yaml
├── README.md
└── screenshots/
    ├── 01-minikube-status.png
    ├── 02-service-created.png
    ├── 03-deployment-pod.png
    ├── 04-minikube-service.png
    └── 05-flask-browser.png
