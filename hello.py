from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

app = FastAPI()

@app.post("/login")
def login(user: User):
    return {"username": user.username}
