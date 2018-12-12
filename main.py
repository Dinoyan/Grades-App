import base64

class Instructor:
	def __init__(self, name, id, username, password):
		self.name = name
		self.id = id
		sefl.username = username
		self.password = base64.b64encoder(password)

	def enterMark(self):
		pass

	def updateMark(self, stuId, assigName, newMark):
		pass

	def viewMarks(self):
		pass


class Student():
	pass




if __name__ =="__main__":
	print("Course Marks")
	username = raw_input("Enter username ")
	password = raw_input("Enter password ")

	if(username == "admin"):
		pass



