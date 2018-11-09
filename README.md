# Docker-Django-Webpack-React-Postgres (ddwrp) cookiecutter template

## Usage

### Install cookiecutter

```sh
$ mkvirtualenv cookiecutter
$ pip install cookiecutter
```

### Start your project

```sh
$ cookiecutter gh:kbairak/ddwrp-cookiecutter
project_name [ddwrp_project]:
first_django_app_name [ddwrp_app]:
secret_key [__SECRET__]:
$ deactivate
$ cd ddwrp_project
```

### Build docker images

```sh
$ docker-compose build
...
```

### Run the initial migrations

```sh
$ docker-compose run --rm django python manage.py migrate
...
```

### Start your docker containers

```sh
$ docker-compose up -d
ddwrp_project_db_1_454a13211a57 is up-to-date
Creating ddwrp_project_webpack_1_49eb6a2f06fc ... done
Creating ddwrp_project_django_1_7eacc8ec8968  ... done

```

### Test

Now if you navigate to `localhost:5000`, you should see 3 messages:

```
Hello from Django
Hello from JS
Hello from React
```

If you look into the template `django/<project>/<app>/templates/index.html`)
and the javascript code `webpack/src/index.js`), you should be able to
understand how these messages are being generated.


## How it works

There are 3 docker services:

- `django`: The main django application and webserver
- `webpack`: Runs `webpack --watch` to try to process javascript into bundles
- `db`: The PostgreSQL server

and 3 docker volumes:

- `django/`: The code that Django runs; changes that are made on the host
  machine will be picked up by the container
- `webpack/`: The code that the webpack container runs; changes that are made
  in the host machine will be picked up by webpack, this is also mounted on the
  Django container and served via the `{% static %}` templatetag
- `db/data`: The data folder of the Potgres container; you can delete its
  contents if you want to reset your database

## TODOs

- [x] Include source maps with webpack
- [ ] Hot loading for react components
- [ ] Add a bit of testing (both django and javascript)
- [ ] Add some CI
