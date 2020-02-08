# Flask User API

This is a basic API which creates users in Postgres and can retrieve them too.

Its purpose is to test out a way of structuring a larger Flask application.


## Run

Setup the database and Flask application

```bash
docker run -e POSTGRES_USER=flask -e POSTGRES_PASSWORD=flask -e POSTGRES_DB=flask -p 5432:5432 postgres:latest
psql -h 127.0.0.1 -U flask < import.sql
python app.py
```

Then create some users

```bash
curl -H "Content-Type: application/json" -XPOST http://127.0.0.1:5005/user/ -d '{"username": "rflett", "email": "ryan@email.com", "age": 26}'
curl -H "Content-Type: application/json" -XPOST http://127.0.0.1:5005/user/ -d '{"username": "jturner", "email": "james@email.com", "age": 26, "city": "MEL"}'
```

and get them:

`curl http://127.0.0.1:5005/users/`

## Overview

The idea is to keep `app.py` (or `__init__.py` in some cases) small and tidy, so that it's easier to avoid circular imports.
As a result a lot of the 'extensions' that you add to the app are created in other modules and then imported and added later.

The database is setup in `Extensions/Database.py` so that it can be easily imported by Controllers and Models.

Custom errors are in `Extensions/Errors.py` which are then registered with an error handler in `app.py`.
As a result you can import these exceptions into other Controllers/Models etc. and raise them at any time, and 
Flask will catch them and return the appropriate response as defined in the Exception.

Finally, all of the routes are setup in the Controllers, which are then imported into the Apis. The api is then imported 
into `app.py` and added to the app.
