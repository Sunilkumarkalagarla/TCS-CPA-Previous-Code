class Question:
    def __init__(self,questionId,markedOption,score):
        self.questionId = questionId
        self.markedOption = markedOption
        self.score = score
        self.status = "Not Answered"

class Student:
    def __init__(self,registrationId,questionsAttempted):
        self.registrationId = registrationId
        self.questionsAttempted = questionsAttempted
    
    def evaluateQuestions(self,answerKey): #2
        for item in self.questionsAttempted:
            if item.questionId not in answerKey.keys():
                continue 
            elif(item.markedOption == answerKey[item.questionId]):
                item.status = "correct"
            else:
                item.status = "incorrect"
        
        
    
    def findGrade(self):
        total= 0
        for item in self.questionsAttempted:
            if item.status.lower() == "correct":
                total += item.score
        
        if total>= 80:
            return 'A'
        elif total>=70:
            return 'B'
        elif total>=60:
            return 'C'
        else:
            return 'F'
        
n = eval(input())
questionsAttempted=[] #1
for i in range(n):
    questionId = eval(input())
    markedOption = eval(input())
    score = eval(input())
    questionsAttempted.append(Question(questionId,markedOption,score))
    
m = eval(input())
answerKey ={}
for i in range(m):
    key = eval(input())
    value = eval(input())
    answerKey[key]=value

y = Student(120,questionsAttempted)

y.evaluateQuestions(answerKey)

for item in questionsAttempted:
    print(item.questionId,item.status)
    
grade = y.findGrade()
print(grade)
