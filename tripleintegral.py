
import cgi
import datetime
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp

handler = None

from function import *
from vector import *


def show(val):
	handler.response.out.write("<br>" + str(val) + "<br>")

class TripleIntegral(webapp.RequestHandler):
	def get(self):
		self.render("",'0','1','0','1','0','1')
		
	def post(self):
		self.render(self.request.get('command')
		,self.request.get('x1')
		,self.request.get('x2')
		,self.request.get('y1')
		,self.request.get('y2')
		,self.request.get('z1')
		,self.request.get('z2')
		)
		
	def render(self,equation,x1,x2,y1,y2,z1,z2):
		global handler
		
		self.response.out.write('''
		<html>
		<head>
		<title>Triple Integral</title>
		
		<script type="text/javascript">
		</script>
		
		</head>
		
		<body>
		<center>
		<h1>Triple Integral</h1>
		
		<br><br>
		Output:<br>
		''')
		
		handler = self
		
		if equation != "":
			
			
			
			
			step = 0.01
			
			sum = 0
			
			x = float(x1)
			
			while (x <= float(x2)):
			
				y = float(y1)
				while (y <= float(y2)):
					
					z = float(z1)
					while (z <= float(z2)):
						
						sum += eval(equation)*pow(step,3)
						
						z += step
					y += step
				x += step
			
			
			
			self.response.out.write(sum)
		
		self.response.out.write('''
		<br><br>
		
		<form action="/tp" method="post">
			<div>Equation: <textarea name="command">''' + equation +'''</textarea></div>
			<div>
			X Limits: <textarea name="x1">''' + x1 +'''</textarea> <textarea name="x2">''' + x2 +'''</textarea>
			</div>
			<div>
			Y Limits: <textarea name="y1">''' + y1 +'''</textarea> <textarea name="y2">''' + y2 +'''</textarea>
			</div>
			<div>
			Z Limits: <textarea name="z1">''' + z1 +'''</textarea> <textarea name="z2">''' + z2 +'''</textarea>
			</div>
			 <div><input type="submit" value="Evaluate"></div>
		</form>
	
		
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
		
		
application = webapp.WSGIApplication([('/tp', TripleIntegral)], debug=True)

wsgiref.handlers.CGIHandler().run(application)