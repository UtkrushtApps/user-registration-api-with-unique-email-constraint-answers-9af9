# Solution Steps

1. 1. Create a new FastAPI project with a standard directory structure: place your main app code in the 'app' folder.

2. 2. Define SQLAlchemy models in app/models.py: create a User model with a unique constraint on the email column.

3. 3. Add Pydantic schemas (UserCreate and UserOut) in app/models.py for request validation and response serialization.

4. 4. Configure the PostgreSQL database connection and session maker in app/database.py, pulling credentials from environment variables.

5. 5. In app/main.py, initialize FastAPI, import models, and create the database schema automatically on startup with Base.metadata.create_all(bind=engine).

6. 6. Implement the POST /register endpoint in app/main.py: on duplicate email (IntegrityError), return a 400 error with a clear message.

7. 7. Implement the GET /users endpoint in app/main.py to list all registered users, using the UserOut schema for responses.

8. 8. Write a Dockerfile to containerize the API service, installing dependencies and running Uvicorn.

9. 9. Write a requirements.txt with FastAPI, Uvicorn, SQLAlchemy, psycopg2-binary (PostgreSQL driver), and pydantic.

10. 10. Write a docker-compose.yml that starts a PostgreSQL service and the FastAPI API service, with environment variables passed in and database volume persistence.

11. 11. Ensure that the 'users' table is created with a unique email constraint and API-side duplicate registration attempts return an appropriate error message.

