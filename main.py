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
import jinja2
import os
import webapp2

jinja=jinja2.Environment(loader=jinja2.FileSystemLoader('pageFiles'))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = jinja.get_template('index.html')
        self.response.write(page.render())
class ContactHandler(webapp2.RequestHandler):
    def get(self):
        contact = jinja.get_template('contact.html')
        self.response.write(contact.render())
        
class ArtHandler(webapp2.RequestHandler):
    def get(self):
        art = jinja.get_template('art.html')
        self.response.write(art.render())
        
class ProgrammingHandler(webapp2.RequestHandler):
    def get(self):
        programming = jinja.get_template('programming.html')
        self.response.write(programming.render())
        
class ProfessionalHandler(webapp2.RequestHandler):
    def get(self):
        professional = jinja.get_template('professional.html')
        self.response.write(professional.render())
        

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/contact',ContactHandler),
    ('/art', ArtHandler),
    ('/programming',ProgrammingHandler),
    ('/professional', ProfessionalHandler)
], debug=True)
