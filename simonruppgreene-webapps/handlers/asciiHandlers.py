#asciiChan handler

from base import *

class asciiHandler(Handler):
        def render_page(self, title="", art="", error=""):
            arts = db.GqlQuery("SELECT * FROM Art ORDER BY created DESC ")
            
            self.render("ascii.html", title=title, art=art, error=error, arts = arts)
        
        def get(self):
            self.render_page()

        def post(self):
            title = self.request.get("title")
            art = self.request.get("art")

            if title and art:
                a = Art(title = title, art = art)
                a.put()

                self.redirect('/ascii')
            else:
                error = "need title + art"
                self.render_page( title, art, error )

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
