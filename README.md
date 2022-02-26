# Assaydashboard

A Dashboard application built using django and chart.js

## Configuring the database:
Just like any django project all the database connection `settings.py` file, you may directly add the database, host, user and password but it is recommended that you use the `mysql.cnf` file. 

1. Start by installing the sql dependencies
    ```
    apt-get install python3-dev default-libmysqlclient-dev build-essential
    ```
2. Install the python requirements 
    ```
    pip3 install -r requirements.txt
    ```
3. Edit the `mysql.cnf` file
    ```
    [client]
    database = assaydash
    host = hostip
    user = username
    password = password
    default-character-set = utf8
    ```
4. Optional:
    It is recommended that you create a new sql user specifically for this application with privialges only on the assaydash database.
    ```
    CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
    GRANT type_of_permission ON database_name.table_name TO 'username'@'localhost';
    FLUSH PRIVILEGES;
    ```
5. Now make sure the config file is read-only, otherwise mysql will ignore it
    ```
    chmod 0444 mysql.cnf
    ```
6. Now create the appropriate tables for the application to run properly
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
7. You also need to create an django Admin user for the application.
    ```
    python3 manage.py createsuperuser
    ```

## Deploying the app:

1. Configuring the allowed host
    In the 'djangobackend/settings.py` find 
    ```
    ALLOWED_HOSTS = []
    ``` 
    specify the domain and sub-domain for your website or the ip address. For more info chechout Django's [Deployment checklist](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#deployment-checklist)  

2. 