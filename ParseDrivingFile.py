class DrivingSchedule:
	'''A Class that will represent a driving cycle'''
	def __init__(self, source = '', output = '', speed = 'mph',
				pattern = r'^([0-9\.]+?)([ \t]+)([0-9\.]+?)(\n)$',
				timePattern = r'\1', speedPattern = r'\3'):
		self.source = source
		self.output = output
		self.data = {}
		self.speed = speed
		self.pattern = pattern
		self.timePattern = timePattern
		self.speedPattern = speedPattern
		
	def parse(self):
		with corpus as open(self.source, 'r'):
			for line in corpus:
				if line[0:2] == '//':
					self.speed = re.sub(r'^([/]*)([a-zA-z]*$', r'\2',line))
				else:
					currentSpeed = re.sub(self.pattern, self.speedPattern, line)
					currentTime = re.sub(self.pattern, self.timePattern, line)
					self.data[currentTime] = currentSpeed
					
	def toKPH(self):
		if (self.speed[0].lower() == 'm'):
			for time in self.data:
				self.data[time] = self.data[time]*0.621371
			self.speed = 'kph'
				
	def toMPH(self):
		if (self.speed[0].lower() == 'k'):
			for time in self.data:
				self.data[time] = self.data[time]*1.60934
			self.speed = 'mph'
	
	def dump(self):
		with output as open(self.output, 'w'):
			output.write('//' + self.speed)
			for time in self.data:
				output.write(str(time) + "\t" + str(self.data[time]))
	
		
