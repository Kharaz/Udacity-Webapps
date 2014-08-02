from base import *


class profileHandler(Handler):
	def render_page(self, response=""):
		user = self.request.cookies.get('user')
		profData = db.GqlQuery("SELECT * FROM User WHERE name = :1", user).get()
		#profData = db.GqlQuery("SELECT * FROM User WHERE name = :1", user)

		try:
			profData.html5text
		except:
			profData.html5text = "None"
			profData.put()


		self.render("profile.html", user = profData, response = response)

	def get(self):
		self.render_page()

	def post(self):
		html5text = self.request.get("html5text")
		response = self.request.get("response")

		if html5text:
			user = self.request.cookies.get("user")
			profData = db.GqlQuery("SELECT * FROM User WHERE name = :1", user).get()
			profData.html5text = html5text
			profData.put()
			print profData.html5text

		else:
			pass

		#self.render_page()

