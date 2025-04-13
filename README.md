# Next.js + Django REST + PostgreSQL + Docker Showcase

A full-stack application boilerplate demonstrating a decoupled architecture using Next.js for the frontend, Django REST framework for the backend API, PostgreSQL for the database, all containerized with Docker and orchestrated by Docker Compose. This project serves as a foundation for building modern web applications following microservice principles.

## Core Technologies

*   **Frontend:** [Next.js](https://nextjs.org/) (v14+ with App Router) - React framework with various rendering capabilities.
*   **UI Styling:** [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework.
*   **Backend:** [Django](https://www.djangoproject.com/) (v5+) - Python web framework.
*   **API:** [Django REST Framework](https://www.django-rest-framework.org/) (DRF) - Toolkit for building Web APIs.
*   **Database:** [PostgreSQL](https://www.postgresql.org/) (v15+) - Powerful, open-source object-relational database system.
*   **Database Driver:** [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) - PostgreSQL adapter for Python.
*   **Containerization:** [Docker](https://www.docker.com/) - Platform for developing, shipping, and running applications in containers.
*   **Orchestration:** [Docker Compose](https://docs.docker.com/compose/) - Tool for defining and running multi-container Docker applications.

## Architecture Overview

This project follows a microservice-inspired architecture with distinct services running in separate Docker containers:

1.  **`frontend` Service:**
    *   Runs the Next.js development server.
    *   Handles user interface rendering and interactions.
    *   Communicates with the `backend` service via HTTP requests to its API endpoints (e.g., `http://backend:8000/api/...`).
    *   Accessible on `http://localhost:3000` on the host machine.
2.  **`backend` Service:**
    *   Runs the Django application using the development server (or Gunicorn/uWSGI in production setups).
    *   Provides a RESTful API using Django REST Framework.
    *   Handles business logic and data manipulation.
    *   Communicates with the `db` service over the internal Docker network.
    *   Accessible on `http://localhost:8000` on the host machine (e.g., for accessing the Django Admin at `/admin/`).
3.  **`db` Service:**
    *   Runs the PostgreSQL database server.
    *   Persists application data using a Docker named volume.
    *   Accessible *internally* to the `backend` service via hostname `db` on port `5432`.
    *   Exposed on `http://localhost:5433` on the host machine for direct database access/debugging with tools like DBeaver, pgAdmin, etc. (Connect using credentials defined in `docker-compose.yml`).

![Basic Architecture Diagram (Conceptual)](https://via.placeholder.com/600x200.png?text=Browser+<->+Frontend+(3000)+<->+Backend+(8000)+<->+DB+(5432))
*(Replace placeholder with a real diagram if desired)*

## Directory Structure
