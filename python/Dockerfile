FROM python:3.11-slim 

WORKDIR /usr/python 

COPY requirements/ requirements/ 

RUN pip install --no-cache-dir -r requirements/backend.in 

COPY . . 

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]