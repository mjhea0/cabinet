# Cabinet

An application to manage Clients, Projects and Invoices made with Flask.

## Deploy project

	cd path/to/repository
	virtualenv env
	env/bin/pip install -r requirements.txt
	chmod a+x run.py
	chmod a+x db_create.py
	chmod a+x db_migrate.py
	chmod a+x db_upgrade.py
	chmod a+x db_downgrade.py
	./db_create.py

## Run application

	./run.py