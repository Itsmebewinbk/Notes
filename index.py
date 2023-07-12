from fastapi import FastAPI
from routes.notes import note_routes

app = FastAPI()
app.include_router(note_routes)
