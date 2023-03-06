from fastapi import APIRouter
from db import add_user, is_exist
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi import Form, File, UploadFile

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.post("/", tags=["upload"])
async def login(request: Request, username=Form(...), password=Form(...)):
    dict = {"username": username, "password": password}
    res = is_exist(dict["username"], dict["password"])
    if res:
        return templates.TemplateResponse(name="homepage.html", context={"request": request})
    else:
        return templates.TemplateResponse(name="sign_up.html", context={"request": request})


@router.post("/sign_up", tags=["upload"])
async def sign_up(request: Request, username=Form(...), password=Form(...)):
    dict = {"username": username, "password": password}
    add_user(dict["username"], dict["password"])
    return templates.TemplateResponse(name="login.html", context={"request": request})


@router.post("/upload", tags=["upload"])
async def get_file(request: Request, filename: UploadFile = File(...)):
    contents = await filename.read()
    with open("D:\\upload\\" + filename.filename, "wb") as f:
        f.write(contents)
    name = filename.filename.split(".")[1]
    print(name)
    if name in ["jpg", "jpeg", "png"]:
        return templates.TemplateResponse(name="image.html",
                                          context={"request": request, "filename": filename.filename})
    elif name in ["wav", "mp3"]:
        return templates.TemplateResponse(name="sound.html",
                                          context={"request": request, "filename": filename.filename})


@router.post("/function", tags=["upload"])
async def function_select(request: Request, functions=Form(...)):
    json = {"functions": functions}
    if json["functions"] == "Filter Design":
        return templates.TemplateResponse(name="filter_design.html", context={"request": request})
    elif json["functions"] == "Image Processing":
        return templates.TemplateResponse(name="image.html", context={"request": request})
    elif json["functions"] == "Audio signal processing":
        return templates.TemplateResponse(name="sound.html", context={"request": request})
