from fastapi import FastAPI
from routes.movimentos import movimento

app = FastAPI()
app.include_router(movimento)
