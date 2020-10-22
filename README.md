# This is a simple CRUD FLASK API

## For Running apps:

## Database Running:
    $ sudo docker-compose up -d

## APPLICATION Running:

- step 1: Make a virtual env
    $ python3 -m venv myenv
- step 2: Activate virtual environment
    $ source myenv/bin/activate
- step 3: Install requirements.txt
    $ pip install -r requirements.txt
- step 4: Connect to database container
    $ python app.py db init
    $ python app.py db migrate
    $ python app.py db upgrade
    $ python app.py runserver --host=0.0.0.0 --port=5000

# API's:

01. @app.route('/api/v1/insert', methods=['POST', 'GET'])
 - Take Json format data and added entry to the postgres database
02. @app.route('/api/v1/getall', methods=['GET'])
 - Return all the data in Json Format
03. @app.route('/api/v1/get/<name>', methods=['GET'])
 - Return data for given name in json format
04. @app.route('/api/v1/update/<name>', methods=['PUT', 'GET'])
 - take name as parameter for query which entry have to update and update data according given new Json format data
05. @app.route('/api/v1/delete/<name>', methods=['DELETE', 'GET'])
 - take name as parameter to delete the record in the database


## APP MAKING TODO:
 01. Installing Flask and other dependicies
 02. Making Api's for create, update, read, delete
 03. Making of the model for the database
 04. Set variable for database
 05. create a docker-compose file for creating POSTGRES docker container
 06. Dockerfile for the CRUD FLASK API

## Dependencies:
```
Flask==1.1.2
flask-marshmallow==0.14.0
Flask-Migrate==2.5.3
Flask-Script==2.0.6
Flask-SQLAlchemy==2.4.4
psycopg2-binary==2.8.6
```

 ## FAILED: [Will try to solve in future]
 01. make a docker-compose file for both app and db 
 02. connect them (I failed in this part)
 03. Make sure that full app is running on docker container.
   - Main issue why I failed:
        - migration command is not working between two container. 
        - Failed to connect app and db 
        (TCP/IP connections on port 5432?
        could not connect to server: Cannot assign requested address
	    Is the server running on host "localhost" (::1) and accepting
	    TCP/IP connections on port 5432?)