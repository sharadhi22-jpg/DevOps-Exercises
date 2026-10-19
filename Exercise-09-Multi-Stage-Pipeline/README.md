# Jenkins Multi-Stage Pipeline - Python Flask Application

## Objective

Implement a Jenkins CI/CD pipeline to build, test, and deploy a Python Flask application.

## Technologies

- Python
- Flask
- Jenkins
- Git and GitHub
- Unit Testing

## Project Files

- `app.py` - Flask web application
- `requirements.txt` - Python dependencies
- `test_app.py` - Unit tests
- `Jenkinsfile` - Declarative Jenkins pipeline

## Pipeline Stages

1. **Build** - Create a virtual environment and install dependencies.
2. **Test** - Run unit tests.
3. **Deploy** - Copy application files to `python-app-deploy`.
4. **Run Application** - Start the Flask application.
5. **Test Application** - Send an HTTP request and verify the response.

## Run Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the tests:

```bash
python -m unittest discover -s .
```

Start the application:

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Expected Output

Hello, Jenkins Multi-Stage Pipeline!

## Outcome

Automated the build, testing, and mock deployment of a Python Flask application using Jenkins.
