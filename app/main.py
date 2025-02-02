from fastapi import FastAPI

#Con Pydantic, además de definir la estructura y los tipos
#se validan automáticamente los datos que se envían al servidor
#si los datos no cumplen con el tipo se genera un erorr
from pydantic import BaseModel

# Instancia de la aplicación FastAPI
app = FastAPI()

# Definición de un modelo de datos utilizando Pydantic
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None



# Endpoint raíz (GET)
@app.get("/")
def read_root():
    return {"message": "¡Hola, esto es la ruta raiz jeff...!"}




# Endpoint para obtener un item por su ID (GET)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = "vacio"):
    """
    Este endpoint recibe un parámetro de ruta 'item_id' y un parámetro de consulta 'q' (opcional).
    """
    return {"id recibido": item_id, "q": q}




# Endpoint para crear un nuevo item (POST)
@app.post("/items/")
def create_item(item: Item):
    """
    Este endpoint recibe un JSON con la información de un item y lo devuelve.
    """
    return {
        "item_name": item.name,
        "price": item.price,
        "is_offer": item.is_offer
    }
