
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
		
		
class Euler(webapp.RequestHandler):
	def get(self):
		self.render("",'0','0','1','0.5')
		
	def post(self):
		self.render(self.request.get('command')
		,self.request.get('x1')
		,self.request.get('y1')
		,self.request.get('x2')
		,self.request.get('step')
		)
		
	def render(self,equation,x1,y1,x2,step):
		global handler
		
		self.response.out.write('''
		<html>
		<head>
		<title>Euler's Method</title>
		
		<script type="text/javascript" src="script/jsDraw2D.js">
		</script>
		
		</head>
		
		<body>
		<center>
		<h1>Euler's Method</h1>
		
		<br><br>
		Output:<br>
		''')
		
		handler = self
		
		if equation != "":
			

			
			self.response.out.write('''
			
			<div id="canvas" style="overflow:hidden;position:relative;width:600px;height:600px;"></div>
			
			<table border="1">
			<tr>
				<td>&nbsp;&nbsp;x&nbsp;&nbsp;</td>
				<td>&nbsp;&nbsp;y&nbsp;&nbsp;</td>
				<td>&nbsp;&nbsp;dy/dx = ''' + equation + '''&nbsp;&nbsp;</td>
				<td>&nbsp;&nbsp;Delta Y = dy/dx * ''' + str(step) + '''&nbsp;&nbsp;</td>
			</tr>
			''')
			
			x = float(x1)
			y = float(y1)
			
			linecode = "points = new Array("
			
			while x <= (float(x2) + float(step)/2):
			
				d = eval(equation)
				dy = d * float(step)
				
				self.response.out.write('''
				<tr>
					<td>''' + str(x) + '''</td>
					<td>''' + str(y) + '''</td>
					<td>''' + str(d) + '''</td>
					<td>''' + str(dy) + '''</td>
				</tr>
				''')
				
				linecode += "new jsPoint(" + str(x) + "," + str(y) + "),"
				
				x += float(step)
				y += dy
				
			x -= float(step)
			y -= dy
			
			linecode = linecode[:(len(linecode)-1)]
			
			linecode += ");"
			
			high = (max(float(x2),float(x1)), max(float(y),float(y1)))
			low = (min(float(x2),float(x1)), min(float(y),float(y1)))
			
			xscale = 600 / (high[0] - low[0])
			yscale = 600 / (high[1] - low[1])
			scale = 1
			
			
			if xscale < yscale:
				scale = xscale
			else:
				scale = yscale
			
			xstart = -float(low[0])*scale
			ystart = (float(low[1])*scale) + 600
				
			self.response.out.write('''
			</table>
			''')
			
			self.response.out.write('''
			
			<script type="text/javascript">
			
			var gr =new jsGraphics(document.getElementById("canvas"));
			
			gr.setOrigin(new jsPoint(''' + str(xstart) + ''', ''' + str(ystart) + '''));

			
			gr.setCoordinateSystem("cartecian");
			
			
			
			var redPen=new jsPen(new jsColor("red"),1);


			gr.setScale(''' + str(abs(scale)) +''');
			
			gr.showGrid(1);
			
			''' + linecode + '''
			
			gr.drawPolyline(redPen, points)



			</script>
			
			
			''' + str(high) + '''
			''' + str(low) + '''
			''')
		

		
		self.response.out.write('''
		<br><br>
		
		<form action="/euler" method="post">
			<div>(dy/dx) = <textarea name="command">''' + equation +'''</textarea></div>
			<div>
			Initial Point: <br>x=<textarea name="x1">''' + x1 +'''</textarea><br> y=<textarea name="y1">''' + y1 +'''</textarea>
			</div>
			
			<div>
			Value to Approximate: <br>x=<textarea name="x2">''' + x2 +'''</textarea>
			</div>
			
			<div>
			Step size=<textarea name="step">''' + step +'''</textarea>
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
		
		
application = webapp.WSGIApplication([('/euler', Euler)], debug=True)
  
wsgiref.handlers.CGIHandler().run(application)