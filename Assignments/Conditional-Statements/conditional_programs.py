Interview-Style Questions Based on Conditional Statements 

1. Check Even or Odd 
Question: Determine whether a number is even or odd. Explanation: A number is even if it 
is divisible by 2. Otherwise, it’s odd. - Input: Number = 6 - Output: Even number 

• num= int (input("Enter the No:")) 
• if num%2==0: 
• print("Even No") 
• else: 
• print("odd No") 
• OUTPUT: 
• Enter the No: 6 
• Even No 

2. Divisible by 5 but Not by 10 
Question: Check if a number is divisible by 5 but not by 10. Explanation: Use modulo (%) 
to check if the number % 5 == 0 and number % 10 != 0. - Input: Number = 25 - Output: 
Satisfy 

• num = int(input("Enter the No:")) 
• if num%5==0 and num%10!=0: 
• print("Divisible ") 
• else: 
• print("Not Divisible") 

• OUTPUT: 
• Enter the No: 25 
• Divisible  

3. Biggest Among Two Numbers 
Question: Find the biggest number among two. Explanation: Use comparison operators 
(>) to check which number is greater. - Input: A = 4, B = 7 - Output: Biggest is: 7 

• a= int (input("Enter the No :")) 
• b= int (input("Enter the No :")) 
• if a>b: 
• print("Biggest is :",a) 
• else: 
• print("Biggest is :", b)
 
• OUTPUT: 
• Enter the No : 4 
• Enter the No : 7 
• Biggest is : 7 

4. Smallest Among Two Numbers 
Question: Find the smallest number among two. Explanation: Use comparison operators 
(<) to find the smaller value. - Input: A = 4, B = 7 - Output: Smallest is: 4 

• A = int(input("Enter first number A: ")) 
• B = int(input("Enter second number B: ")) 
• if A < B: 
• print("Smallest is:", A) 
• else: 
• print("Smallest is:", B) 

• OUTPUT: 
• Enter first number A: 4 
• Enter second number B: 7 
• Smallest is: 4 

5. Divisible by 2, 3, and 6 
Question: Check if a number is divisible by 2, 3, and 6. Explanation: If a number is 
divisible by both 2 and 3, it is also divisible by 6. - Input: Number = 18 - Output: Satisfy 

• num= int(input("Enter the No:")) 
• if num%2==0 and num%3==0 and num%6==0: 
• print("Divisible") 
• else: 
• print("Not Divisible") 

• OUTPUT: 
• Enter the No: 18 
• Divisible 

6. Voting Eligibility 
Question: Check if a person is eligible to vote (age >= 18). Explanation: A person is eligible 
to vote if their age is 18 or above. - Input: Age = 19 - Output: Eligible to vote 

• age = int(input("Enter the Age:")) 
• if age>=18: 
• print("Eligible To Vote") 
• else: 
• print("Not Eligible To Vote") 

• OUTPUT: 
• Enter the Age:19 
• Eligible To Vote 

7. Student Pass/Fail Based on All Subjects >= 35 
Question: Check if a student passed all subjects (maths, physics, chemistry). 
Explanation: Student passes only if marks in all subjects are 35 or more. - Input: Maths = 
40, Physics = 36, Chemistry = 30 - Output: Fail 

• maths = int(input("Enter Maths marks: ")) 
• physics = int(input("Enter Physics marks: ")) 
• chemistry = int(input("Enter Chemistry marks: ")) 
• if maths >= 35 and physics >= 35 and chemistry >= 35: 
•            print("Pass") 
• else: 
•     print("Fail") 

• OUTPUT: 
• Enter Maths marks: 40 
• Enter Physics marks: 36 
• Enter Chemistry marks: 30 
• Fail 

8. Student Pass if Passed Any One Subject (>= 35) 
Question: Check if the student passed at least one subject. Explanation: Use logical OR 
to check if any one subject has marks >= 35. - Input: Maths = 20, Physics = 38, Chemistry = 
25 - Output: Pass 

• maths= int(input("Maths Marks:")) 
• physics = int(input("Physics Marks:")) 
• chemistry = int(input("Chemistry Marks:")) 
• if maths >= 35 or physics >= 35 or chemistry>=35: 
• print("Pass") 
• else: 
• print("Fail") 

• OUTPUT: 
• Enter Maths marks: 20 
• Enter Physics marks: 38 
• Enter Chemistry marks: 25 
• Pass 

