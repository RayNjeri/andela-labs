class Car(object):
	"""docstring for CarClassTest"""
	def __init__(self,name="General",model="Gm",type="saloon"):

		self.name = name
		self.model = model
		self.type = type
		self.num_of_wheels = 4
		self.num_of_doors = 4
		self.speed = 0

	def Car_doors(self):
		if self.name == ['Porshe', 'Koenigsegg']:
			return self.num_of_doors == 2
		else:
			return self.num_of_doors
			
	def Car_wheels(self):
		if self.name == 'trailer':
			return self.num_of_wheels ==7
		else:
			return self.num_of_wheels

	def is_saloon(self):
		if self.vehicle_type is not 'trailer':
			self.vehicle_type == 'saloon'
			return True
			return False		

	

	def Car_drive(self,vel):
		assert isinstance(vel,int)
		if self.type =='trailer':
			self.speed == vel * 11
			return self.speed
		elif self.type == 'mercedes':
			self.speed == vel **10
			return self.speed

			

	

