Arithmetic Operators 
1.	A product costs ₹450 and a customer buys 6 of them. Calculate the total bill. 
•	 price= 450
•	quantity= 6
•	total=price*quantity
•	print("Total bill:",total)

•	OUTPUT: Total bill: 2700

2.	A student scored 480 marks out of 600. Calculate the percentage. 
•	marks= 480
•	total_marks= 600
•	percentage=(marks/total_marks)*100
•	print("Total percentage:",percentage)

•	OUTPUT: Total percentage: 80.0



3.	A company has 125 employees. Divide them equally into 8 teams. Find how many employees are in each team.
•	employes = 125
•	teams= 8
•	total_employes= employes// teams
•	print("Total_employes:", total_employes)

•	OUTPUT: Total_employes: 15



4.	A bakery made 95 cupcakes and packs them into boxes of 12. Find how many completely filled boxes can be made. 
•	cupcakes = 95
•	boxes= 12
•	total_boxes= cupcakes// boxes
•	print("Total_boxes:", total_boxes)

•	OUTPUT: Total_boxes: 7



5.	After packing the cupcakes into boxes of 12, find how many cupcakes are left. 
•	cupcakes=95
•	boxes= 12
•	left_cupcakes= cupcakes%boxes
•	print("Left_cupcakes:", left_cupcakes)

•	OUTPUT: Left_cupcakes: 11


6.	A square has a side length of 14 cm. Find its area.
•	length= 14
•	side= 14
•	square= side*length
•	print("Area of a square:", square) 

•	OUTPUT: Area of a square: 196


7.	A number is multiplied by itself 5 times. Write a program for the calculation. 
•	num= int(input("enter a number:"))
•	multiple= num**5
•	print("Multiplied :", multiple)

•	OUTPUT: enter a number: 2
•	Multiplied : 32


8.	A person earns ₹1,250 per day for 28 days. Find the total earnings. 
•	per_day= 1250
•	days= 28
•	total_earnings= per_day*days
•	print("Total earnings:",total_earnings)

•	OUTPUT: Total earnings: 35000


9.	Rahul has ₹2,500 and spends ₹1,375. Find the remaining balance. 
•	money= 2500
•	spends= 1375
•	remaining_balance= money- spends
•	print("Remaining balance:",remaining_balance)

•	OUTPUT: Remaining balance: 1125


10.	Find the average of three numbers: 45, 78, and 92.
•	a= 45
•	b=78
•	c=92
•	average= (a+b+c)/3
•	print("Average of three numbers:", average) 

•	OUTPUT: Average of three numbers: 71.66666666666667

  
Assignment Operators  
11.	Store the value 500 in a variable called balance. 
•	balance= 500
•	print("Balance=",balance)

•	OUTPUT: Balance= 500


12.	A wallet initially has ₹800. Add ₹250 to it using a shortcut assignment. 
•	wallet = 800
•	wallet +=250

•	print("Total wallet:",wallet)

•	OUTPUT: Total wallet: 1050



13.	A player has 100 health points. Reduce the health by 35 using a shortcut assignment. 

•	health= 100
•	health-= 35
•	print("Reduced health:",health)

•	OUTPUT: Reduced health: 65


14.	A salary is ₹40,000. Increase it by multiplying it by 2 using a shortcut assignment. 
•	salary = 40000
•	salary*=2
•	print("Total salary:", salary)

•	OUTPUT: Total salary: 80000


15.	A total distance is 600 km. Divide it equally among 3 drivers using a shortcut assignment.
•	distance = 600
•	distance /= 3
•	print("Total distance:", distance)

•	OUTPUT: Total distance: 200.0



16.	A number is 96. Update it by dividing it into groups of 5 and keeping only the complete groups. 
•	num = 96
•	num //=5
•	print("Total groups:", num)

•	OUTPUT: Total groups: 19



17.	Store the value 8 in a variable and update it by raising it to the power of 3 using a shortcut assignment. 
•	a = 8
•	a**=3
•	print("The value of a:", a)

•	OUTPUT: The value of a: 512



18.	A warehouse has 125 items. After packing them into groups of 9, update the variable to store only the remaining items. 
•	items = 125
•	items %= 9
•	print("Remaining items:", items)

•	OUTPUT: Remaining items: 8

  
Comparison / Relational Operators 
19.	Check whether Rahul's age (18) is greater than Ramesh's age (16). 
•	rahul = 18
•	ramesh = 16
•	print(rahul>ramesh)

•	OUTPUT: True


20.	Check whether the temperature is less than 0°C. 

•	temperature = int (input("enter the temp:"))
•	print(temperature<0)
•	OUTPUT: enter the temp: -8

•	True



21.	Check whether a student scored at least 35 marks. 
•	marks = 31
•	print(marks>= 35)

•	OUTPUT: False



