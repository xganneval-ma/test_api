import aiohttp
import random
import asyncio
import datetime

SENARIOS = [
    [[100, 100]] * 5,
    # [[80, 50]] * 5,
    # [[50, 70]] * 5,
]

URL = "http://localhost:9518/firstname?waiting_time=%s&count=%s"
CONCURENCY = 100
async def get_data(waiting_time: int, count: int):
    async with aiohttp.ClientSession() as session:
        print(URL % (waiting_time, count))
        async with session.get(URL % (waiting_time, count)) as resp:
            return await resp.json()

async def execute_senarios():
    start_time = datetime.datetime.now()
    for senario in SENARIOS:
        print("Starting %s" % senario)
        results = await asyncio.gather(
            *[
                get_data(senari[0], senari[1])
                for senari in senario
            ]
        )
    total_time = datetime.datetime.now() - start_time
    print(total_time.total_seconds())

asyncio.run(execute_senarios())