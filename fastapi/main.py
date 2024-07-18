from typing import Union, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Pizza(BaseModel):
    name: str
    size: str
    toppings: list[str] = []

pizza_orders = {}
next_id = 1

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/pizzas/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.post("/pizzas/", response_model=Pizza)
def create_pizza(pizza: Pizza):
    global next_id
    pizza_orders[next_id] = pizza
    next_id += 1
    return pizza_orders[next_id - 1]

@app.get("/pizzas/{pizza_id}", response_model=Pizza)
def read_pizza(pizza_id: int):
    if pizza_id in pizza_orders:
        return pizza_orders[pizza_id]
    else:
        raise HTTPException(status_code=404, detail="Pizza not found")

@app.put("/pizzas/{pizza_id}", response_model=Pizza)
def update_pizza(pizza_id: int, pizza: Pizza):
    if pizza_id in pizza_orders:
        pizza_orders[pizza_id] = pizza
        return pizza_orders[pizza_id]
    else:
        raise HTTPException(status_code=404, detail="Pizza not found")

@app.delete("/pizzas/{pizza_id}", response_model=dict)
def delete_pizza(pizza_id: int):
    if pizza_id in pizza_orders:
        del pizza_orders[pizza_id]
        return {"detail": "Pizza deleted"}
    else:
        raise HTTPException(status_code=404, detail="Pizza not found")
