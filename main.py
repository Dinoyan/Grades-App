import base64
import pymongo

class Instructor:
	def __init__(self, name, ID, username, password):
		self.name = name
		self.ID = ID
		sefl.username = username
		self.password = base64.b64encoder(password)

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
		self.password = password
		self.marksList = {}

	def viewMarks(self):
		for name, mark in self.marksList.items():
			print (name, "->", mark)



if __name__ =="__main__":
	print("Course Marks")
	username = raw_input("Enter username ")
	password = raw_input("Enter password ")

	if(username == "admin"):
		print("Create New Account")
		type = raw_input("Student or Instructor")

		if (type == "Student"):
			pass
		else:
			pass

