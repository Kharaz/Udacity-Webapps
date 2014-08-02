from base import *
from passHash import *
import re

class signupHandler(Handler):

    def get(self):
        self.render("signup.html")

    def post(self):
        have_error = False
        
        user = self.request.get("user")
        pw = self.request.get("pw")
        verify = self.request.get("verify")
        email= self.request.get("email")

        params = dict(user = user,
                      email = email)

        if not valid_user(user):
            params['error_user'] = "Invalid Username"
            have_error = True

        if not valid_password(pw):
            params['error_pw'] = "Invalid Password"
            have_error = True
        elif pw != verify:
            params['error_verify'] = "Passwords do not match"
            have_error = True

        if not valid_email(email):
            params['error_email'] = "Invalid Email"
            have_error = True

        if not check_available(user):
            params['error_user'] = "That name is already taken"
            have_error = True

        if have_error:
            self.render('signup.html', **params)
        else:
            newUserId = db.GqlQuery("SELECT COUNT FROM User").get()
            if(type(newUserId) == type(None)):
                newUserId = 0
            u = User(name = user, password = make_pw_hash(user, pw), email = email, userID = newUserId)
            u.put()

            self.response.headers.add_header('Set-Cookie','user=%i, Path=/' % newUserId)
            
            self.redirect('/blog/welcome')

class Welcome(Handler):
    def get(self):
        username = self.request.get('user')

        if valid_user(user):
            self.render('welcome.html',user = user)
        else:
            self.redirect('/signup')

class User(db.Model):
    name = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.StringProperty(required = False)
    created = db.DateTimeProperty(auto_now_add = True)
    userID = db.IntegerProperty()

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_user(user):
    return user and USER_RE.match(user)        
def valid_password(pw):
    return pw and PASS_RE.match(pw)
def valid_email(email):
    return not email or EMAIL_RE.match(email)

def check_available(user):
    q = db.GqlQuery("SELECT * FROM User WHERE name = :1", user)
    userquery = q.get()
    if not userquery:
        return True

