from fastapi import FastAPI, HTTPException
from datetime import datetime

app = FastAPI()

db = [
    {"id": 1, "size": "small", "fuel": "electric", "price": 100},
    {"id": 2, "size": "medium", "fuel": "petrol", "price": 150},
    {"id": 3, "size": "large", "fuel": "diesel", "price": 200},
    {"id": 4, "size": "small", "fuel": "petrol", "price": 120},
]

# add get_cars(), serve at /api/cars, return the data

@app.get("/")
def welcome(name):
    return{"message": f"Welcome {name} to the project"}

@app.get("/date")
def date():
    return{"date": datetime.now()}

@app.get("/api/cars")
def get_cars(size: str = None) -> list:
    if size is None:
        return db
    return [data for data in db if data["size"] == size]

@app.get("/api/cars/{id}")
def get_cars(id: int = None) -> dict:
    result = [data for data in db if id == data["id"]]
    if result:
        return result[0]
    raise HTTPException(status_code=404, detail=f"Item {id} not found")

 