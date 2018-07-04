

class Demo(Object):
	def __init__(self,value):
		self.value=value
	def get_value():
		return self.value

def new_demo_obj(value):
	obj=Demo(value)
	print obj.get_value()
