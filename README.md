# Oriel URL Shortener

A lightning-fast, lightweight URL shortener built with **FastAPI**, **SQLAlchemy**, and **SQLite**. This project provides a simple yet robust API for creating short links, tracking clicks, and redirecting users to original URLs.

## 🚀 Features

- **Shorten URLs**: Transform long, cumbersome URLs into manageable short codes.
- **Redirection**: Instant redirection from short codes to original destinations.
- **Click Analytics**: Track the number of times each short link is accessed.
- **Validation**: built-in URL validation to ensure data integrity.
- **Health Monitoring**: Simple endpoint to verify service availability.
- **Clean Architecture**: Modular code structure for easy extensibility.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [SQLite](https://www.sqlite.org/index.html)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Validation**: [Pydantic](https://docs.pydantic.dev/) & [Validators](https://github.com/python-validators/validators)
- **Server**: [Uvicorn](https://www.uvicorn.org/)

## 📂 Project Structure

```text
Oriel_project/
├── URL_shortener/
│   ├── main.py              # Application entry point
│   ├── db/                 # Database configuration and models
│   │   ├── database.py     # Session and Engine setup
│   │   ├── schemas.py      # Pydantic models (DTOs)
│   │   └── check_db.py     # DB initialization utilities
│   ├── router/             # API route definitions
│   │   └── shortener_router.py
│   ├── service/            # Business logic layer
│   │   └── shortener_services.py
│   ├── utils/              # Helper functions and handlers
│   │   └── exceptionHandler.py
│   ├── requirements.txt    # Project dependencies
│   └── shortener.db        # SQLite database file
└── README.md
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.8+
- [Optional] Virtual environment (e.g., `my-env`)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Oriel_project/URL_shortener
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv my-env
   source my-env/bin/activate  # On Windows: my-env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## 🔌 API Endpoints

### 1. Health Check
`GET /health`
- **Description**: Checks if the API is running.
- **Response**: `{"status": "up"}`

### 2. Shorten URL
`POST /shorten`
- **Body**:
  ```json
  {
    "url": "https://www.example.com/very/long/path/to/resource"
  }
  ```
- **Response**: Returns the created short code and mapping.

### 3. Redirect
`GET /{short_code}`
- **Description**: Redirects the user to the original long URL.

### 4. Get Statistics
`GET /stats/{short_code}`
- **Description**: Retrieves click count and original URL details.
- **Response**:
  ```json
  {
    "original_url": "https://www.example.com/...",
    "short_code": "a1b2c3",
    "clicks": 42
  }
  ```

## 📝 License

This project is licensed under the MIT License.
