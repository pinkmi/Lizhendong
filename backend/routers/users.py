import matlab
import matlab.engine
from fastapi import APIRouter
# 实例化路由器
router = APIRouter()

# 使用router来声明请求方式&URL
@router.get("/1/{a}/{b}/{c}/{e}", tags=["users"])
async def ditong(a: float, b: float, 
                 c: float, e: float):
    # 开启Matlab服务
    eng = matlab.engine.start_matlab()
    # 调用Matlab中编写好的设计低通滤波器的函数
    ret = eng.ditong(matlab.double([a]), 
            matlab.double([b]), 
            matlab.double([c]), matlab.double([e]))
    print('前端数据是:', a, b, c, e)
    return a, b, c, e, ret

# 使用router来声明请求方式&URL
@router.get("/2/{a}/{b}/{c}/{d}/{e}/{f}", tags=["users"])
async def daizu(a: float, b: float, c: float, 
                d: float, e: float, f: float):
    # 开启Matlab服务
    eng1 = matlab.engine.start_matlab()
    # 调用Matlab中编写好的设计数字带阻滤波器的函数
    ret1 = eng1.daizu(matlab.double([a]), matlab.double([b]),
                      matlab.double([c]), matlab.double([d]),
                      matlab.double([e]), matlab.double([f]))
    print("前端数据是:", a, b, c, d, e, f, ret1)
    return a, b, c, d, f, e, f, ret1

@router.get("/sound/{name}", tags=["users"])
async def sound(name: str):
        file2 = "D:\\upload\\"+name
        eng2 = matlab.engine.start_matlab()
        ret2 = eng2.signal_processing(file2)
        print("处理的文件是:", ret2)
        return ret2

@router.get("/image/{name}", tags=["users"])
async def image(name:str):
        file3 = "D:\\upload\\"+name
        eng3 = matlab.engine.start_matlab()
        ret3 = eng3.image_processing(file3)
        print("处理的文件是:", ret3)
        return name