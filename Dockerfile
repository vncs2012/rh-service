#################################################################################
FROM python:3.9.9

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DJANGO_SETTINGS_MODULE=RETHI.settings \
    PORT=8000 \
    WEB_CONCURRENCY=3

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential curl \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy project code
COPY . .

RUN python manage.py collectstatic
RUN python manage.py collectstatic  --noinput
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput

# Run as non-root user
RUN chown -R django:django /app
USER django

# Run application
CMD gunicorn RETHI.wsgi:application