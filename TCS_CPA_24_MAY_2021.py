class Vaccine():
    def __init__(self, vaccineId, vaccineName, startDueMonth, endDueMonth):
        self.vaccineId = vaccineId
        self.vaccineName = vaccineName
        if startDueMonth > endDueMonth:
            self.startDueMonth = endDueMonth
            self.endDueMonth = startDueMonth
        else:
            self.startDueMonth = startDueMonth
            self.endDueMonth = endDueMonth


class Child():
    def __init__(self, childName, dateOFBirth, ageInMonths, vaccinationDetails):
        self.childName = childName
        self.dateOFBirth = dateOFBirth
        self.ageInMonths = ageInMonths
        self.vaccinationDetails = vaccinationDetails


def vaccinateChild(vaccineList, child, vaccinationDate):
	ans = False
    for vaccine in vaccineList:
        if child.vaccinationDetails.get(vaccine.vaccineId) == None and child.ageInMonths >= vaccine.startDueMonth and child.ageInMonths <= vaccine.endDueMonth:
            child.vaccinationDetails[vaccine.vaccineId] = vaccinationDate
            ans = True

    return ans


def vaccinateChildren(vaccineList, childList, vaccinationDate):
    count = 0
    for child in childList:
        if vaccinateChild(vaccineList, child, vaccinationDate):
            count += 1

    return count


if __name__ == '__main__':
    n = int(input())
    vaccineList = []
    for i in range(n):
        vaccineId = int(input())
        vaccineName = input()
        startDueMonth = int(input())
        endDueMonth = int(input())
        vaccineList.append(Vaccine(vaccineId, vaccineName,
                                   startDueMonth, endDueMonth))
    
    m = int(input())
    childList = []
    for i in range(m):
        childName = input()
        dateOFBirth = input()
        ageInMonths = int(input())
        vaccinationDetails = {}
        id1 = int(input())
        id2 = int(input())
        vaccinationDetails[id1] = dateOFBirth
        vaccinationDetails[id2] = dateOFBirth
        childList.append(Child(childName, dateOFBirth,
                               ageInMonths, vaccinationDetails))

    vaccinationDate = input()
    if vaccinateChild(vaccineList,childList[0],vaccinationDate) :
    	print(f"Vaccination Successful For {childList[0].childName}")
    else :
    	print("Vaccination Not Successful.")

    count = vaccinateChildren(vaccineList,childList,vaccinationDate)
    if count > 0 :
    	print(f"Count Of Children Vaccinated={count}")
    	for child in childList :
    		print(child.childName)
    		for k, v in child.vaccinationDetails.items() :
    			print(k, v)
    else :
    	print("No child vaccinated.")
