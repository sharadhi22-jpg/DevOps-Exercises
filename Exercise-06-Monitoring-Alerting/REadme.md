# Exercise 6: Real-Time Operations Monitoring and Alerting

## Overview

This project implements a real-time operations monitoring and alerting
system for a delivery service. It simulates delivery metrics, collects
them using Prometheus, visualizes them using Grafana, and uses Jenkins
to execute a monitoring pipeline.

## Objectives

- Simulate delivery-service operational metrics.
- Expose metrics through a Python HTTP endpoint.
- Collect metrics using Prometheus.
- Configure alerts for delivery-service issues.
- Visualize metrics using Grafana dashboards.
- Automate monitoring checks using Jenkins.

## Technologies Used

- Python
- Prometheus
- Grafana
- Jenkins
- Docker
- Prometheus Python Client

## Project Structure

```text
Exercise-6/
├── delivery_metrics.py
├── prometheus.yml
├── alert_rules.yml
├── Jenkinsfile
├── README.md
└── screenshots/
```
