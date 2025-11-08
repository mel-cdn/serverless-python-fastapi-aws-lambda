from fastapi import FastAPI

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "Welcome to FastAPI from AWS Lambda!",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "userId": user_id,
        "title": "Engr.",
        "firstName": "Bryce",
        "lastName": "Hernandez",
    }
