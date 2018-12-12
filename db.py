import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

students = mydb["students"]
instructors = mydb["instructors"]



