# Next.js + Django REST + PostgreSQL + Docker Showcase

[![GitHub Repo](https://img.shields.io/badge/GitHub-dtobby/nextjs--django--showcase-blue?logo=github)](https://github.com/dtobby/nextjs-django-showcase)

A full-stack application boilerplate demonstrating a decoupled architecture using Next.js for the frontend, Django REST framework for the backend API, PostgreSQL for the database, all containerized with Docker and orchestrated by Docker Compose. This project serves as a foundation for building modern web applications following microservice principles and exploring different Next.js rendering strategies.

**Purpose:** This repository is designed for learning and demonstrating how to integrate these popular technologies into a cohesive, containerized development environment.

## Core Technologies

*   **Frontend:** [Next.js](https://nextjs.org/) (v14+ with App Router) - React framework enabling Server-Side Rendering (SSR), Static Site Generation (SSG), Client-Side Rendering (CSR), etc.
*   **UI Styling:** [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework for rapid UI development.
*   **Backend:** [Django](https://www.djangoproject.com/) (v5+) - High-level Python web framework encouraging rapid development and clean, pragmatic design.
*   **API:** [Django REST Framework](https://www.django-rest-framework.org/) (DRF) - Powerful and flexible toolkit for building Web APIs on top of Django.
*   **Database:** [PostgreSQL](https://www.postgresql.org/) (v15+) - Robust, open-source object-relational database system known for reliability and features.
*   **Database Driver:** [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) - PostgreSQL adapter for Python (used by Django).
*   **Containerization:** [Docker](https://www.docker.com/) - Platform to build, ship, and run applications consistently in isolated environments called containers.
*   **Orchestration:** [Docker Compose](https://docs.docker.com/compose/) - Tool for defining and managing multi-container Docker applications using a YAML file.

## Architecture Overview

This project employs a microservice-inspired architecture where different concerns are handled by independent services running in separate Docker containers:

1.  **`frontend` Service:**
    *   **What:** Runs the Next.js application using its development server.
    *   **Responsibilities:** Handles user interface rendering, client-side logic, user interactions, and fetching data from the backend API.
    *   **Communication:** Makes HTTP requests to the `backend` service's API endpoints (internally via `http://backend:8000/api/...`).
    *   **Access:** Exposed on `http://localhost:3000` on the host machine for browser access.
2.  **`backend` Service:**
    *   **What:** Runs the Django application with Django REST Framework.
    *   **Responsibilities:** Provides a RESTful API, handles business logic, data validation, user authentication (if implemented), and interacts with the database.
    *   **Communication:** Listens for HTTP requests from the `frontend` (or other clients) and connects to the `db` service over the internal Docker network to query/modify data.
    *   **Access:** Exposed on `http://localhost:8000` on the host machine (e.g., for accessing the Django Admin at `/admin/` or API endpoints directly).
3.  **`db` Service:**
    *   **What:** Runs the PostgreSQL database server.
    *   **Responsibilities:** Stores application data persistently.
    *   **Communication:** Accepts database connections from the `backend` service on its internal port `5432`.
    *   **Access:** Port `5432` inside the container is mapped to `http://localhost:5433` on the host machine, allowing direct database access for debugging/management using tools like DBeaver, pgAdmin, etc.
    *   **Persistence:** Uses a Docker named volume (`postgres_data`) to ensure data is saved even if the container is stopped and removed.

![Basic Architecture Diagram (Conceptual)](https://via.placeholder.com/600x200.png?text=Browser+%3C-%3E+Frontend+(3000)+%3C-%3E+Backend+(8000)+%3C-%3E+DB+(5432))
*(**Note:** This is a placeholder. You can create and embed a real diagram here if desired.)*

## Directory Structure

nextjs-django-showcase/
├── backend/ # Django Backend Service Source Code & Config
│ ├── productBackendCore/ # Django project config (where settings.py lives)
│ │ ├── settings.py # Main Django settings (reads env vars for secrets/DB)
│ │ └── urls.py # Main Django URL routing (delegates to apps)
│ ├── products/ # Example Django app for managing products
│ │ ├── migrations/ # Database migration files (auto-generated)
│ │ ├── models.py # Defines database table structure (Product model)
│ │ ├── serializers.py # DRF serializers (convert Model <-> JSON)
│ │ ├── views.py # DRF API Views (request handling logic)
│ │ └── urls.py # App-specific URL routing for products API
│ ├── env/ # Python Virtual Environment (Gitignored) - Used ONLY for local (non-Docker) backend development
│ ├── .env # Local environment variables (Gitignored) - Used ONLY for local (non-Docker) backend development
│ ├── manage.py # Django's command-line utility
│ ├── requirements.txt # Python dependencies (for pip)
│ └── Dockerfile # Instructions to build the backend Docker image
├── frontend/ # Next.js Frontend Service Source Code & Config
│ ├── public/ # Static assets (images, fonts, etc.)
│ ├── src/ # Application source code (using Next.js App Router)
│ │ └── app/ # Core app directory (layouts, pages, components)
│ │ └── page.js # Example root page component
│ ├── node_modules/ # Node.js dependencies (Managed by npm, Gitignored)
│ ├── .next/ # Next.js build output and cache (Gitignored)
│ ├── next.config.mjs # Next.js configuration file
│ ├── package.json # Node.js project manifest (dependencies, scripts)
│ ├── tailwind.config.js # Tailwind CSS configuration
│ ├── postcss.config.js # PostCSS configuration (often used with Tailwind)
│ └── Dockerfile # Instructions to build the frontend Docker image
├── .gitignore # Specifies intentionally untracked files by Git (e.g., env/, node_modules/, .env, .next/)
├── docker-compose.yml # Docker Compose file: Defines services, networks, volumes, ports, environment variables for orchestration
└── README.md # This file: Project documentation


## Setup and Running (Docker Required)

**Prerequisites:**

*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Engine and Docker Compose) installed and running.
*   [Git](https://git-scm.com/) installed (for cloning).
*   A terminal or command prompt.

**Steps:**

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/dtobby/nextjs-django-showcase.git
    cd nextjs-django-showcase
    ```

2.  **Build and Start Containers:**
    This is the primary command to get everything running. It performs the following:
    *   Reads the `docker-compose.yml` file.
    *   Builds the Docker images for `frontend` and `backend` based on their respective `Dockerfile`s (if they aren't already built or if source files have changed).
    *   Pulls the `postgres:15-alpine` image if not present locally.
    *   Creates and starts containers for all three services (`db`, `backend`, `frontend`).
    *   Connects the containers to a shared Docker network.
    *   Runs the services in detached mode (`-d`), meaning they run in the background.

    ```bash
    docker compose up --build -d
    ```
    ***Note:*** *Allow a minute or two, especially on the first run, for images to download/build and for the PostgreSQL database inside the `db` container to fully initialize.* Check status with `docker ps`. The `db` container should eventually show `(healthy)`.

3.  **Apply Django Database Migrations:**
    Django needs to create the necessary tables in the database based on its models (including built-in ones for auth, admin, etc., and our `Product` model). This command executes the `migrate` command *inside* the already running `backend` container.
    ```bash
    docker compose exec backend python manage.py migrate
    ```
    *You only need to run `makemigrations` (see Development Workflow) if you change `models.py`, but `migrate` should always be run after starting the stack for the first time or after new migration files are created.*

4.  **(Optional but Recommended) Create a Django Superuser:**
    This allows you to log into the Django administration panel.
    ```bash
    docker compose exec backend python manage.py createsuperuser
    ```
    Follow the interactive prompts in your terminal to set a username, email (optional), and password.

5.  **Access the Running Services:**
    *   **Frontend Application:** `http://localhost:3000`
    *   **Backend Django Admin:** `http://localhost:8000/admin/` (Log in with the superuser credentials).
    *   **Backend API (Example):** `http://localhost:8000/api/products/` (Will be empty initially unless you add data via the admin or fixtures).
    *   **Database (Direct Connection via Client):**
        *   Host: `localhost`
        *   Port: `5433` (This is the host port mapped in `docker-compose.yml`)
        *   Database Name: `product_showcase_db`
        *   User: `product_user`
        *   Password: `product_password`
        *(These credentials are set as environment variables for the `db` service in `docker-compose.yml`).*

## Development Workflow

This setup is designed for an efficient development experience using Docker.

*   **Starting the Stack:** `docker compose up --build -d` (use `--build` if you modified `Dockerfile`s or dependencies).
*   **Hot Reloading / Live Changes:**
    *   **Why it Works:** The `volumes` sections in `docker-compose.yml` mount your local `frontend` and `backend` directories directly into the corresponding running containers (`./frontend:/app` and `./backend:/app`).
    *   **Frontend (Next.js):** Save changes to files inside `./frontend/src`. Next.js's Fast Refresh will automatically update the application in your browser at `http://localhost:3000` almost instantly.
    *   **Backend (Django):** Save changes to Python files inside `./backend`. The Django development server running inside the container will detect changes and automatically reload itself. You might need to refresh your browser/API client to see the effects on subsequent requests.
*   **Viewing Logs:** Essential for debugging.
    *   Tail logs from all services: `docker compose logs -f` (Press `Ctrl+C` to stop following).
    *   Tail logs for a specific service: `docker compose logs -f backend` or `docker compose logs -f frontend`.
    *   View past logs: `docker compose logs db`.
*   **Running Django `manage.py` Commands:** Since Django runs inside the `backend` container, use `docker compose exec` to run commands within it.
    ```bash
    # Example: Make migrations after changing models.py
    docker compose exec backend python manage.py makemigrations products

    # Example: Apply migrations
    docker compose exec backend python manage.py migrate

    # Example: Access Django shell
    docker compose exec backend python manage.py shell

    # Example: Run tests (if configured)
    docker compose exec backend python manage.py test
    ```
*   **Running `npm` or `npx` commands (Frontend):** Execute commands inside the `frontend` container.
    ```bash
    # Example: Install a new npm package
    docker compose exec frontend npm install <package-name>

    # Example: Run linting (if configured)
    docker compose exec frontend npm run lint
    ```
    *Note:* After installing new npm packages, you might need to stop (`docker compose down`) and restart (`docker compose up --build -d`) the stack to ensure the changes are fully incorporated, especially if the package has binary dependencies.
*   **Stopping Services:**
    ```bash
    docker compose down
    ```
    This stops and *removes* the containers, network, etc., defined in the compose file. **Your database data stored in the `postgres_data` volume will NOT be deleted.**
*   **Stopping and Removing Volumes (Use with Caution!):** To stop containers AND delete the named database volume (lose all data):
    ```bash
    docker compose down -v
    ```

## Key Configuration Points & Notes

*   **`docker-compose.yml`:** The central orchestration file. Defines how services are built (`build:`), how code/data is shared (`volumes:`), how services talk to each other (automatic Docker networking using service names like `db` and `backend`), how they are exposed (`ports:`), and crucially, how they are configured (`environment:`).
*   **Environment Variables:** This is the standard way to pass configuration (especially secrets) into containers. Django's `settings.py` is configured (`os.environ.get(...)`) to read the database credentials, `SECRET_KEY`, `DEBUG` status, and `CORS_ALLOWED_ORIGINS` from environment variables set in the `backend.environment` section of `docker-compose.yml`. **Avoid hardcoding secrets!**
*   **Dockerfiles (`backend/Dockerfile`, `frontend/Dockerfile`):** These define the steps to build the container images. Key steps include starting `FROM` a base image (Python, Node), copying dependency files (`requirements.txt`, `package.json`), installing dependencies (`pip install`, `npm install`), copying application code, and defining the default command (`CMD`) to run when the container starts. Caching is optimized by copying dependency files and installing them *before* copying the rest of the application code.
*   **Volumes:**
    *   **Bind Mounts (`./backend:/app`, `./frontend:/app`):** Essential for development. They directly link your local filesystem directories into the containers, enabling hot-reloading when you edit code locally.
    *   **Named Volume (`postgres_data:/var/lib/postgresql/data`):** Managed by Docker for persistent data storage. Ensures your database content survives container restarts and removals.
*   **Networking:** Docker Compose automatically creates a bridge network. Services can reach each other using their service name as a hostname (e.g., the Django backend connects to `DB_HOST=db` on the default PostgreSQL port `5432`).
*   **Ports:** The `ports:` section maps a `HOST:CONTAINER` port. `3000:3000` means traffic to port 3000 on your host machine (localhost) is forwarded to port 3000 inside the `frontend` container. `5433:5432` means traffic to port 5433 on your host is forwarded to port 5432 (the default Postgres port) inside the `db` container.
*   **CORS (`django-cors-headers`):** Cross-Origin Resource Sharing is needed because your frontend (`http://localhost:3000`) is on a different origin than your backend (`http://localhost:8000`). The `corsheaders` middleware and `CORS_ALLOWED_ORIGINS` setting in Django (configured via environment variable) allow the browser to permit requests from the frontend to the backend API.
*   **Local Development (`.env` file):** The `backend/.env` file and the `dotenv.load_dotenv()` code in `manage.py` are **only** needed if you choose to run the Django development server *directly on your host machine* (outside Docker) using its local virtual environment (`env`). In this specific scenario, you'd need `DB_HOST=localhost` and `DB_PORT=5433` in the `.env` file to connect to the database running inside Docker. **This `.env` file is ignored by Git and is NOT used when running via `docker compose up`.**

## Potential Next Steps

*   Build out CRUD (Create, Read, Update, Delete) API operations for Products in Django/DRF.
*   Create React components in Next.js to display, add, edit, and delete products by fetching data from the API.
*   Implement state management in Next.js (e.g., Zustand, Redux Toolkit, Context API).
*   Add user authentication and authorization (e.g., using DRF's built-in options, JWT, or libraries like `django-allauth`).
*   Write unit tests (Pytest for Django, Jest/React Testing Library for Next.js) and integration tests.
*   Configure Gunicorn or uWSGI in the `backend/Dockerfile`'s `CMD` for a production-ready WSGI server.
*   Optimize the `frontend/Dockerfile` using multi-stage builds for smaller production images.
*   Set up CI/CD pipelines (e.g., using GitHub Actions) to automate testing and deployment.
