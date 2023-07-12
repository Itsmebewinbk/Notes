# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from pymongo import MongoClient
# def add(firstname: str | list | int, lastname: str=None):
#     return firstname + lastname


# app = FastAPI()
# conn = MongoClient("mongodb+srv://.1y5smmf.mongodb.net")


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}


# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     doc = conn.notes.notes.find_one({})
#     docs = conn.notes.notes.find({})
#     datas = []
#     for doc in docs:
#         datas.append({"id": doc["_id"], "notes": doc["notes"]})
#     return templates.TemplateResponse(
#         "index.html",
#         {"request": request, "datas": datas},
#     )
