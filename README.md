# web-crawler

A Django web app that has one text input field, and a "go" button.
The field accepts a URL of a web page (for example https://en.wikipedia.org/wiki/Django_(web_framework)).

After you click the "go" button, the app crawls all the URLs in the given webpage and displays to the customer
a complete list of all the URLs the crawler found, including **nested links**.

# How to run

## Quickstart: Run locally via Docker

The fastest way to run the app is to run it in using Docker-compose. This should be enough for quickstart:

``` bash
git clone https://github.com/rayman1104/web-crawler
cd web-crawler
```

If you want just to run all the things locally, you can use Docker-compose which will start all containers for you. This approach is similar to Production deployment using Dokku but not recommended for production.

#### Create .env file

Specify important environment variables in .env which should be located in root directory of repo (make sure to fork our repo and don't publish your tokens to public).
```
DJANGO_DEBUG=True
DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
```

#### Docker-compose

To run all services (Django, Redis, Celery) at once:

```
docker-compose up --build
```

## Deploy

Deploy to production is done via [Dokku](https://dokku.com/). Dokku is an open-source version of Heroku.
