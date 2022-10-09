# python external library
import uvicorn
from fastapi import FastAPI
# infrastructure
# presentation
from presentation.controller.AuthController import AuthController


app = FastAPI()



app.include_router(AuthController().router)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    # main: ファイル名、app: インスタンス名
    uvicorn.run('main:app', host=host, port=port, reload=True)