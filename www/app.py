
import logging; logging.basicConfig(level=logging.INFO)
#日志等级小于information将被忽略 debug info warning error critical
import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index) #若输入为/ 则处理index函数

    app_runner = web.AppRunner(app)
    await app_runner.setup()
    srv = await loop.create_server(app_runner.server, '127.0.0.1', 9000)
   #原教程写法 会报错 srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    #loop.create_server() 创建TCP服务
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

#day2代码提交