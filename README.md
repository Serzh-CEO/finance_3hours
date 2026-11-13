# Personal Finance

A personal finance app built with **FastAPI** and a lightweight web dashboard. Users can register, manage multiple wallets in different currencies, track income and expenses, transfer money between wallets, and see everything on a dashboard.

It started as a learning project to practice backend development, REST API design, database integration, data validation, and authentication with Python.

## Screenshots
<img width="1919" height="861" alt="image" src="https://github.com/user-attachments/assets/d50d882a-85f7-4514-8cfa-c90927fe78c0" />
<img width="1885" height="862" alt="image" src="https://github.com/user-attachments/assets/1bebafd6-ef6c-439a-8735-6695ea3531f3" />
<img width="1875" height="854" alt="image" src="https://github.com/user-attachments/assets/a8484a12-c773-4d5c-937f-7e9575f71887" />






## About the Project

The base of the project was built by following a tutorial:

[Watch the reference video on YouTube](https://youtu.be/8Zrt6VOBI_Y?si=P3kl_5wnDUja67D3)

On top of it, I added my own improvements:

- **Password authentication** with Argon2 password hashing.
- **JWT access tokens** (replacing the original "login as token" approach).
- **A web frontend** with a dashboard that shows the capabilities of the API.
- Bug fixes and a `GET /wallets` endpoint.

---

## Tech Stack

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) – web framework
- [Pydantic](https://docs.pydantic.dev/) – data validation
- [SQLAlchemy](https://www.sqlalchemy.org/) + SQLite – ORM and database
- [Uvicorn](https://www.uvicorn.org/) – ASGI server
- [PyJWT](https://pyjwt.readthedocs.io/) – JWT tokens
- [pwdlib](https://github.com/frankie567/pwdlib) (Argon2) – password hashing
- [python-dotenv](https://github.com/theskumar/python-dotenv) – environment variables

**Frontend**
- Vanilla HTML / CSS / JavaScript (single file, no build step)
- [Chart.js](https://www.chartjs.org/) – charts

---

## Features

- User registration and login with a password.
- Stateless authentication with JWT access tokens (30 min lifetime).
- Multiple wallets with different currencies (RUB, USD, EUR, KZT).
- Income and expense tracking with categories.
- Transfers between wallets with automatic currency conversion.
- Total balance in a chosen currency.
- Operation history with filters by wallet and date.
- Dashboard: balances, income/expense summary, daily activity chart, expenses-by-category chart.
- Request validation with Pydantic.
- Layered backend structure: API → service → repository.

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

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with a secret key used to sign JWT tokens:

```
SECRET_KEY=your_long_random_string
```

Generate a good value with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

> Never commit the `.env` file. It is already listed in `.gitignore`.

5. Start the application:

```bash
uvicorn main:app --reload
```

### Using the App

- **Dashboard (frontend):** http://127.0.0.1:8000/ui/
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Create an account on the dashboard login page, sign in, and start by creating a wallet.

---

## API Overview

All endpoints are prefixed with `/api/v1`. Endpoints marked 🔒 require the header `Authorization: Bearer <access_token>`.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users` | Register a new user (login + password) |
| POST | `/auth/login` | Log in and receive a JWT access token |
| GET | `/users/me` 🔒 | Current user info |
| GET | `/wallets` 🔒 | List wallets |
| POST | `/wallets` 🔒 | Create a wallet |
| GET | `/wallet_balance` 🔒 | Balance of a wallet by name |
| GET | `/total_balance` 🔒 | Total balance in a target currency |
| GET | `/operations` 🔒 | Operation history (filters: wallet, dates) |
| POST | `/operations/income` 🔒 | Add income |
| POST | `/operations/expense` 🔒 | Add expense |
| POST | `/operations/transfer` 🔒 | Transfer between wallets |

### Authentication flow

1. Register with `POST /users`. The password is stored only as an Argon2 hash.
2. Log in with `POST /auth/login` and receive an `access_token` (JWT).
3. Send the token in the `Authorization: Bearer` header with every protected request.

---

## Project Structure

```
├── main.py              # App entry point
├── app/
│   ├── api/v1/          # Routers (auth, users, wallets, operations)
│   ├── service/         # Business logic
│   ├── repository/      # Database access
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── security.py      # Password hashing and JWT
│   └── dependency.py    # DB session and current user
└── frontend/
    └── index.html       # Dashboard
```
