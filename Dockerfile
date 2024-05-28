FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py .
COPY app/ ./app/


EXPOSE 5000
ENV FLASK_APP=app.py
ENV SECRET_KEY=dioqu3980d32dnjc83
ENV MONGO_URI=mongodb://mongo:27017/

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]