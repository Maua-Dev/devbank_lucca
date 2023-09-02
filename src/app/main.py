from fastapi import FastAPI, HTTPException
from mangum import Mangum
from .environments import Environments
from .entities.item import to_dict

app = FastAPI()

repo = Environments.get_item_repo()()

@app.get("/items/get_all_items")

def get_all_users():
    users = repo.get_all_users()

    return users.to_dict()

@app.post("/items/")

def create_deposit():

    return

@app.post("/items/")

def create_withdraw():

    return

@app.get("/items")

def get_history():

    return



handler = Mangum(app, lifespan="off")




