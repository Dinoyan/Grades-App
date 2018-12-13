from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

students = mydb["students"]
instructors = mydb["instructors"]

def insertStudentUser(user):
	pass

def usertInstructorUser(user):
	pass

def updateMarks(ID, name, mark):
	work = {}
	work[name] = mark


def authenticate(ID, password):
	authenticated = False

	return True



