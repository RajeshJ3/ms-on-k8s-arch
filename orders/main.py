from fastapi import FastAPI

import pubsub
from connection import push

app = FastAPI()

@app.get("/")
def all_orders():
    return [
        {
            "id": 1,
            "title": "Order 1",
            "products": [1]
        },
        {
            "id": 2,
            "title": "Order 2",
            "products": [1, 2]
        }
    ]

@app.post("/")
def order():
    return {
        "id": 1,
        "title": "Order 1",
        "products": [1]
    }

@app.patch("/{pk}")
def order(pk: str):
    data = {
        "pk": pk,
        "status": "completed"
    }
    pubsub.publish(data, channel="orders")
    push(data, channel="invoice")
    return data
