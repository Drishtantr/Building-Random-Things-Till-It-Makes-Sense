from fastapi import FastAPI, HTTPException
from datetime import datetime
from schemas import Car

app = FastAPI()

db = [
    {"id": 1, "size": "small", "fuel": "electric", "doors": 3, "transmission": "automatic"},
    {"id": 2, "size": "medium", "fuel": "gasoline", "doors": 4, "transmission": "manual"},
    {"id": 3, "size": "large", "fuel": "diesel", "doors": 5, "transmission": "automatic"},
    {"id": 4, "size": "small", "fuel": "electric", "doors": 3, "transmission": "automatic"},
    {"id": 5, "size": "medium", "fuel": "gasoline", "doors": 4, "transmission": "manual"},
    {"id": 6, "size": "large", "fuel": "diesel", "doors": 5, "transmission": "automatic"},
    {"id": 7, "size": "small", "fuel": "electric", "doors": 3, "transmission": "automatic"},
    {"id": 8, "size": "medium", "fuel": "gasoline", "doors": 4, "transmission": "manual"},
    {"id": 9, "size": "large", "fuel": "diesel", "doors": 5, "transmission": "automatic"},
    {"id": 10, "size": "small", "fuel": "electric", "doors": 3, "transmission": "automatic"},
    {"id": 11, "size": "medium", "fuel": "gasoline", "doors": 4, "transmission": "manual"},
    {"id": 12, "size": "large", "fuel": "diesel", "doors": 5, "transmission": "automatic"},
    {"id": 13, "size": "small", "fuel": "electric", "doors": 3, "transmission": "automatic"},
    {"id": 14, "size": "medium", "fuel": "gasoline", "doors": 4, "transmission": "manual"},
    {"id": 15, "size": "large", "fuel": "diesel", "doors": 5, "transmission": "automatic"},
    {"id": 16, "size": "small", "fuel": "electric", "doors": 3, "transmission": "automatic"},
    {"id": 17, "size": "medium", "fuel": "gasoline", "doors": 4, "transmission": "manual"},
    {"id": 18, "size": "large", "fuel": "diesel", "doors": 5, "transmission": "automatic"},
    {"id": 19, "size": "small", "fuel": "electric", "doors": 3, "transmission": "automatic"},
    {"id": 20, "size": "medium", "fuel": "gasoline", "doors": 4, "transmission": "manual"}

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

 