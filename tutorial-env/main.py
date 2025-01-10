from fastapi import FastAPI

app = FastAPI()

@app.get("/") # es un decorador, utilizamos un metodo http. En este caso la ruta del endpoint es un #
async def hello_world():
    return {"message": "Hello, World!"}
