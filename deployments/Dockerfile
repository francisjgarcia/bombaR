FROM python:3.12.0

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

COPY app .

RUN pip install -r requirements.txt

CMD [ "python", "-u", "app.py" ]
