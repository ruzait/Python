#------------------------------------------------class & objects-------------------------------------------------------#
# ---------- Arbitrary Arguments, *args --------- #
'''If you do not know how many arguments that will be passed into your function,
 add a * before the parameter name in the function definition.This way the function will receive a tuple of arguments,
  and can access the items accordingly'''

'''def my_function(*kids):
    for x in range(len(kids)):
        print("The youngest child is " + kids[x])

my_function("Emil", "Tobias", "Linus")'''

'''
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")'''

'''
def my_function(**kid):
    print(len(kid))
    print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")'''

'''#	Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")'''

'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)'''

# -------------- Class --------------- #
'''class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)



x = Person("John", "Doe")
x.printname()'''

# ----- Inheritance ---------- #
# single Inheritance & Malte Inheritance & Herarikal Inheritance
# Parent class & child class

'''class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
'''

'''class teacher:

    fees = 10000
    number_of_teachers = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        teacher.number_of_teachers = teacher.number_of_teachers + 1

    def tech(self):
        details = f'name: {self.name}, age: {self.age}'
        return details


    # teacher   => Parent class
    # principal => child class



class princ(teacher):
    pass
    fees = 20000


t_1 = teacher("nasheha", 20)
t_4 = teacher("anofa", 23)

t5 = princ("kfjghf", 23)
print(t5.fees)'''

# super()
'''
class teacher:

    fees = 10000
    number_of_teachers = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        teacher.number_of_teachers = teacher.number_of_teachers + 1

    def tech(self):
        details = f'name: {self.name}, age: {self.age}'
        return details

class princ(teacher):

    fees = 20000

    def __init__(self, name, age, year):
        # super() is calling {self.name = name, self.age = age}
        super().__init__(name, age)
        self.year = year


t5 = princ("kfjghf", 23, 2000)
print(t5.year)
'''

# ----------------- instant method, class method, static method ----------- #
'''class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

t_1 = teacher("nasheha", 20)
print(t_1.age)
'''

'''
class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tech(self):
        details = f'name: {self.name}, age: {self.age}'
        return details


t_1 = teacher("nasheha", 20)
print(t_1.tech())
'''

'''from datetime import *
class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tech(self):
        details = f'name: {self.name}, age: {self.age}'
        return details

    def boorn(self):
        current_year = date.today().year
        return current_year - self.age

t_1 = teacher("nasheha", 20)
print(t_1.boorn())'''

# -------------  Class Variables ----------- #   // Its like comane variyable
# manual Variable
'''
from datetime import *
class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tech(self):
        details = f'name: {self.name}, age: {self.age}'
        return details

    def boorn(self):
        current_year = date.today().year
        return current_year - self.age

t_1 = teacher("nasheha", 20)
t_2 = teacher("nasheha", 20)


# If call t_2 it has a Error:   AttributeError: 'teacher' object has no attribute 'fees'
t_1.fees = 10000

# so create Class Variable
'''

# class out Variables
'''from datetime import *
class teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tech(self):
        details = f'name: {self.name}, age: {self.age}'
        return details

    def boorn(self):
        current_year = date.today().year
        return current_year - self.age

t_1 = teacher("nasheha", 20)
t_2 = teacher("nasheha", 20)


# Class out Variable
teacher.fees = 20000

'''

# class in  Variables
'''from datetime import *
class teacher:

    # Class Variable
    fees = 10000

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tech(self):
        details = f'name: {self.name}, age: {self.age}'
        return details

    def boorn(self):
        current_year = date.today().year
        return current_year - self.age

t_1 = teacher("nasheha", 20)
t_2 = teacher("nasheha", 20)

print(t_1.fees)
print(t_1.__dict__)'''

'''from datetime import *
class teacher:

    fees = 10000

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tech(self):
        details = f'name: {self.name}, age: {self.age}'
        return details

    def boorn(self):
        current_year = date.today().year
        return current_year - self.age

    def amont(self, amo):
        sal = self.fees - amo
        return sal


t_1 = teacher("nasheha", 20)
t_2 = teacher("nasheha", 20)

print(t_1.amont(50000))'''

# count Variable
'''class teacher:

    number_of_teachers = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # number_of_teachers
        teacher.number_of_teachers = teacher.number_of_teachers + 1

    def tech(self):
        details = f'name: {self.name}, age: {self.age}'
        return details


t_1 = teacher("nasheha", 20)
t_2 = teacher("faish", 21)
t_3 = teacher("rams", 22)
t_4 = teacher("anofa", 23)

print(teacher.number_of_teachers)
'''

# ----  class Method & static method -------#
'''class teacher:

    fees = 10000
    number_of_teachers = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        teacher.number_of_teachers = teacher.number_of_teachers + 1

    def amont(self, amo):
        sal = self.fees - amo
        return sal

    @classmethod
    def change_fees(cls, amo):
        cls.fees = amo

t_1 = teacher("nasheha", 20)
t_4 = teacher("anofa", 23)

print(teacher.change_fees(100))
print(t_4.fees)
'''

'''
class teacher:

    fees = 10000
    number_of_teachers = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        teacher.number_of_teachers = teacher.number_of_teachers + 1

    def amont(self, amo):
        sal = self.fees - amo
        return sal

    @classmethod
    def change_fees(cls, amo):
        cls.fees = amo
        return cls.fees

    @classmethod
    def det_split(cls, data):
        name, age = data.split(",")
        return f'name:{name}, age:{age}'

    @staticmethod
    def streem_dip(streem):
        avil_streem = ['Etech', 'Btech']
        if streem in avil_streem:
            return True
        return False

t_1 = teacher("nasheha", 20)
t_4 = teacher("anofa", 23)

#  --------- @classmethod ---- change_fees
#print(teacher.change_fees(6000))

#  --------- @classmethod ---- det_split
data = "ruzait,19"
#print(teacher.det_split(data))

# --------- @staticmethod ----- streem_dip
print(t_4.streem_dip('Etech'))'''


# --------- Special Methods ----------#
'''
    1. __init__
    2. __str__
    3. __repr__ 
       etc...
'''

# __str__(its return data is "string_Type" )
'''
class student:
    def __init__(self, name):
        self.name = name
        self.age = 19

    def __str__(self):
        return self.name
        # return self.age               # return f'(self.age)'


stud = student("hithaya")
print(stud.name, stud.age)

'''

# __repr__(its return data is "string_Type" )

'''class student:
    def __init__(self, name):
        self.name = name
        self.age = 19

    # def __str__(self):
    # return self.name

    def __repr__(self):
        return f'{self.name}'


stud = student("hithaya")
print([stud.name], stud.name)'''