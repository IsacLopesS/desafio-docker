FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
COPY desafio_northwind.py .

RUN pip install --no-cache-dir -r requirements.txt



CMD [ "python", "desafio_northwind.py" ]