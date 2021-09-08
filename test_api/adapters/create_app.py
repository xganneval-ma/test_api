from fastapi import FastAPI
import datetime
import asyncio
import logging
from .firstnames import FIRSTNAMES
from random import randrange, choice
from pydantic import BaseModel
from fastapi_utils.timing import add_timing_middleware

START_DATE = datetime.datetime(1900, 1, 1, 0, 0, 0, 0)
END_DATE = datetime.datetime.now()

GENDER = ["male", "female", "other"]
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
add_timing_middleware(app, record=logger.info, prefix="app", exclude="untimed")

class Person(BaseModel):
    first_name: str
    birthdate: datetime.datetime
    gender: str


def make_wait(func):
    async def _make_wait(count: int = 0, waiting_time: int = 0):
        start_time = datetime.datetime.now()
        result = await func(count=count)
        end_time = datetime.datetime.now()
        process_time = (end_time - start_time)
        to_wait = datetime.timedelta(milliseconds=waiting_time) - process_time
        await asyncio.sleep(to_wait.total_seconds())
        return result
    return _make_wait


def random_date(start: datetime.datetime, end: datetime.datetime):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


@app.get("/firstname")
@app.get("/test")
@make_wait
async def data(count: int = 0):
    return [
        Person(
            first_name=choice(FIRSTNAMES),
            birthdate=random_date(START_DATE, END_DATE),
            gender=choice(GENDER))
        for _ in range(count)
    ]
