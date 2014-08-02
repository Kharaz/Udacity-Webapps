from base import *
from signupHandlers import valid_user, valid_password, valid_email
import time

class welcomeHandler(Handler):
    def get(self):
        userID = self.request.cookies.get('user')
        userName = db.GqlQuery("SELECT * FROM User WHERE userID = :1", userID).get()

    	if(userID):
    		self.render('welcome.html',user = userName)

        else:
            self.redirect('/signup')
