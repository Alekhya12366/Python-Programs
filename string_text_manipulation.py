# String and Text Manipulation – Interview Questions


# 1. Remove Spaces from Given Text

def remove_spaces(text):
    return "".join(text.split())


print(remove_spaces("he llo wor ld"))


# 2. Reverse a String

def reverse_string(text):
    return text[::-1]


print(reverse_string("hello"))


# 3. Reverse a String After Removing Spaces

def reverse_after_removing_spaces(text):
    text = "".join(text.split())
    return text[::-1]


print(reverse_after_removing_spaces("he llo world"))


# 4. Convert Snake Case to Camel Case

def snake_to_camel(text):
    words = text.split("_")

    result = words[0]

    for word in words[1:]:
        result = result + word.capitalize()

    return result


print(snake_to_camel("my_variable_name"))


# 5. Convert Snake Case to Pascal Case

def snake_to_pascal(text):
    words = text.split("_")

    result = ""

    for word in words:
        result = result + word.capitalize()

    return result


print(snake_to_pascal("my_variable_name"))


# 6. Convert Camel Case to Snake Case

def camel_to_snake(text):
    result = ""

    for char in text:
        if char.isupper():
            result = result + "_" + char.lower()
        else:
            result = result + char

    return result


print(camel_to_snake("myVariableName"))


# 7. Convert Camel Case to Pascal Case

def camel_to_pascal(text):
    return text[0].upper() + text[1:]


print(camel_to_pascal("myVariable"))


# 8. Convert Pascal Case to Camel Case

def pascal_to_camel(text):
    return text[0].lower() + text[1:]


print(pascal_to_camel("MyVariable"))


# 9. Convert Pascal Case to Snake Case

def pascal_to_snake(text):
    result = ""

    for char in text:
        if char.isupper() and result != "":
            result = result + "_"

        result = result + char.lower()

    return result


print(pascal_to_snake("MyVariable"))


# 10. Convert Text to Camel Case

def text_to_camel(text):
    words = text.split()

    result = words[0]

    for word in words[1:]:
        result = result + word.capitalize()

    return result


print(text_to_camel("hello world example"))


# 11. Convert Text to Snake Case

def text_to_snake(text):
    words = text.split()

    return "_".join(words)


print(text_to_snake("hello world example"))


# 12. Convert Text to Pascal Case

def text_to_pascal(text):
    words = text.split()

    result = ""

    for word in words:
        result = result + word.capitalize()

    return result


print(text_to_pascal("hello world example"))


# 13. Swap Upper and Lower Case

def swap_case(text):
    return text.swapcase()


print(swap_case("HeLLo"))


# 14. Separate Digits from Text

def separate_digits(text):
    result = ""

    for char in text:
        if char.isdigit():
            result = result + char

    return result


print(separate_digits("abc123d4"))


# 15. Print Uppercase, Lowercase, Digits,
#     and Special Characters Separately

def separate_characters(text):
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


separate_characters("Abc123!@#")


# 16. Count Uppercase, Lowercase, Digits,
#     and Special Characters

def count_characters(text):
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


count_characters("AbC@123x!")


# 17. Check Password Strength

def check_password(password):
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


print(check_password("Pass123!"))


# 18. Remove Duplicates in a Given Input

def remove_duplicates(text):
    result = ""

    for char in text:
        if char not in result:
            result = result + char

    return result


print(remove_duplicates("aabbcc"))


# 19. Print Duplicates in a Given String

def print_duplicates(text):
    result = ""

    for char in text:
        if text.count(char) > 1 and char not in result:
            result = result + char

    return result


print(print_duplicates("aabbccde"))


# 20. Print Next Characters in a Given String

def next_characters(text):
    result = ""

    for char in text:
        result = result + chr(ord(char) + 1)

    return result


print(next_characters("abc"))