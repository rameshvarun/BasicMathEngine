import cgi
import datetime
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp

handler = None

from function import *
from vector import *

from examples import *

handler = None

def show(val):
	handler.response.out.write("<br>" + str(val) + "<br>")

class Sandbox(webapp.RequestHandler):
	def get(self):
		self.render("")
		
	def post(self):
		ex = self.request.get('example')
		
		if ex:
			self.render(examples[int(ex)][1])
		else:
			self.render(self.request.get('command'))
		
	def render(self,command):
		global handler
		
		self.response.out.write('''
		<html>
		<head>
		<title>Sandbox</title>
		
		<script type="text/javascript">
		</script>
		
		</head>
		
		<body>
		<center>
		<h1>Sandbox</h1>
		</center>
		<br><br>
		Output:<br>
		''')
		
		handler = self
		

		lines = command.splitlines()
		
		for line in lines:
			exec(line)
		
		self.response.out.write('''
		<br><br>
		
		<form action="/sandbox" method="post">
			<div><textarea name="command" rows="10" cols="60">''' + command +'''</textarea></div>
			 <div><input type="submit" value="Evaluate"></div>
		</form>
		
		Or...
		
		<form action="/sandbox" method="post">
			<div>
			<select name="example" size="1">
			''')
			
		for x in range(len(examples)):
			self.response.out.write("<option value='" + str(x) + "'>" + examples[x][0] + "</option>")
			
		
		self.response.out.write('''
			</select>
			</div>
			<div><input type="submit" value="Try an example"></div>
		</form>
		
		<center>
		<br>
		Basic Math Engine Copyright 2010 Varun Ramesh
		<br><br>
		<a href="">About</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://varunramesh.net/">More Projects</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://randomperorations.blogspot.com/">Blog</a>
		<br><br>
		
		<img src="http://www.python.org/community/logos/python-powered-w-100x40.png" alt="Python Powered">
		<img src="http://code.google.com/appengine/images/appengine-silver-120x30.gif" alt="Powered by Google App Engine" />
		
		<style type="text/css"> 
		body
		{
			background-color:#bababa;
			background-image:url('images/textarea.png');
			background-repeat:repeat-x;
		}
		</style>
		
		</body></html>
		</center>
		''')

		
		
application = webapp.WSGIApplication([('/sandbox', Sandbox)], debug=True)
  
wsgiref.handlers.CGIHandler().run(application)