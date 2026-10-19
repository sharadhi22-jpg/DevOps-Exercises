# Exercise 7: Introduction to Continuous Integration (CI) and Jenkins Installation

## Objective

To understand the fundamentals of Continuous Integration (CI) and install and access Jenkins using Docker.

## What is Continuous Integration (CI)?

Continuous Integration is a software development practice in which developers frequently integrate code changes into a shared repository. Automated builds and tests help detect errors early and improve software quality.

## Key Features of CI

- Frequent code integration
- Automated builds
- Automated testing
- Immediate feedback

## Benefits of CI

- Early bug detection
- Improved collaboration
- Faster development cycles
- Improved code quality

## Tools and Technologies

- Docker Desktop
- Jenkins LTS
- Visual Studio Code
- Web Browser

## Jenkins Installation

Jenkins can be installed using the official Jenkins LTS Docker image.

Command:

```powershell
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```
