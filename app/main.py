from fastapi import FastAPI
from app.routers import tasks, auth

app = FastAPI(title="To-Do List API")

app.include_router(auth.router)
app.include_router(tasks.router)
