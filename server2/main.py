from fastapi import FastAPI
from pydantic import BaseModel
import json

#dev db path
#DB_PATH = 'db/shopping_list.json'

#deployment db path 
DB_PATH = 'app/db/shopping_list.json'


def load_database() -> dict:
    """Load data from JSON file and return as dictionary"""
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(DB_PATH, 'w') as f:
            json.dumps([])
        
        with open(DB_PATH, "r") as f:
            return json.load(f)


def save_database(data: dict) -> None:
    """Save dictionary data to JSON file"""
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

app = FastAPI(title="Items API", version="1.0.0")

@app.get('/items/')
def get_items():
    data = load_database()
    return list(data)

@app.post('/items/')
def add_item(name: str, quantity: int):
    data = load_database()
    length = len(data)
    item_dict = {'name': name, 'quantity': quantity}
    item_dict.update({'id':length + 1})
    data.append(item_dict)
    save_database(data)
    n = item_dict['name']
    return {'message': f'item {n} added successfully'}



    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)