from base import *

class html5gameHandler(Handler):
    def get(self):
        self.render('html5game/html5game2.html')

    def post():
    	pass

class jqueryHandler(Handler):
	def get(self):
		self.render("html5game/localjquery.js")
