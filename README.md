# Cabinet

An application to manage invoicing. Made with Flask.

## Quick Start

### Set Environment Variables

Update the configuration settings in *config.py* and then run:

```sh
$ export APP_SETTINGS="project.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.config.ProductionConfig"
```

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```