HospitalityClub v3
==================

HospitalityClub Alternate Project written in Django

Virtual Enviroment:
 
    virtualenv hc
    source hc/bin/activate
    
Install requirements

    pip install -r requirements.pip

Please don't forget to export your e-mail settings before running the project:

    export EMAIL_HOST=mail.youremailserver.com
    export EMAIL_PORT=587
    export EMAIL_HOST_USER=name@youremailserver.com
    export EMAIL_HOST_PASSWORD=youremailpassword
    export DEFAULT_FROM_EMAIL=youremailaddress
    
DB Settings:

Project is written for MySql for the initial process. You should create a db with root username called hc. After setting the DB, don't forget to syncdb.

    python manage.py syncdb

Run DEBUG project:
 
    python manage.py runserver


Before commiting and pushing the changes to git:

    python manage.py clean_pyc

http://localhost:8000/