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
	studentSerialize = pickle.dumps(user)
	identifer = {}
	identifer[ID] = studentSerialize

	students.insert_one(identifer)

	

def usertInstructorUser(user):
	pass

def updateMarks(ID, name, mark):
	work = {}
	work[name] = mark


def authenticate(ID, password):
	authenticated = False

	return True



