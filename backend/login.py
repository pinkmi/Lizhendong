import uvicorn
# import pymysql
from routers import users, upload
# from db import add_user, is_exist
from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Access-Control-Allow-Origin",
                   "*", "http://127.0.0.1:5500/"]
)
app.include_router(users.router)
app.include_router(upload.router)


@app.get("/")
async def welcome(request: Request):
    return templates.TemplateResponse(name="login.html", context={"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5500)
