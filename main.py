import base64
import pymongo
from db import *
from bson.binary import Binary
import pickle

class Instructor:
	def __init__(self, name, ID, username, password):
		self.name = name
		self.ID = ID
		sefl.username = username
		self.password = base64.b64encoder(password)

	def __str__():
		return "Welcome " + self.name 

	def enterMark(self):
		pass

	def updateMark(self, stuID, assigName, newMark):
		pass

	def viewMarks(self):
		pass


class Student():
	def __init__(self, name, stuID, username, password):
		self.name = name;
		self.stuID = stuID;
		self.username = username
		self.password = base64.b64encoder(password)
		self.marksList = {}

	def __str__(self):
		return "Welcome " + self.name

	def viewMarks(self):
		for name, mark in self.marksList.items():
			print (name, "->", mark)


if __name__ =="__main__":
	print("Course Marks\n")
	username = raw_input("Enter username ")
	password = raw_input("Enter password ")


	# Creating new accounts
	if(username == "admin"):
	print("Create New Account\n")
	type = raw_input("Student or Instructor")
	if (type == "Student"):
		name = raw_input("Enter name: ")
		ID = raw_input("Enter ID: ")
		username = raw_input("Enter username: ")
		password = raw_input("Enter password: ")
		Student = Student(name, ID, username, password)

		studentSerialize = pickle.dumps(Student)
		db.ininsertStudentUser(studentSerialize)
	else:
		pass


	auth = db.authenticate(username, password)

	if (auth == True):
		pass
	else:
		pass


