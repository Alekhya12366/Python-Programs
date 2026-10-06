# STRING AND TEXT MANIPULATION – INTERVIEW QUESTIONS


# 1. Remove Spaces from Given Text
# Input: "he llo wor ld"
# Output: "helloworld"

def remove_spaces(text):
    return "".join(text.split())

print(remove_spaces("he llo wor ld"))


# Problem: Write a function to remove all spaces from the input string.
# Explanation: Remove any whitespace characters.

def remove_all_spaces(text):
    return "".join(text.split())

print(remove_all_spaces("he llo wor ld"))


# 2. Reverse a String
# Input: "hello"
# Output: "olleh"

def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))


# Problem: Write a function to reverse the characters in a string.
# Input: "hello"
# Output: "olleh"

def reverse_characters(text):
    return text[::-1]

print(reverse_characters("hello"))


# 3. Reverse a String After Removing Spaces
# Input: "he llo world"
# Output: "dlrowolleh"

def reverse_after_removing_spaces(text):
    text = "".join(text.split())
    return text[::-1]

print(reverse_after_removing_spaces("he llo world"))


# Problem: Write a function to reverse a string after removing all spaces.
# Input: "he llo world"
# Output: "dlrowolleh"

def remove_spaces_and_reverse(text):
    text = "".join(text.split())
    return text[::-1]

print(remove_spaces_and_reverse("he llo world"))


# 4. Convert Snake Case to Camel Case
# Input: "my_variable_name"
# Output: "myVariableName"

def snake_to_camel(text):
    words = text.split("_")
    result = words[0]

    for word in words[1:]:
        result = result + word.capitalize()

    return result

print(snake_to_camel("my_variable_name"))


# Problem: Convert a string from snake_case to camelCase.
# Input: "my_variable_name"
# Output: "myVariableName"

def convert_snake_case_to_camel_case(text):
    words = text.split("_")
    result = words[0]

    for word in words[1:]:
        result = result + word.capitalize()

    return result

print(convert_snake_case_to_camel_case("my_variable_name"))


# 5. Convert Snake Case to Pascal Case
# Input: "my_variable_name"
# Output: "MyVariableName"

def snake_to_pascal(text):
    words = text.split("_")
    result = ""

    for word in words:
        result = result + word.capitalize()

    return result

print(snake_to_pascal("my_variable_name"))


# Problem: Convert a string from snake_case to PascalCase.
# Input: "my_variable_name"
# Output: "MyVariableName"

def convert_snake_case_to_pascal_case(text):
    words = text.split("_")
    result = ""

    for word in words:
        result = result + word.capitalize()

    return result

print(convert_snake_case_to_pascal_case("my_variable_name"))


# 6. Convert Camel Case to Snake Case
# Input: "myVariableName"
# Output: "my_variable_name"

def camel_to_snake(text):
    result = ""

    for char in text:
        if char.isupper():
            result = result + "_" + char.lower()
        else:
            result = result + char

    return result

print(camel_to_snake("myVariableName"))


# Problem: Convert a string from camelCase to snake_case.
# Input: "myVariableName"
# Output: "my_variable_name"

def convert_camel_case_to_snake_case(text):
    result = ""

    for char in text:
        if char.isupper():
            result = result + "_" + char.lower()
        else:
            result = result + char

    return result

print(convert_camel_case_to_snake_case("myVariableName"))


# 7. Convert Camel Case to Pascal Case
# Input: "myVariable"
# Output: "MyVariable"

def camel_to_pascal(text):
    return text[0].upper() + text[1:]

print(camel_to_pascal("myVariable"))


# Problem: Convert a string from camelCase to PascalCase.
# Input: "myVariable"
# Output: "MyVariable"

def convert_camel_case_to_pascal_case(text):
    return text[0].upper() + text[1:]

print(convert_camel_case_to_pascal_case("myVariable"))


# 8. Convert Pascal Case to Camel Case
# Input: "MyVariable"
# Output: "myVariable"

def pascal_to_camel(text):
    return text[0].lower() + text[1:]

print(pascal_to_camel("MyVariable"))


# Problem: Convert a string from PascalCase to camelCase.
# Input: "MyVariable"
# Output: "myVariable"

def convert_pascal_case_to_camel_case(text):
    return text[0].lower() + text[1:]

print(convert_pascal_case_to_camel_case("MyVariable"))


# 9. Convert Pascal Case to Snake Case
# Input: "MyVariable"
# Output: "my_variable"

def pascal_to_snake(text):
    result = ""

    for char in text:
        if char.isupper() and result != "":
            result = result + "_"

        result = result + char.lower()

    return result

print(pascal_to_snake("MyVariable"))


