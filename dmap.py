
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

from math import *

def show(val):
	handler.response.out.write("<br>" + str(val) + "<br>")
		
		
class DMap(webapp.RequestHandler):
	def get(self):
		self.render("x*x + y*y")
		
	def post(self):
		self.render(self.request.get('command')
		)
		
	def render(self,equation):
		global handler
		
		self.response.out.write('''
		<html>
		<head>
		<title>Density Map Grapher</title>
		
		<script type="text/javascript" src="script/pnglib.js">
		</script>
		
		</head>
		
		<body>
		<center>
		<h1>Density Map Grapher</h1>
		
		<br><br>
		Output:<br>
		''')
		
		handler = self
		
		self.response.out.write('''
		<script type="text/javascript">
		
		var p = new PNGlib(200, 200, 256);
		var background = p.color(0, 0, 0, 0);
		
		''');
		
		
		
		if equation != "":
			self.response.out.write('''
			
			var x1 = 0;
			var y1 = 0;
			for (x1 = 0; x1 < 200; x1++)
			{
				for (y1 = 0; y1 < 200; y1++)
				{
					x = (x1 - 100)*0.1
					y = (y1 - 100)*0.1
					
					value = ''' + equation + '''
					
					if(value < 255 && value > -255)
					{
						if(value >= 0)
						{
							p.buffer[p.index(x1 , y1)] = p.color(value,value,value,255);
						}
						else
						{
							p.buffer[p.index(x1 , y1)] = p.color(0,-value,-value,255);
						}
					}
				}
			}
			
			''')
					
					
					
		self.response.out.write('''
		document.write('<img src="data:image/png;base64,'+p.getBase64()+'">');
		
		</script>
		''');
		
		self.response.out.write('''
		
		<br><br>
		
		<form action="/dmap" method="post">
			<div>(dy/dx) = <textarea name="command">''' + equation +'''</textarea></div>
			
			<div><input type="submit" value="Graph"></div>
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
		
		
application = webapp.WSGIApplication([('/dmap', DMap)], debug=True)
  
wsgiref.handlers.CGIHandler().run(application)