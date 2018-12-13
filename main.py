import base64
import pymongo
import db
from bson.binary import Binary
import pickle

class Instructor:
	def __init__(self, name, ID, username, password):
		self.name = name
		self.ID = ID
		sefl.username = username
		self.password = base64.b64encode(password.encode("utf-8"))

	def __str__():
		return "Welcome " + self.name 


class Student():
	def __init__(self, name, stuID, username, password):
		self.name = name;
		self.stuID = stuID;
		self.username = username
		self.password = base64.b64encode(password.encode("utf-8"))
		self.marksList = {}

	def __str__(self):
		return "Welcome " + self.name

	def viewMarks(self):
		for name, mark in self.marksList.items():
			print (name, "->", mark)


if __name__ =="__main__":
	print("Course Marks\n")

	authenticated = False
	while (!authenticated):
		ID = input("Enter ID: ")
		password = input("Enter password: ")
		# Check the type of user based on the ID
		authenticated = db.authenticate(ID, password, "blah")


	# Creating new accounts
	if(ID == "admin"):
		print("Create New Account\n")
		type = input("Student or Instructor: ")
		if (type == "Student"):
			name = input("Enter name: ")
			ID = input("Enter ID: ")
			username = input("Enter username: ")
			password = input("Enter password: ")
			student = Student(name, ID, username, password)

			db.insertStudentUser(student)
			
		elif (type == "Instructor"):
			name = input("Enter name: ")
			ID = input("Enter ID: ")
			username = input("Enter username: ")
			password = input("Enter password: ")
			instructor = Instructor(name, ID, username, password)

			db.insertInstructorUser(instructor)
	

	if (authenticated == True):
		pass



