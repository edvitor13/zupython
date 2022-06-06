from fastapi import FastAPI

from zupython.core.controllers import importador_controller

description = """
Zupython API lhe mostrará os melhores artigos 📰
"""

app = FastAPI(
    title="ZUPython",
    description=description
)

app.include_router(importador_controller.router)


@app.get("/", include_in_schema=False)
def read_root() -> dict:
    return {"Bem": "Vindo(a)"}
