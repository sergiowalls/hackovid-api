# hackovid-api

## Production setup

Create and fill a `.env` file in the same `docker-compose.yml` location with the following fields:

```
DEBUG=0
SECRET_KEY=
SQL_ENGINE=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=db
SQL_PORT=5432
DATABASE=
ADMIN_PASSWORD=
```

Also, create a `.env.db` file with:

```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```

## Developer setup

Inside the app folder run `pipenv install` to create the virtual environment with all the required dependencies.

Create a `.env` file with `DEBUG=1` to enable local development features.

Run `pipenv run migrate` to apply database migrations.

Execute `pipenv run server` to start the development server.