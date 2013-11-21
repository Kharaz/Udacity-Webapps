from base import *

class unityHandlerFPS(Handler):
	def render_page(self):
		self.render("unity/FPSExample.html")

	def get(self):
		self.render_page()

	def post(self):
		pass

class unityHandlerTest(Handler):
	def render_page(self):
		self.render("unity/Build1.html")

	def get(self):
		#self.render_page()
		self.render_page()

	def post(self):
		pass

