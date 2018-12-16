from pymongo import MongoClient
import pymongo
from bson.binary import Binary
import pickle
import db_client_info
import base64
import subprocess
import os

myclient = db_client_info.myclient
mydb = myclient["grades"]

students = mydb["students"]
instructors = mydb["instructors"]


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
		print(userObj)
		authenticated = True

	return authenticated


def insertUser(user, type):
	ID = user.ID
	userSerialized = pickle.dumps(user)
	identifer = {"_id" : ID, "user" : userSerialized}

	if (type == "Instructor"):
		instructors.insert_one(identifer)
	else:
		students.insert_one(identifer)


def removeAStudent(ID):
	myquery = {"_id" : ID}
	students.delete_one(myquery)


def clearAllStudent():
	students.delete_many({})

'''
Function to complie and run C programs and output it 
to a .txt file. Then compare the output txt file with the solution.

Source: https://github.com/Dinoyan/Auto-Mark
'''
def autoMarkCAssignment(assignName):
	for file in os.listdir():
    if file.endswith(".c"):
        cmd = os.path.join(file)
        resultFile = cmd[:-2] + ".txt"
        subprocess.run(["gcc",cmd]) #For Compiling
        os.system("./a.out > " + resultFile)
        mark = subprocess.run(["cmp", resultFile, "solution.txt"])
        os.remove(resultFile)
        mark = mark.returncode
        if (mark == 0):
        	updateMarks(cmd[:-2], assignName, 100):
        else:
        	updateMarks(cmd[:-2], assignName, 0):


def updateMarks(ID, name, mark):
	myquery = {"_id" : ID}
	myuser = students.find(myquery)

	for x in myuser:
		userObjSerialized = x.get("user")

	try:
		stuObj = pickle.loads(userObjSerialized)
		stuObj.marksList[name] = mark
		stuObjSerialized = pickle.dumps(stuObj)
		updated = {"$set" : {"user" : stuObjSerialized}}
		students.update_one(myquery, updated)
	except UnboundLocalError:
		print("Invalid ID")
	else:
		print("updated Successfully\n")


def viewMarks(ID):
	myquery = {"_id" : ID}
	myuser = students.find(myquery)

	for x in myuser:
		userObjSerialized = x.get("user")

	stuObj = pickle.loads(userObjSerialized)
	marks = stuObj.marksList
	for name, mark in marks.items():
		print (name, "->", mark)


def getStudentInfo(ID):
	
	for student in students.find({"_id" : ID}):
		pass


def getAllMarks():
	pass


def getWorkAvg(workName):
	pass
