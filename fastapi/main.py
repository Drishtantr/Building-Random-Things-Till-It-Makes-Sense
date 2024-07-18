from fastapi import FastAPI, HTTPException
from crud_json import read_pizza_orders, write_pizza_orders
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class Pizza(BaseModel):
    name: str
    size: str
    toppings: List[str] = []

# Initialize next_id
pizza_orders = read_pizza_orders()
next_id = max(pizza_orders.keys(), default=0) + 1

@app.post("/pizzas/", response_model=Pizza)
def create_pizza(pizza: Pizza):
    global next_id, pizza_orders
    pizza_orders[next_id] = pizza.dict()
    write_pizza_orders(pizza_orders)
    next_id += 1
    return pizza_orders[next_id - 1]

@app.get("/pizzas/{pizza_id}", response_model=Pizza)
def read_pizza(pizza_id: int):
    pizza_orders = read_pizza_orders()
    if pizza_id in pizza_orders:
        return pizza_orders[pizza_id]
    else:
        raise HTTPException(status_code=404, detail="Pizza not found")

@app.put("/pizzas/{pizza_id}", response_model=Pizza)
def update_pizza(pizza_id: int, pizza: Pizza):
    pizza_orders = read_pizza_orders()
    if pizza_id in pizza_orders:
        pizza_orders[pizza_id] = pizza.dict()
        write_pizza_orders(pizza_orders)
        return pizza_orders[pizza_id]
    else:
        raise HTTPException(status_code=404, detail="Pizza not found")

@app.delete("/pizzas/{pizza_id}", response_model=dict)
def delete_pizza(pizza_id: int):
    pizza_orders = read_pizza_orders()
    if pizza_id in pizza_orders:
        del pizza_orders[pizza_id]
        write_pizza_orders(pizza_orders)
        return {"detail": "Pizza deleted"}
    else:
        raise HTTPException(status_code=404, detail="Pizza not found")
