
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
		
		
class DField(webapp.RequestHandler):
	def get(self):
		self.render("x + y", True)
		
	def post(self):
		self.render(self.request.get('command'),
		self.request.get('constrain')
		)
		
	def render(self,equation,constrain):
		global handler
		
		self.response.out.write('''
		<html>
		<head>
		<title>Directional Field Grapher</title>
		
		<script type="text/javascript" src="script/jsDraw2D.js">
		</script>
		
		</head>
		
		<body>
		<center>
		<h1>Directional Field Grapher</h1>
		
		<br><br>
		Output:<br>
		''')
		
		handler = self
		
		if equation != "":
		
					
			self.response.out.write('''
			
			<div id="canvas" style="overflow:hidden;position:relative;width:600px;height:600px;"></div>
			
			<script type="text/javascript">
			
			var gr =new jsGraphics(document.getElementById("canvas"));
			
			gr.setOrigin(new jsPoint(300,300));

			
			gr.setCoordinateSystem("cartecian");
			
			var redPen=new jsPen(new jsColor("red"),1);


			gr.setScale(30);
			
			gr.showGrid(1);
			
			''')
			
			for x in range(-10,11):
				for y in range(-10,11):
					try:
						x = float(x)
						y = float(y)
						point1 = (x,y)
						d = float(eval(equation))
						
						if abs(d) > 1 and constrain:
							scale = (1/d)*1
							point2 = (x + scale, y + d*scale)
						else:
							scale = 1
							point2 = (x + scale, y + d*scale)
					
						self.response.out.write('''
						gr.drawLine(redPen, new jsPoint(''' + str(point1[0]) + ''', ''' + str(point1[1]) + '''), new jsPoint(''' + str(point2[0]) + ''', ''' + str(point2[1]) + '''))
						''')
					except:
						pass
					
			self.response.out.write('''

			</script>
			
			''')
		
		if constrain:
			ct = "1"
		else:
			ct = "0"
		
		self.response.out.write('''
		<br><br>
		
		<form action="/dfield" method="post">
			<div>(dy/dx) = <textarea name="command">''' + equation +'''</textarea></div>
			
			<div><input type="checkbox" checked="''' + ct + '''" name="constrain" value="Constrain to Box">Constrain to Box</div>
			
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
		
		
application = webapp.WSGIApplication([('/dfield', DField)], debug=True)
  
wsgiref.handlers.CGIHandler().run(application)