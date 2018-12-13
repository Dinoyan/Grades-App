from pymongo import MongoClient
import pymongo
from bson.binary import Binary
import pickle
import db_client_info

myclient = db_client_info.myclient
mydb = myclient["grades"]

students = mydb["students"]
instructors = mydb["instructors"]


def insertStudentUser(user):
	ID = user.stuID
	studentSerialized = pickle.dumps(user)
	identifer = {}
	identifer[ID] = studentSerialized

	students.insert_one(identifer)


def insertInstructorUser(user):
	ID = user.ID
	InstructorSerialized = pickle.dumps(user)
	identifer = {"_id" : ID, "user" : InstructorSerialized}
	
	instructors.insert_one(identifer)


def updateMarks(ID, name, mark):
	work = {}
	work[name] = mark


def authenticate(ID, password, type):
	authenticated = False

	# Query the col based on type

	if (ID == "admind"):
		authenticated = True
	else:
		myquery = {"_id" : ID}

		myuser = instructors.find(myquery)

		for x in myuser:
			print(x.get("user"))


	return authenticated



