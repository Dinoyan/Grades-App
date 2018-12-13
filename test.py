import unittest
from db import authenticate

class AuthenticateTestCase(unittest.TestCase):

	def test_one(self):
		self.assertTrue(authenticate(123456, "dino", "instructor"))

	def test_two(self):
		self.assertTrue(authenticate(123458, "dino", "instructor"))

if __name__ == '__main__':
	unittest.main()