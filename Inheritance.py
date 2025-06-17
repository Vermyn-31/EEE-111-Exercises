import sys

class Student():
    def __init__(self, subjects, units, funds):
        # TO DO:
        #     Insert code to initialize the object as specified
        self.subjects = subjects
        self.funds = funds
        self.units = int(units)
        
        if self.funds >= self.units*1500:
            self.funds -= self.units*1500
        else:
            self.subjects.clear()
            self.units = 0
            print("Student not enlisted. Not enough funds.")

      
    def enlist(self, subject, units):
        # TO DO:
        #     Insert code to enlist one subject and update funds
        #   and units as specified

        if self.funds >= units*1500:
            self.subjects.append(subject)
            self.units += int(units)
            self.funds -= int(units)*1500
        
        else:
            print("Not enough funds.")
        

class StudentAssistant(Student):       
    def work(self, hours):
        # TO DO:
        #     Insert code to update the students'fund value
        #   by the number of hours worked multipled by the hourly 
        #   rate of P60
        self.funds += hours*60

        
###Do not edit code below. This is purely for checking.
def main():
    #create object studentA and enlist EEE 111
    studentA = Student(['Math 21', 'Physics 71', 'EEE 113', 'EEE 118'], 12, 100000)
    studentA.enlist("EEE 111", 3)
    
    #create object studentB and enlist EEE 118
    studentB = StudentAssistant(['Eng 13', 'Soc Sci 1', 'EEE 111', 'EEE 113', 'Philo 1', 'Math 20'], 15, 50000)
    studentB.enlist("EEE 118", 1)
    
    # print student details
    print(studentA.subjects)
    print(studentA.units)
    print(studentA.funds)    
    print(studentB.subjects)
    print(studentB.units)
    print(studentB.funds)     
    
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
    