class Person:
    def __init__(self,firstname,lastname):
        ''' Constructor foor this class. '''
        self.firstname = firstname
        self.lastname = lastname
        # Create soome member animals
        #self.members = ['Cod', 'Herring', 'Tuna']
        
    def printName(self):

            print(self.firstname,self.lastname)


class Student(Person):
    def __init__(self,firstname,lastname,subject):
        Person.__init__(self, firstname, lastname)    
        Person.subject = subject
    def printNameSubject(Person):
        print(Person.firstname,' ',Person.lastname,",",' ', Person.subject, sep='')
        


class Teacher(Person):
    def __init__(self,firstname,lastname,course):
        Person.__init__(self, firstname, lastname)
        Person.course = course
    def printNameCourse(Person):
        print(Person.firstname,' ',Person.lastname,",",' ', Person.course, sep='')
        
