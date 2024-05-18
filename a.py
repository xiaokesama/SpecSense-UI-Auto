import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
async def index():
    return "456"


@app.api_route("/api/login", methods=('GET','POST','PUT'))
async def login(request: Request):
    form_data = await request.form()
    mobilephone = form_data.get('mobilephone')
    pwd = form_data.get('pwd')
    print('phone:{},pwd:{}'.format(mobilephone,pwd))
    if pwd == '123456':
        return {"code":"200","msg":"登录成功","id":2,
                'token_info':{'token':"tokenidzvzvzxvhgjfgs"}
                }
    return {"code":"10002","msg":"密码错误"}


@app.api_route("/api/register", methods=('GET','POST','PUT'))
async def register(request: Request):
    # 获取data数据
    form_data = await request.form()
    mobilephone = form_data.get('mobilephone')
    pwd = form_data.get('pwd')

    #获取url
    url = request.url

    # 获取headers
    headers = dict(request.headers)

    return {"code":"200","msg":"注册成功"}


@app.api_route("/menber/recharge", methods=('GET','POST','PUT'))
async def recharge():
    return {"code":"200","msg":"充值成功",
            "data":{
                'token':"tokenidzvzvzxvhgjfgs",
                'id': 1
            }}


@app.api_route("/loan/add", methods=('GET','POST','PUT'))
async def add():
    return {"code":"0","msg":"OK",
            "data":{
                'token':"tokenidzvzvzxvhgjfgs",
                'id': 1,
            }}


@app.api_route("/loan/invest", methods=('GET','POST','PUT'))
async def addad(request: Request):
    form_data = await request.form()
    print("form_data:{}".format(form_data))
    return {"code":"0","msg":"OK","data":{"normal_mobile_phone":form_data.get('mobilephone')}}


if __name__ == '__main__':
    uvicorn.run(app)