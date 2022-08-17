# Django URL Saver
### Locally bringing up the project:
In the first, you sould clone rep:
* cloning repository:
```
git clone https://github.com/AktanKasymaliev/django-video-hosting.git
```
* Set and activate virtual enviroment:
```
python3 -m venv venv
. venv/bin/activate
```
* Install all requirements: 
```
pip install -r requirements.txt
```

* Create a file settings.ini on self project level, copy text from settings.ini_template, and add your value: 

* Enter in your postgresql, and create database:
```
sudo -u postgres psql
CREATE DATABASE <database name> owner <user>;
```

* Sync database with Django:
```
- python manage.py makemigrations
- python manage.py migrate
```

* Create superuser
```
- python manage.py createsuperuser
```

* And finally start project: `python manage.py runserver`

### Bring up the project with Docker:
* Create a file settings.ini on self project level, copy text from settings.ini_template, and add your value: 

( Don't forget that database's host it is docker's database service name )

* And finally start project: `docker-compose up --build`
