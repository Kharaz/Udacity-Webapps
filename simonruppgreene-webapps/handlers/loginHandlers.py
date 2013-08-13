from base import *

class loginHandler(Handler):
    def get(self):
        self.render("login.html")

    def post(self):
        pass
