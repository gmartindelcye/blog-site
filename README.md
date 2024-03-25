# blog-site

## Installation

1. create app dir

   ```bash
   mkdir blog-site
   ```

2. go to app dir

   ```bash
   cd blog-site
   ```

3. install virtual environment

   ```bash
   python3 -m venv .venv
   ```

4. Activate virtual environment

   ```bash
   source .venv/bin/activate
   ```

5. Initialize Git repository

   ```bash
   git init
   ```

6. Initialize pdm

   ```bash
   pdm init
   ```

7. Install dependencies

   - From zero

     ```bash
     pdm add fastapi uvicorn psycopg2-binary sqlmodel alembic python-jose
     ```

   - From `pyproject.toml`
     ```bash
     pdm install
     ```

## Setting Database using Docker and Docker-Compose

### docker-postgres-pgadmin

Create a postgresql-pgadmin container

#### Notes

This docker compose run inside a network with address 192.168.101.0/24.
If you want to change this address, you need to change the network address in docker-compose.yml.

### Instructions

1. Create permanent volumes routes:

   ```bash
   sudo mkdir -p pgsql/data
   sudo mkdir -p pgadmin/data
   ```

2. Change permissions to pgadmin directory in order to be accessed:

   ```bash
   sudo chown -R 5050:5050 pgadmin
   ```

3. Run docker compose:

   ```bash
   docker compose up -d
   ```

4. Access pgadmin in browser:

   ```bash
   https://localhost:5050
   ```

   or

   ```bash
   https://server_url:5050
   ```

5. Stop docker compose:

   ```bash
   docker compose down
   ```

### Data

_User pgadmin_: <admin@admin.com>

_Password pgadmin_: admin

#### Connection to DB

_Connect_: postgres container (suggestion, could be anything)
_database_: postgres
_user_: postgres
_password_: postgres