9. Student Pass if Passed Any Two Subjects 
Question: Check if the student passed any two out of three subjects. Explanation: Use a 
counter or logical conditions to verify two subjects >= 35. - Input: Maths = 40, Physics = 20, 
Chemistry = 36 - Output: Pas 

• maths = int(input("Maths Marks:")) 
• physics = int(input("Physics Marks:")) 
• chemistry = int(input("Chemistry Marks:")) 
• if (maths >= 35 and physics >= 35) or \ 
• (maths >= 35 and chemistry >= 35) or \ 
• (physics >= 35 and chemistry >= 35): 
• print("Pass") 
• else: 
• print("Fail") 

• OUTPUT: 
• Maths Marks: 40 
• Physics Marks: 20 
• Chemistry Marks: 36 
• Pass     

10. Biggest Among Three Numbers 
Question: Find the biggest number among three. Explanation: Compare each pair of 
numbers using if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9 

• a= int (input("A Number :")) 
• b= int (input("B Number:")) 
• c= int(input("C Number:")) 
• if a>b and a>c: 
• print("Biggest is:", a) 
• elif b>a and b>c: 
• print("Biggest is :",b) 
• else: 
• print("Biggest is:", c) 

• OUTPUT: 
• A Number : 7 
• B Number: 4 
• C Number: 9 
• Biggest is: 9 

11. Smallest Among Three Numbers 
Question: Find the smallest number among three. Explanation: Use comparison logic to 
determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4 

• a= int (input("A Number :")) 
• b= int (input("B Number:")) 
• c= int(input("C Number:")) 
• if a<b and a<c: 
•            print("Smallest  is:", a) 
• elif b<a and b<c: 
•            print("Smallest is :",b) 
• else: 
•          print("Smallest is:", c) 

• OUTPUT: 
• A Number : 7 
• B Number: 4 
• C Number: 9 
• Smallest is : 4 

12. Perfect Square or Not 
Question: Check if a number is a perfect square. Explanation: A number is a perfect 
square if the square of its square root equals the number. - Input: Number = 49 - Output: 
Perfect square 

• num = int (input("Enter the No:")) 
• sqrt= int(num**0.5) 
• if sqrt *sqrt ==num: 
• print(num, "Is Perfect Square") 
• else: 
• print(num,"Is Not Perfect Square") 

• OUTPUT: 
• Enter the No: 49 
• 49 Is Perfect Square 

13. Cars Required for Members (Max 5 per car) 
Question: Calculate how many cars are needed for a given number of people. 
Explanation: Divide total people by 5 and round up using ceiling logic. - Input: Members = 
17 - Output: Cars needed = 4 

• # Cars Required for Members 
• members = int(input("Enter Total Members: ")) 
• cars = members // 5 
• # If there are remaining members, one more car is needed 
• if members % 5 != 0: 
• cars = cars + 1 
• print("Cars needed =", cars) 

• OUTPUT 1: 
•  
• Enter Total Members: 17 
• Cars needed = 4 
•  
• OUTPUT 2: 
•  
• Enter Total Members: 10 
• Cars needed = 2 
•  
• OUTPUT 3: 
•  
• Enter Total Members: 23 
• Cars needed = 5 

14. Second Biggest Among Three Numbers 
Question: Find the second largest number among three inputs. Explanation: Use sorting 
or nested conditions to find the second largest value. - Input: A = 10, B = 25, C = 18 - 
Output: Second biggest: 18 

• a= int (input("A Number :")) 
• b= int (input("B Number:")) 
• c= int(input("C Number:")) 
• list1= [a,b,c] 
• list1.sort() 
• print("Second biggest:", list1[1]) 

• OUTPUT: 
• A Number : 10 
• B Number: 25 
• C Number: 18 
• Second biggest: 18 

15. Leap Year or Not 
Question: Check if a given year is a leap year. Explanation: A year is a leap year if it is 
divisible by 4, and (not divisible by 100 unless divisible by 400). - Input: Year = 2024 - 
Output: Leap year 

• # Leap Year or Not 
•  
• year = int(input("Enter the Year: ")) 
•  
• if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
•     print("Leap Year") 
• else: 
•     print( "Not a leap year") 

• OUTPUT 1 
• Enter the Year: 2024 
• 2024 Leap Year 

• OUTPUT 2 
• Enter the Year: 2023 
• 2023 Not a leap year
 
• OUTPUT 3 
• Enter the Year: 2000 
• 2000 Leap Year 

• OUTPUT 4 
• Enter the Year: 1900 
• 1900 Not a leap year 