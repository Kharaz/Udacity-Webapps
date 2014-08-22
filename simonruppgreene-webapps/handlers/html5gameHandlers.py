from base import *

class html5gameHandler(Handler):
    def get(self):
        self.render('html5game/html5game.html')

    def post():
    	pass

class html5game2Handler(Handler):
    def get(self):
        self.render('html5game/html5game2.html')

    def post():
    	pass

class jqueryHandler(Handler):
	def get(self):
		self.render("html5game/localjquery.js")

class Territory():
	def __init__(self, name="DefaultName"):
		self.name = name
		self.owner = None

	def ChangeOwner(self, newOwner):
		self.owner = newOwner