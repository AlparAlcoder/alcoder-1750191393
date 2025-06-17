Desculpe, mas a pergunta pede para criar uma API em Node.js, mas as instruções especificam para criar uma API em Python usando FastAPI. Vou considerar que você solicitou uma API FastAPI e fornecer um exemplo de código para isso.


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float


items = {}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Read item by ID."""
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items/")
def create_item(item: Item):
    """Create an item."""
    if len(items) > 0:
        item_id = max(items.keys()) + 1
    else:
        item_id = 1
    items[item_id] = item
    return item

Este código define uma API FastAPI com dois endpoints. O primeiro endpoint é para obter um item pelo ID. O segundo endpoint é para criar um novo item. Os itens são armazenados em um dicionário em memória.