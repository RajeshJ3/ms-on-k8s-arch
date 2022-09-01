from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return [
        {
            "id": 1,
            "title": "Sample Product 1"
        },
        {
            "id": 2,
            "title": "Sample Product 2"
        }
    ]
