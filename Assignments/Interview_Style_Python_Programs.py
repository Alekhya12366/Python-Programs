Interview-Style Programming Questions: Loops, Strings, and Number Operations
________________________________________
1. Print Numbers from 1 to n
Question: Write a program to print numbers from 1 to n. Explanation: Use a loop starting from 1 to n and print each number. - Input: n = 5 - Output: 1 2 3 4 5
•	# Program 1: Print Numbers from 1 to n

•	n = int(input("Enter n: "))
•	for i in range(1, n + 1):
•	print(i, end=" ")

•	OUTPUT:
•	Enter n: 5
•	1 2 3 4 5 
________________________________________
2. Print Numbers from m to n
Question: Write a program to print numbers from m to n. Explanation: Loop from m to n and print values. - Input: m = 3, n = 7 - Output: 3 4 5 6 7

•	# Program 2: Print Numbers from m to n

•	m = int(input("Enter m: "))
•	n = int(input("Enter n: "))
•	for i in range(m, n + 1):
•	print(i, end=" ")

•	OUTPUT:
•	Enter m:  3
•	Enter n:  7
•	3 4 5 6 7 
________________________________________
3. Print Numbers from n to 1 in Reverse
Question: Write a program to print numbers in reverse from n to 1. Explanation: Use a loop starting from n and decrement to 1. - Input: n = 5 - Output: 5 4 3 2 1

•	# Program 3: Print Numbers from n to 1 in Reverse

•	n = int(input("Enter n: "))
•	for i in range(n, 0, -1):
•	print(i, end=" ")

•	OUTPUT:
•	Enter n:  5
•	5 4 3 2 1 
________________________________________
4. Print Numbers from n to m in Reverse
Question: Write a program to print numbers from n to m in reverse. Explanation: Start from n and go down to m. - Input: n = 10, m = 6 - Output: 10 9 8 7 6

•	# Program 4: Print Numbers from n to m in Reverse

•	n = int(input("Enter n: "))
•	m = int(input("Enter m: "))
•	for i in range(n, m - 1, -1):
•	print(i, end=" ")

•	OUTPUT:
•	Enter n:  10
•	Enter m:  6
•	10 9 8 7 6 
________________________________________
5. Sum of n Natural Numbers
Question: Write a program to calculate the sum of first n natural numbers. Explanation: Use formula or loop to sum from 1 to n. - Input: n = 5 - Output: 15

•	# Program 5: Sum of n Natural Numbers

•	n = int(input("Enter n: "))
•	sum = 0
•	for i in range(1, n + 1):
•	sum = sum + i
•	print(sum)


•	OUTPUT:
•	Enter n:  5
•	15
________________________________________
6. Factorial of a Number
Question: Write a program to find the factorial of a number. Explanation: Multiply all numbers from 1 to n. - Input: n = 5 - Output: 120

•	# Program 6: Factorial of a Number

•	n = int(input("Enter n: "))
•	fact = 1
•	for i in range(1, n + 1):
•	fact = fact * i
•	print(fact)

•	OUTPUT:
•	Enter n:  5
•	120
________________________________________
7. Sum of m to n Numbers
Question: Write a program to find the sum of all numbers from m to n. Explanation: Loop from m to n and add values. - Input: m = 3, n = 6 - Output: 18

•	m = int(input("Enter m: "))
•	n = int(input("Enter n: "))
•	sum = 0
•	for i in range(m, n + 1):
•	sum = sum + i
•	print("Sum =", sum)

•	OUTPUT:
•	Enter m:  3
•	Enter n:  6
•	Sum = 18
________________________________________
8. Product of m to n Numbers
Question: Write a program to find the product of numbers from m to n. Explanation: Loop from m to n and multiply values. - Input: m = 2, n = 4 - Output: 24

•	m = int(input("Enter m: "))
•	n = int(input("Enter n: "))
•	product = 1
•	for i in range(m, n + 1):
•	product = product * i
•	print("Product =", product)

•	OUTPUT:
•	Enter m:  2
•	Enter n:  4
•	Product = 24
________________________________________
9. Print Factors of a Number
Question: Write a program to print all factors of a given number. Explanation: Check divisibility of number from 1 to n. - Input: n = 6 - Output: 1 2 3 6

•	n = int(input("Enter a number: "))
•	for i in range(1, n + 1):
•	if n % i == 0:
•	print(i, end=" ")

•	OUTPUT:
•	Enter a number:  6
•	1 2 3 6 
________________________________________
10. Count of Factors
Question: Write a program to count how many factors a number has. Explanation: Increment count when divisible. - Input: n = 6 - Output: 4

•	n = int(input("Enter a number: "))
•	count = 0
•	for i in range(1, n + 1):
•	if n % i == 0:
•	count = count + 1
•	print( count)

