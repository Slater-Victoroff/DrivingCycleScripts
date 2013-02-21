import DrivingCycle

test = DrivingCycle.DrivingSchedule(
source = "../DrivingTextFiles/JapaneseTechnicalStandards/15mode.txt",
output ="../DrivingTextFiles/JapaneseTechnicalStandards/15mode.txt")
test.parse()
test.toMPH()
test.dump()
	
