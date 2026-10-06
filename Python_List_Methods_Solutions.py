# Python List Methods Tasks


# 1. Add an Element
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers.append(60)
print("After append:", numbers)


# 2. Add Multiple Elements
students = ["Rahul", "Priya", "Amit"]
print("Original list:", students)

students.extend(["Sneha", "Kiran", "Divya"])
print("After extend:", students)


# 3. Insert at Specific Position
items = [10, 20, 30, 40]
print("Original list:", items)

items.insert(0, 5)                    # beginning
print("Insert at beginning:", items)

items.insert(len(items) // 2, 25)     # middle
print("Insert at middle:", items)

items.insert(len(items), 50)          # end
print("Insert at end:", items)


# 4. Remove a Specific Element
numbers = [10, 20, 30, 20, 40, 20]
print("Original list:", numbers)

numbers.remove(20)
print("After removing first 20:", numbers)


# 5. Remove Element by Position
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

index = int(input("Enter the index to remove: "))
removed = numbers.pop(index)

print("Removed element:", removed)
print("Updated list:", numbers)


# 6. Remove Last Element
fruits = ["apple", "banana", "mango", "orange"]
print("Original list:", fruits)

removed = fruits.pop()
print("Removed element:", removed)
print("Updated list:", fruits)


# 7. Find Occurrence Count
numbers = [1, 2, 3, 2, 4, 2, 5]
value = 2

print("List:", numbers)
print("Number of times", value, "occurs:", numbers.count(value))


# 8. Find Position of an Element
colors = ["red", "green", "blue", "yellow"]
element = "blue"

print("List:", colors)
print("Index of", element, "is:", colors.index(element))


# 9. Sort Numbers in Ascending Order
numbers = [40, 10, 50, 30, 20]
print("Original list:", numbers)

numbers.sort()
print("Ascending order:", numbers)


# 10. Sort Numbers in Descending Order
numbers = [40, 10, 50, 30, 20]
print("Original list:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)


# 11. Reverse a List
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)


# 12. Clear a List
items = ["pen", "book", "bag", "bottle"]
print("Before clear:", items)

items.clear()
print("After clear:", items)


# 13. Create an Independent Copy
original = [1, 2, 3, 4, 5]
copied = original.copy()

copied.append(6)
copied[0] = 100

print("Original list:", original)
print("Copied list:", copied)
print("Same list object?", original is copied)


# 14. Merge Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("List 1:", list1)
print("List 2:", list2)

list1.extend(list2)
print("After merging:", list1)


# 15. Student Marks Processing
marks = [78, 92, 65, 88, 70]
print("Original marks:", marks)

marks.append(95)
print("After adding 95:", marks)

marks.remove(65)
print("After removing 65:", marks)

marks.sort()
print("After sorting:", marks)

marks.reverse()
print("After reversing:", marks)


# 16. Shopping Cart
cart = ["milk", "bread", "eggs", "rice", "sugar"]
print("Cart:", cart)

cart.append("butter")
print("After adding butter:", cart)

cart.insert(2, "apple")
print("After inserting apple at position 2:", cart)

cart.remove("eggs")
print("After removing eggs:", cart)

cart.pop()
print("After removing the last item:", cart)


# 17. Duplicate Detection
numbers = [10, 20, 30, 20, 40, 50, 10]
print("List:", numbers)

num = int(input("Enter a number: "))

if numbers.count(num) > 1:
    print(num, "appears more than once.")
else:
    print(num, "does not appear more than once.")


# 18. Move an Element
numbers = [10, 20, 30, 40, 50]
element = 40
print("Original list:", numbers)

numbers.remove(element)
numbers.insert(0, element)
print("After moving", element, "to the beginning:", numbers)


# 19. Second Largest Number
numbers = [12, 45, 7, 89, 34, 89, 23]
print("List:", numbers)

numbers.sort(reverse=True)
largest = numbers[0]

second_largest = None
for n in numbers:
    if n != largest:
        second_largest = n
        break

print("Sorted list:", numbers)
print("Second largest number:", second_largest)


# 20. List Method Challenge
numbers = [40, 10, 20, 40, 30, 20, 50]

numbers.append(60)
print("After adding 60:", numbers)

numbers.insert(0, 5)
print("After inserting 5 at index 0:", numbers)

print("Count of 20:", numbers.count(20))
print("Index of 40:", numbers.index(40))

numbers.remove(40)
print("After removing first 40:", numbers)

numbers.pop()
print("After removing last element:", numbers)

numbers.sort(reverse=True)
print("After sorting in descending order:", numbers)

copied = numbers.copy()
numbers.clear()

print("Original list:", numbers)
print("Copied list:", copied)
