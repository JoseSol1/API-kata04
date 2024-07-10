
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install kata04

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]