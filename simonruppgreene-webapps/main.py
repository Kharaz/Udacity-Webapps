#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

web_pages = ['form.txt','rot13.txt']
pages = {}

for i in web_pages:
    a = open(i)
    a = a.read()
    pages[i[0:i.index('.')]] = a

form = pages['form']
rot13pg = pages['rot13']



class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error":error,
                                        "month":escape_html(month),
                                        "day":escape_html(day),
                                        "year":escape_html(year)})
    
    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not(month and day and year):
            self.write_form("That doesn't look valid to me, friend.",
                            user_month, user_day, user_year)
        else:
            self.redirect('/thanks')


class ThanksHandler(webapp2.RequestHandler):
    
    def get(self):
        self.response.out.write("Thanks! Valid!")

class Rot13_Handler(webapp2.RequestHandler):

    def get(self):
        self.write_form()

    def write_form(self, text = ""):
        self.response.out.write(rot13pg % {"text":escape_html(text)})

    def post(self):
        user_text = self.request.get('text')

        self.write_form(rot13(user_text))

        
    

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler),
    ('/rot13', Rot13_Handler)
], debug=True)

months= ["January",
         "February",
         "March",
         "April",
         "May",
         "June",
         "July",
         "August",
         "September",
         "October",
         "November",
         "December"]


def rot13(text_in):
    pass

def valid_month(month):
    try:
        month_in = (month[0].upper() + month[1:].lower())
    except:
        return None
     
    if month_in in months:
        return month_in
    else:
        return None
    

def valid_day(day):
    if day.isdigit() and day:
        pass
    else:
        return None
       
    if int(day) > 0 and int(day) <= 31:
        return day
    else:
        return None


def valid_year(year):
    if year.isdigit() and year:
            if int(year) >= 1900 and int(year) <= 2025:
                return year
    return None


def escape_html(s):
    return cgi.escape(s, quote = True)
