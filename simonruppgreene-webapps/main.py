'''
Main application, ties everything together
'''

from handlers.base import *
from handlers.blogHandlers import *
from handlers.asciiHandlers import *
from handlers.signupHandlers import *
from handlers.welcomeHandlers import *
from handlers.loginHandlers import *

app = webapp2.WSGIApplication([
        ('/blog', blogHandler),
        ('/blog/blogPost', blogPostHandler),
        ('/blog/signup', signupHandler),
        ('/blog/login', loginHandler),
        ('/blog/welcome', welcomeHandler),
        ('/ascii', asciiHandler),
        ('/testPage', testHandler)],
        debug = True)
                
            
