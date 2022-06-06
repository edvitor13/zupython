from fastapi import FastAPI

from zupython.core.controllers import importador_controller


app = FastAPI()

app.include_router(importador_controller.router)


@app.get("/", include_in_schema=False)
def read_root() -> dict:
    return {"Bem": "Vindo(a)"}
