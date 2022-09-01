from fastapi import FastAPI

import requests

from helpers import get_domain
from config import (
    PRODUCTS,
    ORDERS
)

app = FastAPI()

@app.get("/")
def ping():
    return {"details": "ok"}

# Products
@app.get("/products")
def products():
    resp = requests.get(f"{get_domain(PRODUCTS)}/")
    return {"details": resp.json()}

# Orders
@app.get("/orders")
def orders():
    resp = requests.get(f"{get_domain(ORDERS)}/")
    return {"details": resp.json()}

@app.post("/orders")
def orders():
    resp = requests.post(f"{get_domain(ORDERS)}/")
    return {"details": resp.json()}

@app.patch("/orders/{pk}")
def orders(pk: str):
    resp = requests.patch(f"{get_domain(ORDERS)}/{pk}")
    return {"details": resp.json()}
