from base import *
#from signupHandlers import valid_user, valid_password, valid_email
from authenticationHandlers import *
import time

class html5gameHandler(Handler):
    def get(self):
    	currentUserID = int(verify_hash(self.request.cookies.get("userID")))
    	currentUser = db.GqlQuery("SELECT * FROM User WHERE userID = :1",currentUserID).get()
    	html5text = currentUser.html5text
        self.render('/html5game/html5game.html'. html5text = html5text)
