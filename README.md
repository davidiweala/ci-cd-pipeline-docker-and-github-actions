# DevOps Project - CI/CD Pipeline with Docker and GitHub Actions

## Overview
This project demonstrates a simple DevOps workflow using a Python Flask application, Docker containerization, automated testing with pytest, and CI automation with GitHub Actions.

## Tech Stack
- Python Flask
- Docker
- GitHub Actions
- pytest

## Features
- Simple web application with endpoints
- Dockerized deployment
- Automated testing
- CI pipeline triggered on push and pull request

## Endpoints
- `/` - main application endpoint
- `/david` - David check endpoint

## Run Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app/main.py