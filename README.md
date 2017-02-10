### Flask + fullcalendar Sample
----------------------------
- install [python 2.7](https://www.python.org/downloads/)
- install [mysql](https://dev.mysql.com/downloads/)
- install [python-pip](https://pip.pypa.io/en/stable/installing/)
- create database

```sql
CREATE DATABASE mydatabase;
```

- create table

```sql
CREATE TABLE `my_schedule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL,
  `allDay` char(1) NOT NULL DEFAULT 'Y',
  PRIMARY KEY (`id`)
)
```

- clone project && move folder

```
$ git clone git@github.com:ParkMinKyu/scheduler.git
$ cd scheduler
```

- install [virtualenv](https://virtualenv.pypa.io/en/stable/)

```
$ sudo pip install virtualenv
```

- create virtualenv && activate

```
$ virtualenv envname
$ . envname/bin/activate
(envname) $
```

- install [flask](http://flask.pocoo.org/) && [pymysql](https://github.com/PyMySQL/PyMySQL)

```
(envname) $ pip install flask
(envname) $ pip install pymysql
```

- mysql info modify in dao/schedulerdao.py

```python
def getConnection():
    return pymysql.connect(host='localhost', user='root', password='123456', db='myintranet', charset='utf8')
```

- run application

```
(envname) $ python application.py
```

- [browser accept](http://localhost:5000)
