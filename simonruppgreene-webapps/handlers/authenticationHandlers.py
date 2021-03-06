from base import *
from passHash import *
import re

class User(db.Model):
    name = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    email = db.StringProperty(required = False)
    created = db.DateTimeProperty(auto_now_add = True)
    userID = db.IntegerProperty(required = False)
    html5text = db.StringProperty(required = False)

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
			newUserId = db.GqlQuery("SELECT * FROM User").count()
			
			#make database entry for user
			u = User(name = user, password = make_pw_hash(user, pw), email = email, userID = newUserId)
			u.put()

			#set cookie for new user
			userID = make_hash(newUserId)
			self.response.headers.add_header("Set-Cookie", "userID=%s; Path=/" % userID)

			#redirect to welcome page (end goal is display the logged in user's name)
			self.redirect('/blog/welcome')

class loginHandler(Handler):
	def get(self):
		self.render("login.html")

	def post(self):
		user = self.request.get("userLog")
		pw = self.request.get("passLog")

		attempt_logged_user = db.GqlQuery("SELECT * FROM User WHERE name = :1", user)
		logUser = attempt_logged_user.get()
		userID = logUser.userID
		if valid_pw(user, pw, logUser.password):
			self.response.headers.add_header("Set-Cookie", "userID=%s; Path=/" % make_hash(userID))
			self.redirect("/blog/welcome", logUser.name)
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

class welcomeHandler(Handler):
    def get(self):
		user_id = verify_hash(self.request.cookies.get('userID')) #fetch cookie (id|hash) and verify
		current_user = db.GqlQuery("SELECT * FROM User WHERE userID = :1", int(user_id)).get()
		name = current_user.name
		if(current_user):
			self.render('welcome.html', user = name)
		else:
		    self.redirect('/blog/signup')
