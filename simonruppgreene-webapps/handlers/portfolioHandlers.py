from base import *

class portfolioHandler(Handler):
	def render_page(self):
		self.render("portfolio.html")

	def get(self):
		self.render_page()

	def post(self):
		pass