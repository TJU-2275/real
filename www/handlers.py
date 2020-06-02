from web_frame import get, post
from aiohttp import web
from models import User, Comment, Blog, next_id
import asyncio

__author__ = 'Michael Liao'

' url handlers '

@get('/blog')
async def handler_url_blog(request):
    return web.Response(body=b'<h1>Awesome: /blog</h1>', content_type='text/html', charset='UTF-8')

@get('/index')
async def handler_url_index(request):
    return web.Response(body=b'<h1>Awesome: /index</h1>', content_type='text/html', charset='UTF-8')

@get('/create_comment')
async def handler_url_create_comment(request):
    return web.Response(body=b'<h1>Awesome>: /create_comment</h1', content_type='text/html', charset='UTF-8')

@post('/result')
async def handler_url_result(request):
    body='<h1>您输入的邮箱是</h1>'
    return body

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }

