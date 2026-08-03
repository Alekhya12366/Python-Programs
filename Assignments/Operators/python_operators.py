#Arithmetic Operators 
#1.	A product costs ₹450 and a customer buys 6 of them. Calculate the total bill. 
price = 450
quantity = 6

total_bill = price * quantity

print("Total bill:", total_bill)

#OUTPUT:   Total bill: 2700

#2.	A student scored 480 marks out of 600. Calculate the percentage. 
marks = 480
total_marks = 600

percentage = (marks / total_marks) * 100

print("Percentage:", percentage)

#OUTPUT:   Percentage: 80.0
#3.	A company has 125 employees. Divide them equally into 8 teams. Find how many employees are in each team. 

employees = 125
teams = 8

employees_per_team = employees // teams

print("Employees in each team:", employees_per_team)

#OUTPUT:   Employees in each team: 15

#4.	A bakery made 95 cupcakes and packs them into boxes of 12. Find how many completely filled boxes can be made. 

cupcakes = 95
box_size = 12

filled_boxes = cupcakes // box_size

print("Completely filled boxes:", filled_boxes)

#OUTPUT:   Completely filled boxes: 7

#5.	After packing the cupcakes into boxes of 12, find how many cupcakes are left. 

cupcakes = 95
box_size = 12

remaining_cupcakes = cupcakes % box_size

print("Remaining cupcakes:", remaining_cupcakes)

#OUTPUT:   Remaining cupcakes: 11

#6.	A square has a side length of 14 cm. Find its area. 

side = 14

area = side * side

print("Area of square:", area)

#OUTPUT:   Area of square: 196


#7.	A number is multiplied by itself 5 times. Write a program for the calculation. 

number = 3

result = number ** 5

print("Result:", result)

#OUTPUT:   Result: 243


#8.	A person earns ₹1,250 per day for 28 days. Find the total earnings. 

daily_earning = 1250
days = 28

total_earnings = daily_earning * days

print("Total earnings:", total_earnings)

#OUTPUT:  Total earnings: 35000


#9.	Rahul has ₹2,500 and spends ₹1,375. Find the remaining balance. 

balance = 2500
spent = 1375

remaining_balance = balance - spent

print("Remaining balance:", remaining_balance)

#OUTPUT: Remaining balance: 1125


#10.	Find the average of three numbers: 45, 78, and 92. 
num1 = 45
num2 = 78
num3 = 92

average = (num1 + num2 + num3) / 3

print("Average:", average)

#OUTPUT:   Average: 71.66666666666667
 
#Assignment Operators  
#11.	Store the value 500 in a variable called balance. 

balance = 500

print("Balance:", balance)

#OUTPUT:   Balance: 500


#12.	A wallet initially has ₹800. Add ₹250 to it using a shortcut assignment. 

wallet = 800

wallet += 250

print("Wallet balance:", wallet)

#OUTPUT:   Wallet balance: 1050


#13.	A player has 100 health points. Reduce the health by 35 using a shortcut assignment. 

health = 100

health -= 35

print("Remaining health:", health)

#OUTPUT:   Remaining health: 65


#14.	A salary is ₹40,000. Increase it by multiplying it by 2 using a shortcut assignment. 

salary = 40000

salary *= 2

print("Updated salary:", salary)

#OUTPUT:   Updated salary: 80000


#15.	A total distance is 600 km. Divide it equally among 3 drivers using a shortcut assignment. 

distance = 600

distance /= 3

print("Distance for each driver:", distance)

#OUTPUT:   Distance for each driver: 200.0


#16.	A number is 96. Update it by dividing it into groups of 5 and keeping only the complete groups. 


number = 96

number //= 5

print("Complete groups:", number)


#OUTPUT:   Complete groups: 19



#17.	Store the value 8 in a variable and update it by raising it to the power of 3 using a shortcut assignment. 


number = 8

number **= 3

print("Result:", number)

#OUTPUT:   Result: 512


#18.	A warehouse has 125 items. After packing them into groups of 9, update the variable to store only the remaining items. 


items = 125

items %= 9

print("Remaining items:", items)

#OUTPUT:   Remaining items: 8

#Comparison / Relational Operators 


#19.	Check whether Rahul's age (18) is greater than Ramesh's age (16). 

rahul_age = 18
ramesh_age = 16

result = rahul_age > ramesh_age

print("Rahul is older than Ramesh:", result)

#OUTPUT:   Rahul is older than Ramesh: True


#20.	Check whether the temperature is less than 0°C. 

temperature = -5

result = temperature < 0

print("Temperature is below 0°C:", result)

