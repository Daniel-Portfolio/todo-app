FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py .
COPY app/ ./app/

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]