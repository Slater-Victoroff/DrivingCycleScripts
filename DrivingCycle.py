import re
import matplotlib.pyplot as plt

class DrivingSchedule:
	'''A Class that will represent a driving cycle'''
	def __init__(self, source = '', output = '', speed = 'mph',
				pattern = r'^([0-9\.]+?)([ \t]+)([0-9\.]+?)(\n)$',
				timePattern = r'\1', speedPattern = r'\3'):
		self.source = source
		self.output = output
		self.TVdata = {} #Time mapped to velocity
		self.VAdata = {} #Velocity mapped to acceleration
		self.speed = speed #Either mph or kph
		self.pattern = pattern #Theoretically you can use custom formats
								#by passing in your own regex pattern
		self.timePattern = timePattern #If using custom regex, this should be
										#the time regex
		self.speedPattern = speedPattern #This should be the speed regex
		
	def parse(self):
		'''Reads in Driving Schedule data from the provided file according
		to the regex patterns provided, or the defaults'''
		with open(self.source, 'r') as corpus:
			for line in corpus:
				if line[0:2] == '//':
					self.speed = re.sub(r'^([/]*)([a-zA-z]*)$', r'\2',line)
				else:
					currentSpeed = float(re.sub(self.pattern, self.speedPattern, line))
					currentTime = float(re.sub(self.pattern, self.timePattern, line))
					self.TVdata[currentTime] = currentSpeed
		previousVelocity = 0
		for time in self.TVdata:
			self.VAdata[self.TVdata[time]] = self.TVdata[time] - previousVelocity
			previousVelocity = self.TVdata[time]
					
	def toKPH(self):
		'''Changes the velocity values to kph if they are in mph, checks
		this by looking at the comment at the top of the file, otherwise
		there should be no change, change is inplace'''
		if (self.speed[0].lower() == 'm'):
			self.TVdata = self.rescaleTV(1.60934)
			self.VAdata = self.rescaleVA(1.60934)
			self.speed = 'kph'
				
	def toMPH(self):
		'''Same as toKPH, but for MPH'''
		if (self.speed[0].lower() == 'k'):
			self.TVdata = self.rescaleTV(0.621371)
			self.VAdata = self.rescaleVA(0.621371)
			self.speed = 'mph'
	
	def rescaleTV(self, constant):
		'''returns scaled TV data, does not change in place'''
		answer = {}
		for time in self.TVdata:
				answer[time] = self.TVdata[time]*constant
		return answer
				
	def rescaleVA(self,constant):
		'''return scaled VA data, also does not change in place'''
		newVAdata = {}
		for velocity in self.VAdata:
			newVAdata[velocity*constant] = self.VAdata[velocity]*constant
	
	def plotTV(self):
		'''Should render a TV plot as a line graph over time, might allow
		for more calls through to pyplot if people are interested'''
		plt.plot([self.TVdata[time] for time in self.TVdata])
		plt.ylabel("Vehicle Speed (" + self.speed.strip() + ")")
		plt.xlabel("time(secs)")
		plt.show()
		
	def plotVA(self):
		'''Should render a VA plot as a scatter plot showing the power
		regions involved with the given driving schedule'''
		velocities = []
		accelerations = []
		for velocity in self.VAdata:
			 velocities.append(velocity)
			 accelerations.append(self.VAdata[velocity])
		plt.plot(velocities,accelerations,'ro')
		plt.ylabel("Velocity (" + self.speed.strip() + ")")
		plt.xlabel("Acceleration (" + self.speed.strip() + "/s)")
		plt.show()
		
	def dump(self):
		'''Writes the file to the provided output'''
		with open(self.output, 'w') as output:
			output.write('//' + self.speed + "\n")
			for time in self.TVdata:
				output.write(str(time) + "\t" + str(self.TVdata[time]) + "\n")
	
		
