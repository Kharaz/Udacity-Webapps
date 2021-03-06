'''
Main application, ties everything together
'''

from handlers.base import *
from handlers.blogHandlers import *
from handlers.asciiHandlers import *
#from handlers.signupHandlers import *
#from handlers.welcomeHandlers import *
#from handlers.loginHandlers import *
from handlers.unityHandlers import *
from handlers.html5gameHandlers import *
from handlers.authenticationHandlers import *
from handlers.profileHandlers import *
from handlers.portfolioHandlers import *

app = webapp2.WSGIApplication([
        ('/blog', blogHandler),
        ('/blog/blogPost', blogPostHandler),
        ('/blog/signup', signupHandler),
        ('/blog/login', loginHandler),
        ('/blog/loginTest', testLogin),
        ('/blog/welcome', welcomeHandler),
        ('/ascii', asciiHandler),
        ('/testPage', testHandler),
        ('/unityfps', unityHandlerFPS),
        ('/unitytest', unityHandlerTest),
        ('/html5test', html5gameHandler),
        ('/html5test2', html5game2Handler),
        ('/jquery', jqueryHandler),
        ('/profile', profileHandler),
        ('/portfolio', portfolioHandler),
        ('/testCookies', testCookieHandler),
        ],
        debug = True)
                
            
