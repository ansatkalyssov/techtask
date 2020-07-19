## Technical Task


##### Navigate to the project directory and create virtual environment

```shell script
python -m venv venv
```

##### Activate it

```shell script
source venv/bin/activate
```  

##### Create Database 

```shell script
sqlite3 db.sqlite3
```

##### Exit from newly created database

```shell script
.exit
```

##### Install dependencies

```shell script
pip install -r requirements.txt
```

##### Migrate the Database

```shell script
python manage.py makemigrations core

python manage.py migrate
```

##### Running the Project

```shell script
python manage.py runserver
```