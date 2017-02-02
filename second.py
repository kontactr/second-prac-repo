class age:
    def s_age(self):
        self.s__age=input("enter your age: ")
    def s_last(self):
        print ("\nthanks for using....")


class student(age):
    name="xyz"
    rollno="0"
    def s_input(self):
     self.name=input("enter your name: ")
     self.rollno=input("enter your rollno: ")
     self.s_age()
    def s_output(self):
        print ("\nname is: "+self.name)
        print ("rollno is: "+self.rollno)
        print ("age is: "+self.s__age)
        self.s_last()
    def __init__(self):
     print ("welcome....\n")


s1=student()
s1.s_input()
s1.s_output()

