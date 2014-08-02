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
            self.set_cookie('user',user)
            self.redirect("/blog/welcome')
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

class testCookieHandler(Handler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        
        visits = 0
        visit_cookie_str = self.request.cookies.get('visits')

        if(visit_cookie_str):
            cookie_val = verify_hash(visit_cookie_str)

            if cookie_val:
                visits = int(cookie_val)

        visits += 1
        new_cookie_val = make_hash(str(visits))

        self.response.headers.add_header('Set-Cookie', 'visits=%s' % new_cookie_val)

        self.write("You've been here %s times!" % visits)

        if(int(visits) % 10 == 0):
            self.write("\nYou've been here some multiple of 10! Have a cookie! (hah)")
