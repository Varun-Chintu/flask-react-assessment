# Project Name

**Flask-React Comment API** (replace with your actual project name)

## Description

A brief overview of your project. Example:

> This project is a simple task management backend using Flask with CRUD APIs for comments. It also integrates with a React frontend for task management and comments.

---

## Features

* RESTful API for comments: Create, Read, Update, Delete (CRUD)
* Task management APIs
* Integrated Flask backend with React frontend (if applicable)
* In-memory data storage for demo purposes

---

## Tech Stack

* **Backend:** Python, Flask, Flask-CORS
* **Frontend:** React (if used)
* **Dependencies:** See `Pipfile` for backend packages
* **Version Control:** Git & GitHub

---

## Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Varun-Chintu/flask-react-assessment.git
cd flask-react-assessment/src/apps/backend
```

### 2️⃣ Setup Python virtual environment with Pipenv

```bash
pipenv --python 3.11
pipenv install
pipenv shell
```

### 3️⃣ Run the server

```bash
set PYTHONPATH=.
python server.py
```

Server will start on: `http://127.0.0.1:5000`

---

## API Endpoints

### Comments API

* **Create Comment:** `POST /api/comments`
* **Get All Comments:** `GET /api/comments`
* **Update Comment:** `PUT /api/comments/<comment_id>`
* **Delete Comment:** `DELETE /api/comments/<comment_id>`

**Request/Response Example:**

```json
POST /api/comments
{
  "task_id": 123,
  "text": "This is a comment"
}
```

---

## Notes

* Temporal server is required for some backend tasks. Ensure it’s running if needed.
* This project uses in-memory storage for demo purposes, so data will reset on server restart.

# Flask React Template

Boilerplate project for Flask, React & MongoDB based projects. This README documents the steps necessary to get the application up and running, and various components of the application.

| Build Status                                                                                                                                                                                                                                     | Code Coverage                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [![Production Deploy](https://github.com/jalantechnologies/rflask-boilerplate/actions/workflows/production_on_push.yml/badge.svg?branch=main)](https://github.com/jalantechnologies/rflask-boilerplate/actions/workflows/production_on_push.yml) | [![Code Coverage](https://sonarqube.platform.jalantechnologies.com/api/project_badges/measure?project=jalantechnologies_rflask-boilerplate&metric=coverage&token=a4dd71c68afbb8da4b7ed1026329bf0933298f79)](https://sonarqube.platform.jalantechnologies.com/dashboard?id=jalantechnologies_rflask-boilerplate) |

## Documentation Directory

- [Getting Started](docs/getting-started.md)
- [Backend Architecture](docs/backend-architecture.md)
- [Logging](docs/logging.md)
- [Configuration](docs/configuration.md)
- [Secrets](docs/secrets.md)
- [Bootstrapping](docs/bootstrapping.md)
- [Scripts](docs/scripts.md)
- [Code Formatting](docs/code-formatting.md)
- [Workers](docs/workers.md)
- [Deployment](docs/deployment.md)
- [Running Scripts in Production](docs/running-scripts-in-production.md)

## Best Practices

Once you have familiarized yourself with the documentation, head over to the [Engineering Handbook](https://github.com/jalantechnologies/handbook/blob/main/engineering/index.md) to learn about the best practices we follow at Better Software.

PS: Before you start working on the application, these [three git settings](https://spin.atomicobject.com/git-configurations-default/) are a must-have!
