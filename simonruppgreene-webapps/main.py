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

form="""

<form method="post">
    What is your Birthday?
    <br>
    <label>
        Month
        <input type="text" name="month" value="%(month)s">
    </label>
    
    <label>
        Day
        <input type="text" name="day" value="%(day)s">
    </label>
    
    <label>
        Year
        <input type="text" name="year" value"%(year)s">
    </label>
    
    <div style="color: red">%(error)s</div>
    <br><br>
    
    <input type="submit">
</form>


"""



class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error":error,
                                        "month":month,
                                        "day":day,
                                        "year":year})
    
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
            self.response.out.write("Thanks! Valid!")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
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
                return int(year)

    
