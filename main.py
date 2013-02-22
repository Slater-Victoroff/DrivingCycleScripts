import DrivingCycle

test = DrivingCycle.DrivingSchedule(
source = "../DrivingTextFiles/CaliforniaEPA/UnifiedDrivingSchedule.txt",
output ="../DrivingTextFiles/CaliforniaEPA/UnifiedDrivingSchedule.txt")
test.parse()
test.plotVA()
test.VAdata = test.jitterVAData(velocityJitter = 10, accelerationJitter = 2)
test.plotVA()
	
