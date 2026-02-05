# Mini CRM

A lightweight Customer Relationship Management (CRM) API built with Django and Django REST Framework.

## Features

- **Authentication**: User login handling.
- **Organizations**: Manage organization details.
- **Orders**: Create orders with dynamic price calculations (sizes, extras).
- **Admin Stats**: View simple revenue and order statistics.
- **Dockerized**: Ready to run with Docker and Docker Compose.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) (Recommended)
- OR Python 3.11+ installed locally.

## Installation & Running

### Option 1: Using Docker (Recommended)

This is the easiest way to run the project as it handles dependencies automatically.

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd mini_crm
    ```

2.  **Build and Run:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the API:**
    The server will start at `http://localhost:8000`.
    > **Note:** If the terminal shows `http://0.0.0.0:8000/`, do not click it. Use `http://localhost:8000/` instead.
    -   Health check: `http://localhost:8000/health/`
    -   API Root: `http://localhost:8000/api/`

### Option 2: Local Python Setup

1.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment:**
    Create a `.env` file in the root directory (same level as `manage.py`) with the following content:
    ```ini
    DEBUG=1
    SECRET_KEY=your-secret-key-here
    ALLOWED_HOSTS=*
    ```

4.  **Apply Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoints

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/health/` | System health check | No |
| `POST` | `/api/auth/login/` | User login | No |
| `GET` | `/api/organizations/` | List organizations | Yes |
| `POST` | `/api/organizations/` | Create organization | Yes |
| `POST` | `/api/orders/` | Create a new order | Yes |
| `GET` | `/api/admin/stats/` | View revenue stats | Yes (Admin) |

## Running Tests

To run the automated tests for pricing logic and services:

```bash
# If using Docker
docker-compose exec web python manage.py test

# If running locally
python manage.py test
```