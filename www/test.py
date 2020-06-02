import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    #对应schema.sql文件中的grant 权限列表 on 库.表 to 用户名@'ip' identified by "密码"一行内容
    await orm.create_pool(loop=loop, user='www-data',
                          password='password', db='awesome')
    u = User(name='Test62', email='test62@example.com', passwd='1234567890', image='about:blank')
    await u.save()

    #添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()