import DrivingCycle

test = DrivingCycle.DrivingSchedule(
source = "../DrivingTextFiles/CaliforniaEPA/UnifiedShortDrivingCycle.txt",
output ="../DrivingTextFiles/CaliforniaEPA/UnifiedShortDrivingCycle.txt")
test.parse()
test.plotVA()
	
