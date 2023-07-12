from fastapi import APIRouter, FastAPI, Request
from models.note import Note
from config.db import connection
from schema.notes import notes, note
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
note_routes = APIRouter()

note_routes.mount("/static", StaticFiles(directory="static"), name="static")
@note_routes.get("/", response_class=HTMLResponse)
async def get_notes(request: Request):
    docs = connection.notes.notes.find({})
    datas = []
    for doc in docs:
        datas.append(
            {
                "id": doc["_id"],
                "title": doc.get("title"),
                "description": doc.get("description"),
                "important": doc.get("important"),
            }
        )
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "datas": datas},
    )

@note_routes.post("/")
async def create_notes(request: Request):
    form = await request.form()
    dictform = dict(form)
    dictform["important"] = True if dictform.get("important") else False
    connection.notes.notes.insert_one(dictform)

    docs = connection.notes.notes.find({})
    datas = []
    for doc in docs:
        datas.append(
            {
                "id": doc["_id"],
                "title": doc.get("title"),
                "description": doc.get("description"),
                "important": doc.get("important"),
            }
        )

    success_message = "Note created successfully!"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "datas": datas,
            "success_message": success_message,
        },
    )
