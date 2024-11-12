#Object Oriented Programming
#Take note of the syntax class Classname:
#(important to note that the classname starts witha capital letter and its always in singular)
#Creating Classes
#forexample Cohort class
#class Cohort:
    #name(string)
    #description(string)
    #start_date(string)
    #end_date(string)
    #total_number_of_students(int)
    #add a constructor for the cohort class. hint read about constructors
    #add a method(function) to the class that prints name and the total_number_of students
    #create a new instance(object) of the cohort class. hint Newcohort = cohort()


class Cohort():
    def __init__(self,name,description,start_date,end_date,total_number_of_students):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.number = total_number_of_students
       
    def print_information(self):
        print('The cohort name is: ' + self.name)
        print(f'The total number of students in this cohort is: {self.number}')
        
New_cohort = Cohort("cohort4","diploma in computer science","5th/08/2024","6th/08/2024",50)
New_cohort.print_information()
