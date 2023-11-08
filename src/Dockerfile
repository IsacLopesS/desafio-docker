FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY desafio_northwind.py .

CMD [ "python", "desafio_northwind.py" ]