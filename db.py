from pymongo import MongoClient
import pymongo
from bson.binary import Binary
import pickle

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

students = mydb["students"]
instructors = mydb["instructors"]

def insertStudentUser(user):
	ID = user.stuID
	studentSerialize = pickle.dumps(user)
	identifer = {}
	identifer[ID] = studentSerialize
	

def usertInstructorUser(user):
	pass

def updateMarks(ID, name, mark):
	work = {}
	work[name] = mark


def authenticate(ID, password):
	authenticated = False

	return True



