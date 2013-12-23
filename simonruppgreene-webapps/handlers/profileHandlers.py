from base import *


class profileHandler(Handler):
	def render_page(self):
		user = self.request.cookies.get('user')
		profData = db.GqlQuery("SELECT * FROM User WHERE name = :1", user).get()
		#profData = db.GqlQuery("SELECT * FROM User WHERE name = :1", user)
		self.render("profile.html", user = profData)

	def get(self):
		self.render_page()

	def post(self):
		self.set_cookie('user', None)
		self.render("DONT POST ON THIS DAWG")

