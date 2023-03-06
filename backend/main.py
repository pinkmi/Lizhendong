import uvicorn
from routers import users, upload
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

# 设置FastAPI对象
app = FastAPI()
# 挂载静态文件
app.mount("/static",
          StaticFiles(directory="static"),
          name="static")
# 实例化Jinja2对象，并将文件夹路径设置为以templates命令的文件夹
templates = Jinja2Templates(directory="templates")
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


# 设置根路由，当在web端输入访问的网址时可以直接跳转到编写好的页面中
@app.get("/")
async def homepage(request: Request):
    return templates.TemplateResponse(name='login.html',
                                      context={'request': request})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5500)
