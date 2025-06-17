
class UniversityPerson:
    def __init__(self, lname, fname, age):
        # TODO: Initialize UniversityPerson
        self._lname = lname
        self._fname = fname
        self.age = int(age)

    def __lt__(self, other):
        # TODO: Compare `self` with `other` in this order:
        # - lname
        # - fname
        # - age
        
        # HINT: Comparison here should take into consideration
        #       the "default" order.
        return (self.lname,self.fname,self.age) < (other.lname,other.fname,other.age) 

    @property
    def fname(self):
        # TODO: Return capitalized first name
        return self._fname.title()

    @property
    def lname(self):
        # TODO: Return capitalized last name
        return self._lname.title()

    def __str__(self):
        # TODO: Return UniversityPerson as a string in the specified
        #       output format
        return f"{self.lname}, {self.fname}; {self.age}"
        #pass

def main():
    University_records = []
    testcases = int(input())

    for t in range(testcases):
        n_names, sort_order = input().split(' ')
        n_names = int(n_names)

        for n in range(n_names):
            lname, fname, age = [x.strip() for x in input().split(';')]
            
            # TODO: Create a UniversityPerson object with the previous information
            #       and save that object somewhere.
            #student_record = UniversityPerson(lname, fname, int(age))
            University_records.append(UniversityPerson(lname, fname, int(age)))
            
        # TODO: Sort the records
        if sort_order == '+':
            University_records.sort()
        elif sort_order == '-':
            University_records.sort(reverse = True)
                    
        # TODO: Print each person here
        print(f"Case #{t + 1}:")
        for i in University_records:
            print(i)
        University_records.clear()


if __name__ == '__main__':
    main()