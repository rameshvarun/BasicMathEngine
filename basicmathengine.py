
import cgi
import datetime
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
	def get(self):
		self.render()
		
	def render(self):
		global handler
		
		self.response.out.write('''
		<html>
		<head>
		<title>Basic Math Engine</title>
		
		<link type="text/css" href="css/ui-lightness/jquery-ui-1.8.8.custom.css" rel="Stylesheet" />	
		<script type="text/javascript" src="js/jquery-1.4.4.min.js"></script>
		<script type="text/javascript" src="js/jquery-ui-1.8.8.custom.min.js"></script>
		
		</head>
		
		<body>
		<center>
		<h1>Basic Math Engine</h1>
		
		''')
		
		self.response.out.write('''
		<br><br>
		
		<div id="accordion" style="width:660px;">
			<h3><a href="#">Math Sandbox</a></h3>
			<div>
			A full python powered sandbox embedded into a webpage.
			<br><button onclick="window.location.href='sandbox'">Try It!</button>
			</div>
			
			<h3><a href="#">Triple Integrals</a></h3>
			<div>
			Simple program for solving triple integrals using a Riemann Sum (currently only works for constant itervals).
			<br><button onclick="window.location.href='tp'">Try It!</button>
			</div>
			
			<h3><a href="#">Euler's Method</a></h3>
			<div>Program for solving differential equations using Euler's method. Creates both a graph and a table.
			<br><button onclick="window.location.href='euler'">Try It!</button>
			</div>
			
			<h3><a href="#">Directional Field Grapher</a></h3>
			<div>Experimental grapher for differential equations.
			<br><button onclick="window.location.href='dfield'">Try It!</button>
			</div>
			
			<h3><a href="#">Density Map Grapher</a></h3>
			<div>Experimental program for graphing multivariable functions as density maps.
			<br><button onclick="window.location.href='dmap'">Try It!</button>
			</div>
		</div>
		
		<script type="text/javascript">
		
		$(function() {
			$( "#accordion" ).accordion({
				autoHeight: false,
				navigation: true
			});
			
			$( "button").button();
			
		});
		
		</script>
		
		<br>
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
		
application = webapp.WSGIApplication([('/', MainPage)], debug=True)
  
wsgiref.handlers.CGIHandler().run(application)