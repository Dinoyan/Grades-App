# Grades-App

A program where instructors can update students assignment marks and students can see it as soon as the innstructor updates them. 

## Getting Started

### Prerequisites

- Python 3.x

- PyMongo
```
$ pip3 install pymongo==3.4.0
```

- MongoDB
```
$ brew install mongodb
```


### Deployment

1) Clone this repo.

3) Start the Mongo daemon (local only)

```
$ mongod
```
To connect to the local mongoDB: Replace line 4 in db_client_info.py with the following
```
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
```

- Run the python main program.
```
$ python3 main.py
```

### Demo (through command line)

User login interface: <br/>
![login](https://i.imgur.com/slhDYLH.png)
<br/>
Student menu:
<br/>
![stu](https://i.imgur.com/3c22J3I.png)
<br/>
Instructor menu
<br/>
![ins](https://i.imgur.com/j3qgRVf.png)

### Features
- db.py: autoMarkCAssignment()
  https://github.com/Dinoyan/Auto-Mark
  
  
## Built With

* [PyMongo](https://api.mongodb.com/python/current/) - PyMongo DB
* Python



