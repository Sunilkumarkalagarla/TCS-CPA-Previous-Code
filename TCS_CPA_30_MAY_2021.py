class Citizen:
    def __init__(self,citizenID,citizenName,citizenAge,isFrontlineWorker,VaccineOptedFor,preference=None):
        self.citizenID=citizenID
        self.citizenName=citizenName
        self.citizenAge=citizenAge
        self.isFrontlineWorker=isFrontlineWorker
        self.VaccineOptedFor =VaccineOptedFor
        self.preference=preference
        
    def setPreference(self):
        if self.isFrontlineWorker.lower() == "yes" or self.citizenAge >45:
            self.preference=1
        else:
            self.preference=0
            
class VaccinationDrive:
    def __init__(self,cList):
        self.cList=cList
    
    def getPrefferedVaccinationCount(self):
        count =0
        for item in self.cList: #2
            if item.preference == 1:
                count +=1
        
        if count>0:
            return count
        else:
            return None
                
        
        
    def getCitizensAsPerVaccine(self,vaccineName):
        newList =[]
        for item in cList: #3
            if item.VaccineOptedFor.lower()== vaccineName.lower():
                newList.append(item)
                
        if len(newList)>0: #4
            orderedList = sorted(newList, key = lambda x:x.citizenAge)
            return orderedList
        else:
            return None
            
                
        
        
n=eval(input())
cList =[]
for i in range(n): #1
    citizenID = input()
    citizenName = input()
    citizenAge= eval(input())
    isFrontlineWorker=input()
    VaccineOptedFor = input()
    cList.append(Citizen(citizenID, citizenName, citizenAge, isFrontlineWorker, VaccineOptedFor))
    cList[i].setPreference()

y = VaccinationDrive(cList)
VaccineName = input()

val= y.getCitizensAsPerVaccine(VaccineName)
if val == None:
    print("Citizen not found")
else:
    for item in val:
        print(item.citizenID,item.citizenName,item.citizenAge,sep="\n")
    
res = y.getPrefferedVaccinationCount()
if res == None:
    print("Preffered citizen not found")
else:
    print(res)
