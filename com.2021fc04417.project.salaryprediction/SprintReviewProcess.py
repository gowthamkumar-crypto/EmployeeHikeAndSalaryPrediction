
class ReviewData():
    totalWorkingHours = []
    actualWorkingHours = []
    jobInvolvement = []
    overTime = []
    assignedStoryPoints = []
    spillOver = []
    achivements = []
    coreValues = []
    numberOfSprints = 0
    def __init__(self,data):
        self.numberOfSprints = len(data)
        for record in data:
            self.totalWorkingHours.append(record[0])
            self.actualWorkingHours.append(record[1])
            self.jobInvolvement.append(record[2])
            self.overTime.append(record[3])
            self.assignedStoryPoints.append(record[4])
            self.spillOver.append(record[5])
            self.achivements.append(record[6])
            self.coreValues.append(record[7])

    def review(self):
        workingHours = (sum(self.totalWorkingHours)/sum(self.actualWorkingHours))*0.1
        involvement  = ((sum(self.jobInvolvement)/self.numberOfSprints)/4)*0.25
        ot = ((sum(self.overTime)/self.numberOfSprints)/sum(self.totalWorkingHours))*0.15
        sprintPoints =  ((sum(self.assignedStoryPoints)/self.numberOfSprints)/8)*0.15
        spill = ((sum(self.spillOver)/self.numberOfSprints)/8)*(-0.2)
        achive = (self.achivements.count('true')/self.numberOfSprints)*0.25
        values = (self.coreValues.count('true')/self.numberOfSprints)*0.1
        finalreview = workingHours+involvement+ot+sprintPoints+spill+achive+values
        return round(finalreview, 2)