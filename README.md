# Python_SQLAlchemy_Sample
Sample Code for Python [SQLAlchemy](https://www.sqlalchemy.org/) ORM

```
pip install sqlalchemy
```

After installation, Check the version of SQLAlchemy:
```
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
```
and then if you want to use MySql use pymysql module:
```
pip install pymysql
```


```
import sqlalchemy as db

engine = db.create_engine('mysql+pymysql://username:password@host/database_name')
conn = engine.connect()
```