•	OUTPUT:
•	Enter a number:  6
•	 4
________________________________________
11. Prime Number Check
Question: Check if a number is prime. Explanation: A number is prime if it has exactly 2 factors. - Input: n = 7 - Output: Prime

•	n = int(input("Enter a number: "))
•	count = 0
•	for i in range(1, n + 1):
•	if n % i == 0:
•	count = count + 1
•	if count == 2:
•	print("Prime")
•	else:
•	print("Not Prime")

•	OUTPUT:
•	Enter a number:  7
•	Prime
________________________________________
12. Even Numbers from m to n
Question: Print all even numbers between m and n. Explanation: Use loop and check if divisible by 2. - Input: m = 3, n = 10 - Output: 4 6 8 10

•	m = int(input("Enter m: "))
•	n = int(input("Enter n: "))
•	for i in range(m, n + 1):
•	if i % 2 == 0:
•	print(i, end=" ")

•	OUTPUT:
•	Enter m:  3
•	Enter n:  10
•	4 6 8 10 
________________________________________
13. Odd Numbers from m to n
Question: Print all odd numbers between m and n. Explanation: Check if number % 2 != 0. - Input: m = 3, n = 10 - Output: 3 5 7 9

•	m = int(input("Enter m: "))
•	n = int(input("Enter n: "))
•	for i in range(m, n + 1):
•	if i % 2 != 0:
•	print(i, end=" ")

•	OUTPUT:
•	Enter m:  3
•	Enter n:  10
•	3 5 7 9 
________________________________________
14. Count of Even and Odd Numbers
Question: Count how many even and odd numbers are in the range m to n. Explanation: Use counters for even and odd. - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3

•	m = int(input("Enter m: "))
•	n = int(input("Enter n: "))
•	even = 0
•	odd = 0
•	for i in range(m, n + 1):
•	if i % 2 == 0:
•	even = even + 1
•	else:
•	odd = odd + 1
•	print("Even =", even)
•	print("Odd =", odd)

•	OUTPUT:
•	Enter m:  3
•	Enter n:  7
•	Even = 2
•	Odd = 3
________________________________________
15. Reverse a String
Question: Reverse a given string. Explanation: Use slicing or loop. - Input: “hello” - Output: “olleh”
•	string = input("Enter a string: ")
•	reverse = string[::-1]
•	print( reverse)

•	OUTPUT:
•	Enter a string:  hello
•	 olleh

________________________________________
16. Check for Palindrome String
Question: Check if a string is a palindrome. Explanation: Compare string with its reverse. - Input: “madam” - Output: Palindrome
•	string = input("Enter a string: ")
•	reverse = string[::-1]
•	if string == reverse:
•	print("Palindrome")
•	else:
•	print("Not Palindrome")

•	OUTPUT:
•	Enter a string:  madam
•	Palindrome

________________________________________
17. Sum of Digits
Question: Calculate the sum of digits of a number. Explanation: Use loop and % 10 to extract digits. - Input: 123 - Output: 6
•	number = int(input("Enter a number: "))
•	sum = 0
•	while number > 0:
•	digit = number % 10
•	sum = sum + digit
•	number = number // 10
•	print(sum)

•	OUTPUT:
•	Enter a number:  123
•	 6

________________________________________
18. Product of Digits
Question: Calculate the product of digits. Explanation: Multiply digits extracted from number. - Input: 123 - Output: 6
•	number = int(input("Enter a number: "))
•	product = 1
•	while number > 0:
•	digit = number % 10
•	product = product * digit
•	number = number // 10
•	print( product)

•	OUTPUT:
•	Enter a number:  123
•	 6

________________________________________
19. Armstrong Number Check
Question: Check if a number is an Armstrong number. Explanation: Sum of cube of digits equals the number. - Input: 153 - Output: Armstrong number
number = int(input("Enter a number: "))

•	temp = number
•	sum = 0
•	while temp > 0:
•	digit = temp % 10
•	sum = sum + (digit ** 3)
•	temp = temp // 10
•	if sum == number:
•	print("Armstrong number")
•	else:
•	print("Not Armstrong number")

•	OUTPUT:
•	Enter a number:  153
•	Armstrong number

________________________________________
20. Reverse a Number
Question: Reverse the digits of a number. Explanation: Use loop with % and // to reverse. - Input: 123 - Output: 321
•	number = int(input("Enter a number: "))
•	reverse = 0
•	while number > 0:
•	digit = number % 10
•	reverse = reverse * 10 + digit
•	number = number // 10
•	print( reverse)

•	OUTPUT:
•	Enter a number:  123
•	321

________________________________________
21. Palindrome Number Check
Question: Check if a number is a palindrome. Explanation: Compare number with its reverse. - Input: 121 - Output: Palindrome
•	number = int(input("Enter a number: "))
•	temp = number
•	reverse = 0
•	while temp > 0:
•	digit = temp % 10
•	reverse = reverse * 10 + digit
•	temp = temp // 10
•	if number == reverse:
•	print("Palindrome")
•	else:
•	print("Not Palindrome")

