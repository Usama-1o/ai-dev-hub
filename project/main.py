from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Fake database
users = []

# Data model
class User(BaseModel):
    name: str
    email: str
    password: str

# Signup API
@app.post("/signup")
def signup(user: User):
    users.append(user)
    return {
        "message": "User signup successful",
        "total_users": len(users)
    }
