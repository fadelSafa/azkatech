# Vacation CRUD App

## Configuration
	- open settings.py
	- go to line 80, and configure database
	- go to mysql and create a new database that satisfies the name you added in the previous step

## Install Required Pacakges
	- sudo apt install mysql-server
	- pip install mysqlclient
	
## Setting up server: Run the following commands
	- [user@azkatech:~/azkatech]$pip install requirments.txt
	- [user@azkatech:~/azkatech]$python manage.py makemigrations my_app
	- [user@azkatech:~/azkatech]$python manage.py migrate
	- [user@azkatech:~/azkatech]$python manage.py createsuperuser

## Start Server
	- [user@azkatech:~/azkatech]$python manage.py runserver	
	
