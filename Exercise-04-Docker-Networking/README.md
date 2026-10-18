# Exercise 4: Docker Networking with Multiple Containers

## Objective

To understand Docker networking concepts and configure a multi-container application using a custom bridge network.

## Scenario

This exercise uses three containers:

- **Flask:** A Python-based REST API.
- **MySQL:** A relational database server.
- **Redis:** An in-memory data store.

All three containers are connected through a custom Docker bridge network called `my-bridge-net`.

## Technologies Used

- Docker
- Docker Bridge Networking
- Python
- Flask
- MySQL
- Redis
- Git and GitHub

## Project Structure

```text
Exercise-04-Docker-Networking/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── screenshots/
    ├── 01-network-created.png
    ├── 02-network-inspected.png
    ├── 03-containers-running.png
    ├── 04-flask-api.png
    ├── 05-ping-connectivity.png
    └── 06-flask-local-server.png

```
