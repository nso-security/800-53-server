import unittest
import sys
import os
import json

sys.path.append(os.path.join('lib'))
sys.path.append(os.path.join('data'))
from seccontrol import SecControl

class SecControlTest(unittest.TestCase):
	
	def test(self):
		self.assertTrue(True)

	def test_id(self):
		id = "AT-3"
		c = SecControl(id)
		self.assertTrue(id == c.id)

	def test_details(self):
		id = "AT-3"
		c = SecControl(id)
		self.assertTrue(c.title == "ROLE-BASED SECURITY TRAINING")

	def test_details_nonexistent_control(self):
		id = "AX-3"
		c = SecControl(id)
		self.assertTrue(c.title == "Error")		

	def test_responsible(self):
		# test "organization"
		id = "AT-3"
		c = SecControl(id)
		r = c.getResponsible()
		self.assertTrue(r == "organization")

		id = "AU-8"
		c = SecControl(id)
		r = c.getResponsible()
		self.assertTrue(r == "information system")

		# test "[Withdrawn"
		id = "SA-7"
		c = SecControl("SA-7")
		r = c.getResponsible()
		self.assertTrue(r == "withdrawn")

		# test for other (not organization, information system, or [Withdrawn)

if __name__ == "__main__":
	unittest.main()
