from fastapi import FastAPI

app = FastAPI(
    title="Lab9 - Pipeline CI/CD",
    description="API para atividade de CI/CD",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "mensagem": "API Lab9 funcionando!",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }