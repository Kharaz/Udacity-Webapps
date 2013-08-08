'''
Main application, ties everything together
'''

from handlers.base import *
from handlers.blogHandlers import *

app = webapp2.WSGIApplication([
        ('/blog', blogHandler),
        ('/blogPost', blogPostHandler),
        ('/testPage', testHandler)],
        debug = True)
                
            
