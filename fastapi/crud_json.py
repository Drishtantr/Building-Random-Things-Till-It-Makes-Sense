import json
from pathlib import Path
from typing import Dict

# Define the path to the JSON file
PIZZA_FILE_PATH = Path("pizza_orders.json")

def read_pizza_orders() -> Dict[int, dict]:
    if PIZZA_FILE_PATH.exists() and PIZZA_FILE_PATH.stat().st_size > 0:
        with open(PIZZA_FILE_PATH, "r") as file:
            try:
                return {int(k): v for k, v in json.load(file).items()}
            except json.JSONDecodeError:
                return {}
    return {}

def write_pizza_orders(pizza_orders: Dict[int, dict]):
    with open(PIZZA_FILE_PATH, "w") as file:
        json.dump(pizza_orders, file, indent=4)
