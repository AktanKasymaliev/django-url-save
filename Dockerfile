FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
COPY ./django-entrypoint.sh ./
RUN chmod +x django-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./django-entrypoint.sh"]