# coding=utf-8

import asyncio
import aiomysql

loop = asyncio.get_event_loop()

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'test',
    'charset': 'utf8mb4',
    'loop': loop,
}

@asyncio.coroutine
def test():
    conn = yield from aiomysql.connect(**db_config)
    cur = yield from conn.cursor()
    yield from cur.execute("select host,user from mysql.user")
    print(cur.description)
    r = yield from cur.fetchall()
    print(r)
    yield from cur.close()
    conn.close()


# 测试存储过程
async def test_procedure():
    conn = await aiomysql.connect(**db_config)

    async with conn.cursor() as cur:
        await cur.execute('drop procedure if exists myinc;')
        await cur.execute("""create procedure myinc(p1 int)
                             begin
                                 select p1 + 1;
                             end""")
        await cur.callproc('myinc', [1])
        (ret, ) = await cur.fetchone()
        assert 2, ret
        print(ret)
    conn.close()


# 测试批量插入
async def test_executemany():
    conn = await aiomysql.connect(**db_config)

    cur = await conn.cursor()
    async with conn.cursor() as cur:
        await cur.execute("drop table if exists music_style;")
        await cur.execute("""create table music_style (id int, name varchar(255), primary key (id));""")
        await conn.commit()

        # insert 3 rows one by one
        await cur.execute("insert into music_style values(1,'heavy metal')")
        await cur.execute("insert into music_style values(2,'death metal');")
        await cur.execute("insert into music_style values(3,'power metal');")
        await conn.commit()

        # insert 3 row by one long query using *executemane* method
        data = [(4, 'gothic metal'), (5, 'doom metal'), (6, 'post metal')]
        await cur.executemany("insert into music_style (id, name) values (%s,%s)", data)
        await conn.commit()

        # fetch all insert row from table music_style
        await cur.execute("select * from music_style;")
        result = await cur.fetchall()
        print(result)
    conn.close()


# 测试事务
async def test_transaction():
    conn = await aiomysql.connect(**db_config)

    async with conn.cursor() as cursor:
        stmt_drop = "drop table if exists names"
        await cursor.execute(stmt_drop)
        await cursor.execute("""create table names (id int primary key auto_increment, name varchar(10))""")
        await conn.commit()

        names = (('Geert',), ('Jan',), ('Michel',))
        stmt_insert = "insert into names (name) values (%s)"
        await cursor.executemany(stmt_insert, names)

        await conn.rollback()

        stmt_select = "select id, name from names order by id"
        await cursor.execute(stmt_select)
        resp = await cursor.fetchall()
        assert not resp

        await cursor.executemany(stmt_insert, names)

        await cursor.execute(stmt_select)
        resp = await cursor.fetchall()
        print(resp)

        await conn.commit()

        await cursor.execute(stmt_select)
        print(resp)

        await cursor.execute(stmt_drop)
        await cursor.close()
        conn.close()


# 测试连接池
async def test_connection_pool():
    pool = await aiomysql.create_pool(**db_config)
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("select name from music_style")
            print(cur.description)
            (r,) = await cur.fetchone()
            assert r == 'heavy metal'
    pool.close()
    await pool.wait_closed()

loop.run_until_complete(test())
loop.run_until_complete(test_procedure())
loop.run_until_complete(test_executemany())
loop.run_until_complete(test_transaction())
loop.run_until_complete(test_connection_pool())
