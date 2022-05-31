import os
from typing import List
from fastapi import FastAPI
from mangum import Mangum
from models import User
from db import table

stage = os.environ.get("STAGE", "local")

app = FastAPI(
    title=f"Awesome API [{stage}]",
    root_path=None if stage == "local" else f"/{stage}"
    )


@app.post("/users", response_model=User)
def create_user(user: User):
    table.put_item(Item=user.dict())
    return user


@app.get("/users", response_model=List[User])
def list_users(limit: int = 100):
    response = table.scan(Limit=limit)
    return [User(**item) for item in response["Items"]]


@app.get("/")
def root():
    return {"message": "hello", "stage": stage}


handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
