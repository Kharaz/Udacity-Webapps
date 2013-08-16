from base import *
from passHash import *

class loginHandler(Handler):
    def get(self):
        self.render("login.html")

    def post(self):
        user = self.request.get("userLog")
        pw = self.request.get("passLog")

        attempt_logged_user = db.GqlQuery("SELECT * FROM User WHERE name = :1", user)
        logUser = attempt_logged_user.get()
        if valid_pw(user, pw, logUser.password):
            self.redirect("/blog/welcome?user="+user)
        else:
            error = "Invalid Password"
            self.render("login.html", error = error)
            

        

class testLogin(Handler):
    def get(self):
        all_users = db.GqlQuery("SELECT * FROM User ORDER BY created DESC")
        self.render("loginTest.html", users = all_users)


    def post(self):
        user = self.request.get("user")

        self.purge_user(user)

        self.get()
