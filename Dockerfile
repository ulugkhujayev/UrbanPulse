FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE config.settings

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    postgresql-client

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]