1.Palindrome of a Number Using Recursion

def is_number_palindrome(num):
    def reverse_number(n, rev=0):
        if n == 0:
            return rev

        return reverse_number(n // 10, rev * 10 + n % 10)

    return num == reverse_number(num)


num = int(input("Enter a number: "))

if is_number_palindrome(num):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")



2. Palindrome of a String Using Recursion

def is_string_palindrome(text, start, end):
    if start >= end:
        return True

    if text[start] != text[end]:
        return False

    return is_string_palindrome(text, start + 1, end - 1)


text = input("Enter a string: ")

if is_string_palindrome(text, 0, len(text) - 1):
    print("String is a palindrome")
else:
    print("String is not a palindrome")
