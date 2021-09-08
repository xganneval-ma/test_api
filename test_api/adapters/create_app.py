from fastapi import FastAPI
import datetime
import asyncio
from logging import getLogger
from .firstnames import FIRSTNAMES
from random import randint, randrange, choice
from datetime import timedelta
from pydantic import BaseModel

START_DATE = datetime.datetime(1900, 1, 1 , 0, 0, 0, 0)
END_DATE = datetime.datetime.now()

GENDER = ["male", "female", "other"]

class Person(BaseModel):
    first_name: str
    birthdate: datetime.datetime
    gender: str


app = FastAPI()

logger = getLogger(__name__)



def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def get_person():
    first_name = choice(FIRSTNAMES)
    birthdate = random_date(START_DATE, END_DATE)
    gender = choice(GENDER)
    return Person(first_name=first_name, birthdate=birthdate, gender=gender)



@app.get("/firstname")
async def data(count: int=0, waiting_time: int=0):
    start_time = datetime.datetime.now()
    result = [get_person() for i in range(count)]
    end_time = datetime.datetime.now()
    process_time = (end_time - start_time)
    to_wait = datetime.timedelta(milliseconds=waiting_time) - process_time
    await asyncio.sleep(to_wait.total_seconds())
    return result
