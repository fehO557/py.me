#variable = container a value (string, integer, float, boolean)
# a variable behaves as if it was the value it contais

#strings
first_name =  "Bro"
food = "pizza"
email = "Bro123@fake.com"

print(f"Hello {first_name}")
#f-string is something like, only the name between parentesis.
#if you need to call the variable, dont use "" or ''.
#ps: to use together u need say print(f"text u need to write {variable}")
print(f"Do you like {food}?")
print(f"your email is: {email}")
#integers
age = 22
quantity = 3
num_of_students = 30

print(f"you are {age} years old")
print(f"you are buying {quantity} items")
print(f"your class has {num_of_students} students")

#float
price = 10.99
gpa= 3.2
distance = 5.5

print(f"the price is ${price}")
print(f"your gpa is: {gpa}")
print(f"you ran {distance}km")

#boolean -> true or false
is_student = True
for_sale = True
is_online= True

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("that item is for sale")
else:
    print("that item item is NOT available")

if is_online:
    print("you are online")
else:
    print("you are offline")