# Problem: Convert a string from PascalCase to snake_case.
# Input: "MyVariable"
# Output: "my_variable"

def convert_pascal_case_to_snake_case(text):
    result = ""

    for char in text:
        if char.isupper() and result != "":
            result = result + "_"

        result = result + char.lower()

    return result

print(convert_pascal_case_to_snake_case("MyVariable"))


# 10. Convert Text to Camel Case
# Input: "hello world example"
# Output: "helloWorldExample"

def text_to_camel(text):
    words = text.split()
    result = words[0]

    for word in words[1:]:
        result = result + word.capitalize()

    return result

print(text_to_camel("hello world example"))


# Problem: Convert normal text into camelCase.
# Input: "hello world example"
# Output: "helloWorldExample"

def convert_text_to_camel_case(text):
    words = text.split()
    result = words[0]

    for word in words[1:]:
        result = result + word.capitalize()

    return result

print(convert_text_to_camel_case("hello world example"))


# 11. Convert Text to Snake Case
# Input: "hello world example"
# Output: "hello_world_example"

def text_to_snake(text):
    return "_".join(text.split())

print(text_to_snake("hello world example"))


# Problem: Convert normal text into snake_case.
# Input: "hello world example"
# Output: "hello_world_example"

def convert_text_to_snake_case(text):
    return "_".join(text.split())

print(convert_text_to_snake_case("hello world example"))


# 12. Convert Text to Pascal Case
# Input: "hello world example"
# Output: "HelloWorldExample"

def text_to_pascal(text):
    words = text.split()
    result = ""

    for word in words:
        result = result + word.capitalize()

    return result

print(text_to_pascal("hello world example"))


# Problem: Convert normal text into PascalCase.
# Input: "hello world example"
# Output: "HelloWorldExample"

def convert_text_to_pascal_case(text):
    words = text.split()
    result = ""

    for word in words:
        result = result + word.capitalize()

    return result

print(convert_text_to_pascal_case("hello world example"))


# 13. Swap Upper and Lower Case
# Input: "HeLLo"
# Output: "hEllO"

def swap_upper_lower(text):
    return text.swapcase()

print(swap_upper_lower("HeLLo"))


# 14. Separate Digits from Text
# Input: "abc123d4"
# Output: "1234"

def separate_digits(text):
    result = ""

    for char in text:
        if char.isdigit():
            result = result + char

    return result

print(separate_digits("abc123d4"))


# 15. Print Uppercase, Lowercase, Digits,
# and Special Characters Separately

def print_character_types(text):
    uppercase = ""
    lowercase = ""
    digits = ""
    special = ""

    for char in text:
        if char.isupper():
            uppercase = uppercase + char
        elif char.islower():
            lowercase = lowercase + char
        elif char.isdigit():
            digits = digits + char
        else:
            special = special + char

    print("Uppercase:", uppercase)
    print("Lowercase:", lowercase)
    print("Digits:", digits)
    print("Special Characters:", special)


print_character_types("Abc123!@#")


# 16. Count Uppercase, Lowercase, Digits,
# and Special Characters

def count_character_types(text):
    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0

    for char in text:
        if char.isupper():
            uppercase = uppercase + 1
        elif char.islower():
            lowercase = lowercase + 1
        elif char.isdigit():
            digits = digits + 1
        else:
            special = special + 1

    print("Uppercase:", uppercase)
    print("Lowercase:", lowercase)
    print("Digits:", digits)
    print("Special Characters:", special)


count_character_types("AbC@123x!")


# 17. Check Password Strength
# Input: "Pass123!"
# Output: "Strong Password"

def check_password_strength(password):
    uppercase = False
    lowercase = False
    digit = False
    special = False

    for char in password:
        if char.isupper():
            uppercase = True
        elif char.islower():
            lowercase = True
        elif char.isdigit():
            digit = True
        else:
            special = True

    if uppercase and lowercase and digit and special:
        return "Strong Password"
    else:
        return "Weak Password"


print(check_password_strength("Pass123!"))


# 18. Remove Duplicates
# Input: "aabbcc"
# Output: "abc"

def remove_duplicates(text):
    result = ""

    for char in text:
        if char not in result:
            result = result + char

    return result


print(remove_duplicates("aabbcc"))


# 19. Print Duplicates
# Input: "aabbccde"
# Output: "abc"

def print_duplicates(text):
    result = ""

    for char in text:
        if text.count(char) > 1 and char not in result:
            result = result + char

    print(result)


print_duplicates("aabbccde")


# 20. Print Next Characters
# Input: "abc"
# Output: "bcd"

def print_next_characters(text):
    result = ""

    for char in text:
        result = result + chr(ord(char) + 1)

    print(result)


print_next_characters("abc")
