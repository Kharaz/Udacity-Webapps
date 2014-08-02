from base import *
from passHash import *
import logging

class profileHandler(Handler):
	def render_page(self, response=""):
		userID = verify_hash(self.request.cookies.get('userID'))
		profData = db.GqlQuery("SELECT * FROM User WHERE userID = :1", int(userID)).get()

		self.render("profile.html", user = profData)

	def get(self):
		self.render_page()

	def post(self):
		html5text = self.request.get("htext")
		testForm = self.request.get("testform")

		if html5text:
			userID = int(verify_hash(self.request.cookies.get("userID")))
			profData = db.GqlQuery("SELECT * FROM User WHERE userID = :1", userID).get()
			profData.html5text = html5text
			profData.put()
		else:
			pass

		self.render_page()