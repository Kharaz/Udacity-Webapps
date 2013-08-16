from base import *
from signupHandlers import valid_user, valid_password, valid_email
import time

class welcomeHandler(Handler):
    def get(self):
        user = self.request.get('user')

        if valid_user(user):
            self.render('welcome.html',user = user)

        else:
            self.redirect('/signup')
