import base64
import pymongo
import db
from bson.binary import Binary
import pickle

class Instructor:
	def __init__(self, name, ID, username, password):
		self.name = name
		self.ID = ID
		self.username = username
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
	userType = ""
	print("Course Marks\n")

	authenticated = False
	while (not authenticated):
		ID = input("ID: ")
		password = input("Password: ")
		# Check the type of user based on the ID
		if (len(str(ID)) >= 6):
			authenticated = db.authenticate(ID, password, "admin")
			userType = "admin"
		else:
			authenticated = db.authenticate(ID, password, "student")
			userType = "student"

	# Creating new accounts
	if(ID == "admin"):
		print("Create a New Account\n")
		type = input("Student or Instructor: ")
		if (type == "Student"):
			name = input("Name: ")
			ID = input("ID: ")
			username = input("Username: ")
			password = input("Password: ")
			student = Student(name, ID, username, password)

			db.insertStudentUser(student)
			
		elif (type == "Instructor"):
			name = input("Name: ")
			ID = input("ID: ")
			username = input("Username: ")
			password = input("Password: ")
			instructor = Instructor(name, ID, username, password)

			db.insertInstructorUser(instructor)
	
	