•	OUTPUT:
•	Enter a number:  121
•	Palindrome

________________________________________
22. Count Vowels in String
Question: Count number of vowels in a string. Explanation: Loop and check for a, e, i, o, u. - Input: “apple” - Output: 2
•	string = input("Enter a string: ")
•	count = 0
•	for ch in string:
•	if ch.lower() in "aeiou":
•	count = count + 1
•	print( count)

•	OUTPUT:
•	Enter a string:  apple
•	 2

________________________________________
23. Count Consonants in String
Question: Count consonants in a string. Explanation: Check for alphabetic characters not vowels. - Input: “apple” - Output: 3
•	string = input("Enter a string: ")
•	count = 0
•	for ch in string:
•	if ch.isalpha() and ch.lower() not in "aeiou":
•	count = count + 1
•	print( count)

•	OUTPUT:
•	Enter a string:  apple
•	3

________________________________________
24. Count Vowels and Consonants
Question: Count vowels and consonants in input string. Explanation: Maintain two counters. - Input: “apple” - Output: Vowels = 2, Consonants = 3
•	string = input("Enter a string: ")
•	vowels = 0
•	consonants = 0
•	for ch in string:
•	if ch.isalpha():
•	if ch.lower() in "aeiou":
•	vowels = vowels + 1
•	else:
•	consonants = consonants + 1
•	print("Vowels =", vowels)
•	print("Consonants =", consonants)

•	OUTPUT:
•	Enter a string:  apple
•	Vowels = 2
•	Consonants = 3

________________________________________
25. Perfect Number Check
Question: Check if a number is perfect. Explanation: Sum of proper divisors equals the number. - Input: 28 - Output: Perfect number
•	number = int(input("Enter a number: "))
•	sum = 0
•	for i in range(1, number):
•	if number % i == 0:
•	sum = sum + i
•	if sum == number:
•	print("Perfect number")
•	else:
•	print("Not Perfect number")

•	OUTPUT:
•	Enter a number:  28
•	Perfect number

________________________________________
26. Neon Number Check
Question: Check if a number is a neon number. Explanation: Square the number, sum digits, match original. - Input: 9 - Output: Neon number
•	number = int(input("Enter a number: "))
•	square = number * number
•	sum = 0
•	while square > 0:
•	digit = square % 10
•	sum = sum + digit
•	square = square // 10
•	if sum == number:
•	print("Neon number")
•	else:
•	print("Not Neon number")

•	OUTPUT:
•	Enter a number:  9
•	Neon number

________________________________________
27. Strong Number Check
Question: Check if a number is a strong number. Explanation: Sum of factorial of digits equals the number. - Input: 145 - Output: Strong number
•	number = int(input("Enter a number: "))
•	temp = number
•	sum = 0
•	while temp > 0:
•	digit = temp % 10
•	factorial = 1
•	for i in range(1, digit + 1):
•	factorial = factorial * i
•	sum = sum + factorial
•	temp = temp // 10
•	if sum == number:
•	print("Strong number")
•	else:
•	print("Not Strong number")

•	OUTPUT:
•	Enter a number:  145
•	Strong number

________________________________________
28. Harshad Number Check
Question: Check if a number is divisible by the sum of its digits. Explanation: Calculate digit sum and check divisibility. - Input: 18 - Output: Harshad number
•	number = int(input("Enter a number: "))
•	temp = number
•	sum = 0
•	while temp > 0:
•	digit = temp % 10
•	sum = sum + digit
•	temp = temp // 10
•	if number % sum == 0:
•	print("Harshad number")
•	else:
•	print("Not Harshad number")

•	OUTPUT:
•	Enter a number:  18
•	Harshad number

________________________________________
29. Fibonacci Series
Question: Print the Fibonacci series up to n terms. Explanation: Start with 0, 1 and continue with sum of last two. - Input: n = 5 - Output: 0 1 1 2 3
•	n = int(input("Enter number of terms: "))
•	first = 0
•	second = 1
•	for i in range(n):
•	print(first, end=" ")
•	next = first + second
•	first = second
•	second = next

•	OUTPUT:
•	Enter number of terms:  5
•	0 1 1 2 3 

________________________________________
30. Check for Neon Number (Repeated)
Question: Again, check for a neon number (example). Explanation: Square number and sum digits. - Input: 9 - Output: Neon number
•	number = int(input("Enter a number: "))
•	square = number * number
•	sum = 0
•	while square > 0:
•	digit = square % 10
•	sum = sum + digit
•	square = square // 10
•	if sum == number:
•	print("Neon number")
•	else:
•	print("Not Neon number")

•	OUTPUT:
•	Enter a number:  9
•	Neon number


