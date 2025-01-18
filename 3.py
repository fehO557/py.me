#Tyoecasting = the process of converting a variable from one data type to another
#Str(), int(), float(), bool()

name= "Fernanda"
age = 22
gpa = 3.2
is_student = True
print(type(name))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)

age += "1"
print(age)
#when u use str it's useful "str", if it's false (str) use only the number

name = bool(name)
print(name)