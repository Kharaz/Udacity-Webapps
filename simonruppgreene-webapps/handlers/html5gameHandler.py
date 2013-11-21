from base import *
from signupHandlers import valid_user, valid_password, valid_email
import time

class html5gameHandler(Handler):
    def get(self):
        self.render('/html5game/html5game.html')
