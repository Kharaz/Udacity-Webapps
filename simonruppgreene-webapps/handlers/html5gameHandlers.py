from base import *
from authenticationHandlers import *

class html5gameHandler(Handler):
    def get(self):
    	try:
            currentUserID = int(verify_hash(self.request.cookies.get("userID")))
            currentUser = db.GqlQuery("SELECT * FROM User WHERE userID = :1",currentUserID).get()
            html5text = str(currentUser.html5text)
        except:
            html5text = "no user: default string"
        
        self.render('/html5game/html5game.html', html5text = html5text)
        #self.write("html5text:" +html5text)
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
