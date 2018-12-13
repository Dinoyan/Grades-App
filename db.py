from pymongo import MongoClient
import pymongo
from bson.binary import Binary
import pickle
import db_client_info
import base64

myclient = db_client_info.myclient
mydb = myclient["grades"]

students = mydb["students"]
instructors = mydb["instructors"]

'''
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
'''

def insertUser(user, type):
	ID = user.ID

	userSerialized = pickle.dumps(user)
	identifer = {"_id" : ID, "user" : userSerialized}

	if (type == "Instructor"):
		instructors.insert_one(identifer)
	else:
		students.insert_one(identifer)


def updateMarks(ID, name, mark):
	work = {}
	work[name] = mark


def authenticate(ID, password, type):
	authenticated = False

	myquery = {"_id" : ID}

	# Query the col based on type

	if (type == "instructor"):
		
		myuser = instructors.find(myquery)

	else:
		
		myuser = students.find(myquery)

	for x in myuser:
			userObjSerialized = x.get("user")

	userObj = pickle.loads(userObjSerialized)

	accPass = base64.b64decode(userObj.password)

	if((accPass.decode("utf-8")) == password):
		authenticated = True

		
	return authenticated