#OUTPUT:   Temperature is below 0°C: True


#21.	Check whether a student scored at least 35 marks. 

marks = 42

result = marks >= 35

print("Student passed:", result)

#OUTPUT:   Student passed: True

#22.	Check whether a product price is not equal to ₹999. 

price = 850

result = price != 999

print("Price is not equal to ₹999:", result)

#OUTPUT:   Price is not equal to ₹999: True


#23.	Check whether two passwords entered by a user are exactly the same.


password1 = "Python123"
password2 = "Python123"

result = password1 == password2

print("Passwords are the same:", result)

#OUTPUT:   Passwords are the same: True

 
#24.	Check whether a person's height is greater than or equal to 170 cm. 

height = 175

result = height >= 170

print("Height is greater than or equal to 170 cm:", result)


#OUTPUT:   Height is greater than or equal to 170 cm: True


#25.	Check whether the stock quantity is less than or equal to 10.


stock = 8

result = stock <= 10

print("Stock is less than or equal to 10:", result)

#OUTPUT:   Stock is less than or equal to 10: True

 
#26.	Check whether the entered PIN is different from the stored PIN. 
stored_pin = 1234
entered_pin = 5678

result = entered_pin != stored_pin

print("PIN is different:", result)

#OUTPUT:   PIN is different: True
 
#Logical Operators  
#27.	A student passes only if marks are above 35 and attendance is at least 75%. Write the condition. 

marks = 40
attendance = 80

result = marks > 35 and attendance >= 75

print("Student Passed:", result)

#OUTPUT:   Student Passed: True


#28.	A customer gets free delivery if they are a premium member or their purchase is above ₹1,000. 

premium_member = False
purchase_amount = 1500

result = premium_member or purchase_amount > 1000

print("Free Delivery:", result)

#OUTPUT:   Free Delivery: True


#29.	A website allows login only if the username and password are both correct. 

username_correct = True
password_correct = True

result = username_correct and password_correct

print("Login Successful:", result)

#OUTPUT:   Login Successful: True


#30.	A user can enter the examination hall if they have an ID card or a hall ticket. 


id_card = False
hall_ticket = True

result = id_card or hall_ticket

print("Allowed to Enter:", result)

#OUTPUT:   Allowed to Enter: True


#31.	Check whether a number is not negative. 


number = 15

result = not (number < 0)

print("Number is not negative:", result)

#OUTPUT:   Number is not negative: True


#32.	A person is eligible for a driving license only if they are at least 18 years old and have passed the driving test. 


age = 20
passed_test = True

result = age >= 18 and passed_test

print("Eligible for Driving License:", result)

#OUTPUT:   Eligible for Driving License: True


#33.	A movie ticket discount is available if the customer is a student or a senior citizen. 

student = False
senior_citizen = True

result = student or senior_citizen

print("Discount Available:", result)

#OUTPUT:   Discount Available: True


#34.	A machine starts only if the emergency switch is not turned on. 

emergency_switch = False

result = not emergency_switch

print("Machine Starts:", result)

#OUTPUT:   Machine Starts: True
 
#Bitwise Operators  

#35.	Find the binary result after performing a bitwise operation between 12 and 10. 

num1 = 12
num2 = 10

result = num1 & num2

print("Bitwise AND:", result)
print("Binary:", bin(result))

#OUTPUT:   Bitwise AND: 8
#Binary: 0b1000


#36.	Find the binary result after performing a bitwise operation between 9 and 5. 

num1 = 9
num2 = 5

result = num1 | num2

print("Bitwise OR:", result)
print("Binary:", bin(result))

#OUTPUT:   Bitwise OR: 13
#Binary: 0b1101


#37.	Find the binary result after performing a bitwise operation between 15 and 6.

num1 = 15
num2 = 6

result = num1 ^ num2

print("Bitwise XOR:", result)
print("Binary:", bin(result))

#OUTPUT:   Bitwise XOR: 9
#Binary: 0b1001

 
#38.	Shift the binary representation of 20 by 2 positions toward the left. 

number = 20

result = number << 2

print("Left Shift:", result)
print("Binary:", bin(result))


#OUTPUT:   Left Shift: 80
#Binary: 0b1010000


#39.	Shift the binary representation of 64 by 3 positions toward the right. 

number = 64

result = number >> 3

print("Right Shift:", result)
print("Binary:", bin(result))



#OUTPUT:   Right Shift: 8
#Binary: 0b1000


#40.	Find the bitwise complement of the number 18. 

number = 18

result = ~number

print("Bitwise Complement:", result)

#OUTPUT:   Bitwise Complement: -19
 
