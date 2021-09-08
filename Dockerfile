FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

CMD "uvicorn", "runserver:app", "--host", "0.0.0.0", "--port", "9518"