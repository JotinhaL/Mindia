from fastapi import FastAPI

from app.api.routes.assessment import router as assessment_router

app = FastAPI(
    title="DASS-21 API",
    version="1.0.0",
    description="API para avaliação de estresse, ansiedade e depressão utilizando DASS-21."
)

app.include_router(assessment_router)


@app.get("/")
def root():
    return {"message": "API funcionando!"}