22.	Check whether a product price is not equal to ₹999. 
•	price = 450
•	print(price!= 999)  

•	OUTPUT:True



23.	Check whether two passwords entered by a user are exactly the same. 
•	a= int(input("enter the password"))
•	b= int(input("enter the password"))
•	print(a==b)

•	OUTPUT: enter the password 1290
•	enter the password 4590
•	False



24.	Check whether a person's height is greater than or equal to 170 cm. 
•	height = 160
•	print(height>=170)

•	OUTPUT: False


25.	Check whether the stock quantity is less than or equal to 10. 
•	quantity = 19
•	print(quantity<=10) 

•	OUTPUT: False


26.	Check whether the entered PIN is different from the stored PIN. 
•	a= int(input("enter a pin"))
•	b= int(input("enter b pin"))
•	print(a!= b )

•	OUTPUT: True
  
Logical Operators  
27.	A student passes only if marks are above 35 and attendance is at least 75%. Write the condition. 
•	marks = int(input("enter marks"))
•	attendence = int(input("enter the attendence"))
•	print(marks>35 and attendence>=75)

•	OUTPUT:
•	 enter marks 55
•	enter the attendence 80
•	True


28.	A customer gets free delivery if they are a premium member or their purchase is above ₹1,000. 
•	premium = input("are you a premium member? (yes/no)")
•	purchase = int (input("enter the ammount of purchase"))
•	result = premium=="yes" or purchase >1000
•	print("free delevery", result)

•	OUTPUT:
•	are you a premium member? (yes/no) no
•	enter the ammount of purchase 1600
•	free delevery True


29.	A website allows login only if the username and password are both correct. 
•	username = input("enter the username:")
•	password = int(input("enter the password:"))
•	result = username== "alekhya" and password =="12345"
•	print("login:",result)

•	OUTPUT:
•	enter the username: alekhya
•	enter the password: 34567
•	login: False


30.	A user can enter the examination hall if they have an ID card or a hall ticket. 
•	id_card = input("do you have an id card ? (yes/no):")
•	hall_ticket = input("do you have a hall ticket? (yes/no):")
•	result = id_card == "yes" or hall_ticket=="no"
•	print("entered the exam hall",result)

•	OUTPUT:
•	do you have an id card ? (yes/no): no
•	do you have a hall ticket? (yes/no): no
•	entered the exam hall True


31.	Check whether a number is not negative. 
•	num= int(input("enter the no:"))
•	result = not(num <0)
•	print("the no is not negative:",result)
•	OUTPUT:
•	enter the no: 6
•	the no is not negative: True


32.	A person is eligible for a driving license only if they are at least 18 years old and have passed the driving test. 
•	age = int(input("enter the age"))
•	test = input("have you passed the driving license ? (yes/no)")
•	result = age>=18 and test == "yes"
•	print("eligible for the license:",result)

•	OUTPUT:
•	enter the age 23
•	have you passed the driving license ? (yes/no) no
•	eligible for the license: False


33.	A movie ticket discount is available if the customer is a student or a senior citizen. 
•	student = input("Are you a student? (yes/no): ")
•	senior = input("Are you a senior citizen? (yes/no): ")
•	result = student == "yes" or senior == "yes"
•	print("Discount available:", result)

•	OUTPUT:
•	Are you a student? (yes/no):  yes
•	Are you a senior citizen? (yes/no):  no
•	Discount available: True



34.	A machine starts only if the emergency switch is not turned on. 
•	emergency = input("Is the emergency switch turned on? (yes/no): ")
•	result = not (emergency == "yes")
•	print("Machine can start:", result)
•	OUTPUT:
•	Is the emergency switch turned on? (yes/no):  yes
•	Machine can start: False

  
Bitwise Operators  
35.	Find the binary result after performing a bitwise operation between 12 and 10. 
•	a = 12
•	b = 10
•	result = a & b
•	print("Result:", result)

•	OUTPUT: Result: 8


36.	Find the binary result after performing a bitwise operation between 9 and 5. 
•	a = 9
•	b = 5
•	result = a & b
•	print("Result:", result)

•	OUTPUT: Result: 1


37.	Find the binary result after performing a bitwise operation between 15 and 6. 
•	a = 15
•	b = 6
•	result = a & b
•	print("Result:", result)

•	OUTPUT: Result: 6


38.	Shift the binary representation of 20 by 2 positions toward the left.
•	num =20
•	result = num<<2
•	print("result", result) 

•	OUTPUT: result 80


39.	Shift the binary representation of 64 by 3 positions toward the right. 
•	num = 64
•	result = num>>3
•	print("Result:",result)

•	OUTPUT: Result: 8


40.	Find the bitwise complement of the number 18. 
•	num = 18
•	result = ~18
•	print("Result:", result)
•	OUTPUT:
•	Result: -19

 
