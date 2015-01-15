# Cabinet

An application to manage Clients, Projects and Invoices. Made with Flask.

## Quick Start

### Set Environment Variables

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
```

### Run the Application

```sh
$ python run.py
```

## TODO

1. Dashboard Calendar
1. Services and tasks
1. Date selection
1. Theme