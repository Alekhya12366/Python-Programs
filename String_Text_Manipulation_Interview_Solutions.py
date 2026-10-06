# String and Text Manipulation - Interview Questions


# 1. Remove Spaces from Given Text
def remove_spaces(text):
    return text.replace(" ", "")

print("1.", remove_spaces("he llo wor ld"))


# 2. Reverse a String
def reverse_string(text):
    return text[::-1]

print("2.", reverse_string("hello"))


# 3. Reverse a String After Removing Spaces
def reverse_without_spaces(text):
    text = text.replace(" ", "")
    return text[::-1]

print("3.", reverse_without_spaces("he llo world"))


# 4. Convert Snake Case to Camel Case
def snake_to_camel(text):
    words = text.split("_")
    result = words[0]
    for word in words[1:]:
        result = result + word.capitalize()
    return result

print("4.", snake_to_camel("my_variable_name"))


# 5. Convert Snake Case to Pascal Case
def snake_to_pascal(text):
    words = text.split("_")
    result = ""
    for word in words:
        result = result + word.capitalize()
    return result

print("5.", snake_to_pascal("my_variable_name"))


# 6. Convert Camel Case to Snake Case
def camel_to_snake(text):
    result = ""
    for ch in text:
        if ch.isupper():
            result = result + "_" + ch.lower()
        else:
            result = result + ch
    return result

print("6.", camel_to_snake("myVariableName"))


# 7. Convert Camel Case to Pascal Case
def camel_to_pascal(text):
    return text[0].upper() + text[1:]

print("7.", camel_to_pascal("myVariable"))


# 8. Convert Pascal Case to Camel Case
def pascal_to_camel(text):
    return text[0].lower() + text[1:]

print("8.", pascal_to_camel("MyVariable"))


# 9. Convert Pascal Case to Snake Case
def pascal_to_snake(text):
    result = ""
    for i in range(len(text)):
        ch = text[i]
        if ch.isupper() and i != 0:
            result = result + "_" + ch.lower()
        else:
            result = result + ch.lower()
    return result

print("9.", pascal_to_snake("MyVariable"))


# 10. Convert Text to Camel Case
def text_to_camel(text):
    words = text.split()
    result = words[0].lower()
    for word in words[1:]:
        result = result + word.capitalize()
    return result

print("10.", text_to_camel("hello world example"))


# 11. Convert Text to Snake Case
def text_to_snake(text):
    return "_".join(text.lower().split())

print("11.", text_to_snake("hello world example"))


# 12. Convert Text to Pascal Case
def text_to_pascal(text):
    words = text.split()
    result = ""
    for word in words:
        result = result + word.capitalize()
    return result

print("12.", text_to_pascal("hello world example"))


# 13. Swap Upper and Lower Case
def swap_case(text):
    return text.swapcase()

print("13.", swap_case("HeLLo"))


# 14. Separate Digits from Text
def extract_digits(text):
    digits = ""
    for ch in text:
        if ch.isdigit():
            digits = digits + ch
    return digits

print("14.", extract_digits("abc123d4"))


# 15. Print Uppercase, Lowercase, Digits and Special Characters Separately
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

print("15.")
print_char_types("Abc123!@#")


# 16. Count of Uppercase, Lowercase, Digits and Special Characters
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
print("16.")
count_char_types("AbC@123x!")


# 17. Check Password Strength
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

print("17.", check_password("Pass123!"))


# 18. Remove Duplicates in a Given Input
def remove_duplicates(text):
    result = ""
    for ch in text:
        if ch not in result:
            result = result + ch
    return result

print("18.", remove_duplicates("aabbcc"))


# 19. Print Duplicates in a Given String
def print_duplicates(text):
    duplicates = []
    for ch in text:
        if text.count(ch) > 1 and ch not in duplicates:
            duplicates.append(ch)
    print(" ".join(duplicates))

print("19.", end=" ")
print_duplicates("aabbccde")


# 20. Print Next Characters in a Given String
def next_characters(text):
    result = ""
    for ch in text:
        result = result + chr(ord(ch) + 1)
    return result

print("20.", next_characters("abc"))
