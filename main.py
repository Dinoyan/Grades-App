import base64
import pymongo
import db
from bson.binary import Binary
import pickle
import getpass

class Instructor():
	def __init__(self, name, ID, username, password):
		self.name = name
		self.ID = ID
		self.username = username
		self.password = base64.b64encode(password.encode("utf-8"))

	def __str__(self):
		return "Welcome " + self.name 


class Student():
	def __init__(self, name, stuID, username, password):
		self.name = name;
		self.ID = stuID;
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
		password = getpass.getpass('Password: ')
		# Check the type of user based on the ID
		if (len(str(ID)) >= 6):
			authenticated = db.authenticate(ID, password, "instructor")
			userType = "instructor"
		else:
			authenticated = db.authenticate(ID, password, "student")
			userType = "student"


	if(userType == "instructor"):

		print("Instructor menu\n")
		decision = input("Create User (1) | Update Mark (2) ")

		# Creating new accounts
		if (decision == "1"):

			print("Create a New Account\n")
			type = input("student or instructor: ")

			name = input("Name: ")
			ID = input("ID: ")
			username = input("Username: ")
			password = input("Password: ")

			if (type == "student"):
			
				student = Student(name, ID, username, password)
				
			elif (type == "instructor"):
			
				instructor = Instructor(name, ID, username, password)
		
			db.insertUser(student, type)
		else:
			
			print("Student menu\n")
			decision = input("view Marks (1) ")


