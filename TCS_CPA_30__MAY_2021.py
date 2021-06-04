class Sponsor:
    def __init__(self,sponsorName,sponsorCompany,subsidiaries,sponsorCategory):
        self.sponsorName=sponsorName
        self.sponsorCompany=sponsorCompany
        self.subsidiaries = subsidiaries
        self.sponsorCategory = sponsorCategory
        
def getSponsor(sponsorList,sponsorCategory):
    nameList=[]
    for item in sponsorList: #2
        if item.sponsorCategory.lower() == sponsorCategory.lower():
            nameList.append(item.sponsorName)
    
    if len(nameList)==0:
        return None
    else:
        return sorted(nameList) #3
    
    

def findSponsorWithMaximumSubsdiaries(sponsorList):
    highest= 0
    obj = None
    for item in sponsorList: #4
        if len(item.subsidiaries)>highest:
            highest = len(item.subsidiaries)
            obj = item
            
    return obj.sponsorName
            
            
    
sponsorList = []
n = eval(input())
for i in range(n):#1
    sponsorName = input()
    sponsorCompany= input()
    m = eval(input())
    subsidiaries =[]
    for j in range(m):
        subsidiaries.append(input())
    sponsorCategory = input()
    sponsorList.append(Sponsor(sponsorName,sponsorCompany,subsidiaries,sponsorCategory))
    
sponsorCategory=input()


val = getSponsor(sponsorList,sponsorCategory)
if val ==None:
    print("No matching record found")
else:
    for item in val:
        print(item)
    

name = findSponsorWithMaximumSubsdiaries(sponsorList)
print(name)
