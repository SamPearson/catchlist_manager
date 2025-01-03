# Catchlist_manager
Simple webapp to catch thoughts for short-term storage with minimal categorization

# Running the app

The app can be run on a web server using gunicorn (assuming nginx is
configured to serve from the directory this app is in), or it can be run 
locally without a web server (locally the app should be served at 
127.0.0.1:8000 by default, but the actual URL will be output when you run
the app).

There are different commands to run the app locally vs on a server, shown
in the sections below.

## Locally/Dev
The following command will start the server locally

`$ python app.py`

## Server/Prod
The following command will start the server and bind it to domain/port

`gunicorn --config gunicorn_config.py --workers 3 --bind 127.0.0.1:5000 app:app`

The config file includes database initialization, app is the name of the 
app.py file as well as the flask instance defined therein, hence app:app

