# Personal Finance Backend

A personal finance management backend built with **FastAPI**. The project allows users to manage multiple wallets, work with different currencies, and track their income and expenses.

It was developed as a learning project to practice backend development, REST API design, database integration, data validation, and authentication using Python.

## About the Project

The main goal of this project was to gain practical experience building a backend application with FastAPI and SQLAlchemy.

During development, I worked with API endpoints, Pydantic schemas, database models, authentication, and the separation of application logic into different layers.

The project was developed over one week using tutorials and documentation as learning resources.

Special thanks to the creators of the tutorial that helped me with this project:

[Watch the reference video on YouTube](https://youtu.be/8Zrt6VOBI_Y?si=P3kl_5wnDUja67D3)

---

## Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) 0.162.0
- **Data Validation:** [Pydantic](https://docs.pydantic.dev/) 2.14.1
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) 2.1.6
- **ASGI Server:** [Uvicorn](https://www.uvicorn.org/)
- **Testing:** [Pytest](https://docs.pytest.org/)

---

## Features

- User registration and authentication.
- Multiple wallet management.
- Support for different currencies.
- Income and expense tracking.
- Database integration using SQLAlchemy.
- Request validation with Pydantic.
- Separated backend layers for better code organization.

---

## Getting Started

### Prerequisites

- Python 3.10 or newer.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create and activate a virtual environment:

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the application:

```bash
uvicorn main:app --reload
```

### API Documentation

Once the server is running, the interactive API documentation is available at:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

---

## Roadmap

The project is currently in its MVP stage. Planned improvements:

- [ ] Fix bugs and improve error handling.
- [ ] Add more tests using Pytest.
- [ ] Develop a frontend and integrate it with the API.
- [ ] Add financial analytics and expense categories.