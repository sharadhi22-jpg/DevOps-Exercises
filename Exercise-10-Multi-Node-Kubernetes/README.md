# Exercise 10: Multi-Node Kubernetes Cluster with Multiple Applications and Replicasets

## Objective

Deploy two Flask applications on a three-node Kubernetes cluster using Docker images, Deployments, ReplicaSets, and NodePort Services.

## Applications

### 1. Product Catalog

- Built using Python and Flask.
- Endpoint: `/products`
- Returns a list of products with their IDs, names, and prices.
- Replicas: 2

### 2. Shopping Cart

- Built using Python and Flask.
- Endpoint: `/cart`
- Supports retrieving cart items using GET and adding items using POST.
- Replicas: 3

## Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- Minikube
- PowerShell

## Project Structure

```text
exercise10/
├── Dockerfile.product
├── Dockerfile.shopping
├── product_catalog.py
├── product_catalog_deployment.yaml
├── product_catalog_service.yaml
├── shopping_cart.py
├── shopping_cart_deployment.yaml
├── shopping_cart_service.yaml
└── README.md
```

## Implementation Steps

1. Started a three-node Minikube cluster using the Docker driver.
2. Created the Product Catalog and Shopping Cart Flask applications.
3. Built Docker images for both applications.
4. Loaded the images into the Minikube cluster.
5. Created Kubernetes Deployments with 2 Product Catalog replicas and 3 Shopping Cart replicas.
6. Configured pod anti-affinity to distribute each application's replicas across different nodes.
7. Exposed both applications using NodePort Services.
8. Verified the pods, services, and application endpoints.

## Verification

- All five application pods reached the Running state.
- Product Catalog returned Laptop, Phone, and Headphones.
- Shopping Cart successfully accepted and returned a Laptop item.

## Note

The Shopping Cart uses in-memory storage for demonstration purposes. Items are not persisted across pod restarts, and individual replicas maintain separate in-memory carts.
