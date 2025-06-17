import sys

## TO DO:
#  Add your code here to define the following classes:
#     Student()
#    StudentAssistant()
#    STscholar()
#    SAscholar
##
class Student:
    def __init__(self, subjects, units, funds):
        if not hasattr(self, 'discount'):
            self.discount = 0
            
        self.subjects = subjects
        self.funds = funds
        self.units = int(units)
            
        if self.funds >= self.units*1500*(1-self.discount):
                self.funds -= self.units*1500*(1-self.discount)
                
        else:
            self.subjects.clear()
            self.units = 0
            print("Student not enlisted. Not enough funds.")
        
    def enlist(self, subject, units):
        # TO DO:
        #     Insert code to enlist one subject and update funds
        #   and units as specified

        if self.funds > units*1500*(1-self.discount):
            self.subjects.append(subject)
            self.units += int(units)
            self.funds -= int(units)*1500*(1-self.discount)
        
        else:
            print("Not enough funds.")
            
    
class StudentAssistant(Student):
    def work(self,hours):
        self.funds += hours*60

class STscholar(Student):
    def __init__(self, subjects, units, funds, bracket):
        discount_bracket = {'A':0,'B':0.33,'C':0.60,'D':0.80,'E':1}
        self.discount = discount_bracket[bracket]
        super().__init__(subjects, units, funds)
        
class SAscholar(StudentAssistant, STscholar):     
    def overtime(self,hours):
        self.funds += hours*60*(1+self.discount)


###Do not edit code below. This is purely for checking.
def main():
    
    #initialize list of students
    mystudents=[]
    
    #enlist students of different types
    mystudents.append(Student(['Math 21', 'Physics 71', 'EEE 113', 'EEE 118'], 12, 100000))
    mystudents[0].enlist("EEE 111", 3)
    
    mystudents.append(StudentAssistant(['Eng 13', 'Soc Sci 1', 'EEE 111', 'EEE 113', 'Philo 1', 'Math 20'], 15, 50000))
    mystudents[1].enlist("EEE 118", 1)
    mystudents[1].work(10)
    
    mystudents.append(STscholar(['Math 21', 'Physics 71', 'EEE 113', 'EEE 118'], 12, 100000,"B"))
    mystudents[2].enlist("EEE 111", 3)
    
    mystudents.append(SAscholar(['Math 21', 'Physics 71', 'EEE 113', 'EEE 118'], 12, 100000,"B"))
    mystudents[3].enlist("EEE 111", 3)
    mystudents[3].work(10)
    mystudents[3].overtime(10)
    
    # print student details    
    for i in mystudents:
        print(i.subjects)
        print(i.units)
        print(i.discount)    
        print(i.funds, "\n")
    
    #### Remove the following 10 lines if not coding in HackerRank
    # execute additional test cases, if any
    inplist = []
    for line in sys.stdin:
        inplist.append(line.replace("\n",""))
    
    if inplist[0] == "0":
        pass
    else:
        for i in range(1, len(inplist)):
            exec(inplist[i])

if __name__ == '__main__':
    main()
