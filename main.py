from fastapi import FastAPI

from zupython.core.controllers import importador_controller

app = FastAPI(
    title="ZUPython",
    description="Zupython API lhe mostrará os melhores artigos 📰"
)

app.include_router(importador_controller.router)


@app.get("/", include_in_schema=False)
def read_root() -> dict:
    return {"Bem": "Vindo(a)"}
