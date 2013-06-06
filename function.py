import sandbox as bme

class Function:

	def __init__(self,text,head = "f(x)"):
		self.text = text
		self.head = head
		
	def show(self):
		bme.handler.response.out.write("<br>" + self.head + " = " + self.text + "<br>")
		
	def calc(self,*args, **kwargs):
		
		x = kwargs.get('x',0)
		y = kwargs.get('y',0)
		z = kwargs.get('z',0)
		
		return eval(self.text)
		
	def linTable(self,*args, **kwargs):
		bme.handler.response.out.write('''
		<table border="1">
			<tr>
				<td>&nbsp;&nbsp;x&nbsp;&nbsp;</td>
				<td>&nbsp;&nbsp;''' + self.head + '''&nbsp;&nbsp;</td>
			</tr>
			''')
			
		for val in args:
			bme.handler.response.out.write('''<tr>
			<td>''' + str(val) + '''</td>
			<td>''' + str(self.calc(x=val)) + '''</td>
			</tr>''')
	
		bme.handler.response.out.write('''
		<table>
		''')
		
class Parametric(Function):

	def __init__(self,*args, **kwargs):
	
		self.x = kwargs.get('x',None)
		self.y = kwargs.get('y',None)
		self.z = kwargs.get('z',None)
		
	def show(self):
		bme.handler.response.out.write("<br>")
		
		if self.x:
			bme.handler.response.out.write("x = " + self.x + "<br>")
		
		if self.y:
			bme.handler.response.out.write("y = " + self.y + "<br>")
			
		if self.z:
			bme.handler.response.out.write("z = " + self.z + "<br>")
		
	def calc(self,t):
		
		val = []
		
		if self.x:
			val.append(eval(self.x))
		
		if self.y:
			val.append(eval(self.y))
			
		if self.z:
			val.append(eval(self.z))
		
		return tuple(val)