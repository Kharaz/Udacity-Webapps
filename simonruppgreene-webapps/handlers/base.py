'''
This file is for all base functions and general framework-laying
'''

import os
import webapp2
import jinja2
import re
import sys
import urllib2
from xml.dom import minidom
from datetime import date

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
        def write(self, *a, **kw):
            self.response.out.write(*a, **kw)

        def render_str(self, template, **params):
            t = jinja_env.get_template(template)
            return t.render(params)

        def render(self, template, **kw):
            self.write(self.render_str(template,**kw))

        def purge_user(self, username):
        	q = db.GqlQuery("SELECT * FROM User WHERE name =:1",username)
        	db.delete(q.fetch(1))


        
