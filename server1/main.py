from fastapi import FastAPI

app = FastAPI()

@app.get('items/')
def get_items():
    pass

@app.post('items/')
def add_item():
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)