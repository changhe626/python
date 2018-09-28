import aiomysql as aiomysql
import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

def index(request):
    #return web.Response(body=b'<h1>answer</h1>')
    return web.Response(body="<h1>hello world</h1>")

@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route("GET","/",index)
    srv=yield from loop.create_server(app.make_handler(),"127.0.0.1",9000)
    logging.info("server started at http://127.0.0.1:9000...")
    return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


"""
所以，我们要首先把常用的SELECT、INSERT、UPDATE和DELETE操作用函数封装起来。

由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步IO操作，因为所有用户都是由一个线程服务的，协程的执行速度必须非常快，才能处理大量用户的请求。而耗时的IO操作不能在协程中以同步的方式调用，否则，等待一个IO操作时，系统无法响应任何其他用户。

这就是异步编程的一个原则：一旦决定使用异步，则系统每一层都必须是异步，“开弓没有回头箭”。

幸运的是aiomysql为MySQL数据库提供了异步IO的驱动。
"""

@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global  __pool
    __pool=yield from aiomysql.create_pool(
        host=kw.get("host","localhost"),
        port=kw.get("port",3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )



"""
SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。
注意要始终坚持使用带参数的SQL，而不是自己拼接SQL字符串，这样可以防止SQL注入攻击。

注意到yield from将调用一个子协程（也就是在一个协程中调用另一个协程）
并直接获得子协程的返回结果。
"""

@asyncio.coroutine
def select(sql,args,size=None):
    logging.log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur=yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace("?","%s"),args or ())
        if size:
            rs=yield from cur.fetchmany(size)
        else:
            rs=yield from cur.fetchall()
        yield from cur.close
        logging.info('rows returned: %s' % len(rs))
        return rs


@asyncio.coroutine
def execute(sql, args):
    logging.log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected




