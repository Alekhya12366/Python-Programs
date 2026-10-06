# String and Text Manipulation – Interview Questions


# 1. Remove Spaces from Given Text
# Problem: Write a function to remove all spaces from the input string. Explanation: Remove any whitespace characters.
# Input: "he llo wor ld"
# Output: "helloworld"
def remove_spaces(text):
    return text.replace(" ", "")

print(remove_spaces("he llo wor ld"))


# 2. Reverse a String
# Problem: Write a function to reverse the characters in a string.
# Input: "hello"
# Output: "olleh"
def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))


# 3. Reverse a String After Removing Spaces
# Problem: Write a function to reverse a string after removing all spaces.
# Input: "he llo world"
# Output: "dlrowolleh"
def reverse_without_spaces(text):
    text = text.replace(" ", "")
    return text[::-1]

print(reverse_without_spaces("he llo world"))


# 4. Convert Snake Case to Camel Case
# Problem: Convert a string from snake_case to camelCase.
# Input: "my_variable_name"
# Output: "myVariableName"
def snake_to_camel(text):
    words = text.split("_")
    result = words[0]
    for word in words[1:]:
        result = result + word.capitalize()
    return result

print(snake_to_camel("my_variable_name"))


# 5. Convert Snake Case to Pascal Case
# Problem: Convert a string from snake_case to PascalCase.
# Input: "my_variable_name"
# Output: "MyVariableName"
def snake_to_pascal(text):
    words = text.split("_")
    result = ""
    for word in words:
        result = result + word.capitalize()
    return result

print(snake_to_pascal("my_variable_name"))


# 6. Convert Camel Case to Snake Case
# Problem: Convert a string from camelCase to snake_case.
# Input: "myVariableName"
# Output: "my_variable_name"
def camel_to_snake(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result = result + "_" + ch.lower()
        else:
            result = result + ch
    return result

print(camel_to_snake("myVariableName"))


# 7. Convert Camel Case to Pascal Case
# Problem: Convert a string from camelCase to PascalCase.
# Input: "myVariable"
# Output: "MyVariable"
def camel_to_pascal(text):
    return text[0].upper() + text[1:]

print(camel_to_pascal("myVariable"))


# 8. Convert Pascal Case to Camel Case
# Problem: Convert a string from PascalCase to camelCase.
# Input: "MyVariable"
# Output: "myVariable"
def pascal_to_camel(text):
    return text[0].lower() + text[1:]

print(pascal_to_camel("MyVariable"))


# 9. Convert Pascal Case to Snake Case
# Problem: Convert a string from PascalCase to snake_case.
# Input: "MyVariable"
# Output: "my_variable"
def pascal_to_snake(text):
    result = ""
    for i in range(len(text)):
        ch = text[i]
        if ch.isupper() and i != 0:
            result = result + "_" + ch.lower()
        else:
            result = result + ch.lower()
    return result

print(pascal_to_snake("MyVariable"))


# 10. Convert Text to Camel Case
# Problem: Convert a space-separated sentence into camelCase.
# Input: "hello world example"
# Output: "helloWorldExample"
def text_to_camel(text):
    words = text.split()
    result = words[0].lower()
    for word in words[1:]:
        result = result + word.capitalize()
    return result

print(text_to_camel("hello world example"))


# 11. Convert Text to Snake Case
# Problem: Convert a space-separated sentence into snake_case.
# Input: "hello world example"
# Output: "hello_world_example"
def text_to_snake(text):
    return "_".join(text.lower().split())

print(text_to_snake("hello world example"))


# 12. Convert Text to Pascal Case
# Problem: Convert a space-separated sentence into PascalCase.
# Input: "hello world example"
# Output: "HelloWorldExample"
def text_to_pascal(text):
    words = text.split()
    result = ""
    for word in words:
        result = result + word.capitalize()
    return result

print(text_to_pascal("hello world example"))


# 13. Swap Upper and Lower Case
# Problem: Swap the case of each letter in a given string.
# Input: "HeLLo"
# Output: "hEllO"
def swap_case(text):
    return text.swapcase()

print(swap_case("HeLLo"))


# 14. Separate Digits from Text
# Problem: Extract all digits from a given alphanumeric string.
# Input: "abc123d4"
# Output: "1234"
def extract_digits(text):
    digits = ""
    for ch in text:
        if ch.isdigit():
            digits = digits + ch
    return digits

print(extract_digits("abc123d4"))


# 15. Print Uppercase, Lowercase, Digits and Special Characters Separately
# Problem: Print each type of character separately from the string.
# Input: "Abc123!@#"
# Output:
#   Uppercase: A
#   Lowercase: b c
#   Digits: 1 2 3
#   Special Characters: ! @ #
def print_char_types(text):
    upper = []
    lower = []
    digits = []
    special = []
    for ch in text:
        if ch.isupper():
            upper.append(ch)
        elif ch.islower():
            lower.append(ch)
        elif ch.isdigit():
            digits.append(ch)
        else:
            special.append(ch)
    print("Uppercase:", " ".join(upper))
    print("Lowercase:", " ".join(lower))
    print("Digits:", " ".join(digits))
    print("Special Characters:", " ".join(special))

print_char_types("Abc123!@#")


# 16. Count of Uppercase, Lowercase, Digits and Special Characters
# Problem: Count each type of character in a string.
# Input: "AbC@123x!"
# Output:
#   Uppercase: 2
#   Lowercase: 1
#   Digits: 3
#   Special Characters: 2
# Note: the input has 2 lowercase letters ('b' and 'x'), so the program prints 2.
def count_char_types(text):
    upper = 0
    lower = 0
    digits = 0
    special = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1
    print("Uppercase:", upper)
    print("Lowercase:", lower)
    print("Digits:", digits)
    print("Special Characters:", special)

# Note: "AbC@123x!" has 2 lowercase letters ('b' and 'x'),
# so the correct count is 2 (the sample output in the question says 1).
count_char_types("AbC@123x!")


# 17. Check Password Strength
# Problem: Check if a password contains at least one uppercase, one lowercase, one digit, and one special character.
# Input: "Pass123!"
# Output: "Strong Password"
def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True
    if has_upper and has_lower and has_digit and has_special:
        return "Strong Password"
    else:
        return "Weak Password"

print(check_password("Pass123!"))


# 18. Remove Duplicates in a Given Input
# Problem: Remove duplicate characters from a string.
# Input: "aabbcc"
# Output: "abc"
def remove_duplicates(text):
    result = ""
    for ch in text:
        if ch not in result:
            result = result + ch
    return result

print(remove_duplicates("aabbcc"))


# 19. Print Duplicates in a Given String
# Problem: Identify and print duplicate characters in a string.
# Input: "aabbccde"
# Output: a b c
def print_duplicates(text):
    duplicates = []
    for ch in text:
        if text.count(ch) > 1 and ch not in duplicates:
            duplicates.append(ch)
    print(" ".join(duplicates))

print_duplicates("aabbccde")


# 20. Print Next Characters in a Given String
# Problem: Replace each character in the string with its next character.
# Input: "abc"
# Output: "bcd"
def next_characters(text):
    result = ""
    for ch in text:
        result = result + chr(ord(ch) + 1)
    return result

print(next_characters("abc"))
