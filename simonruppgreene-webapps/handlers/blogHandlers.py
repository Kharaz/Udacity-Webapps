'''
Handles all blog-related tasks
'''

from base import *

class blogHandler(Handler):
        def render_page(self):
            entries = db.GqlQuery("SELECT * FROM Entry ORDER BY created ASC ")
            
            self.render("blog.html", entries=entries)
        
        def get(self):
            self.render_page()

        def post(self):
                pass

class blogPostHandler(Handler):
        def render_page(self, title="", entry="", error=""):
            self.render("blogpost.html", title=title, entry=entry, error=error)

        def get(self):
            self.render_page()
    
        def post(self):
            title = self.request.get("title")
            content = self.request.get("entry")

            if title and content:
                e = Entry(title = title, content = content)
                e.put()

                self.redirect('/blog')
            else:
                error = "need title + content"
                self.render_page(title, entry, error)

class testHandler(Handler):
        def render_page(self):
                entries = db.GqlQuery("SELECT * FROM Entry ORDER BY created DESC")
                self.render("testPage.html", entries=entries)

        def get(self):
                self.render_page()

class Entry(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    date = db.DateProperty(auto_now_add = True)
    #date = date.strftime("%d/%m/%/y")
