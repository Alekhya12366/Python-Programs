1. What does “scope” mean in Python?
 A. The size of a variable
 B. The region where a variable can be accessed
 C. The data type of a variable
 D. The lifetime of a program
Ans: B. The region where a variable can be accessed


2. Which rule does Python use to find a variable?
 A. FIFO
 B. LIFO
 C. LEGB
 D. FILO
Ans: C. LEGB

3. What does LEGB stand for?
 A. Local, External, Global, Built-in
 B. Local, Enclosing, Global, Built-in
 C. Local, Enclosing, General, Basic
 D. Local, Global, Enclosing, Built-in
Ans: B. Local, Enclosing, Global, Built-in


4. A variable created inside a function normally has what scope?
 A. Global
 B. Built-in
 C. Local
 D. Enclosing
Ans: C. Local


5. What is the output?
x = 10

def test():
    x = 20
    print(x)

test()
A. 10
 B. 20
 C. 30
 D. Error
Ans: B. 20




6. What is the output?
x = 10

def test():
    print(x)

test()
A. 0
 B. 10
 C. None
 D. Error
Ans: B. 10



7. Which keyword is used to modify a global variable inside a function?
 A. global
 B. extern
 C. public
 D. outer
Ans: A. global   



8. What is the output?
x = 10

def change():
    global x
    x = 20

change()
print(x)
A. 10
 B. 20
 C. None
 D. Error
Ans: B.20





9. What happens here?
x = 10

def change():
    x = x + 5
    print(x)

change()
A. Prints 15
 B. Prints 10
 C. Raises an error
 D. Prints 5
Ans: C. Raises an error 



10. Which keyword allows a nested function to modify a variable in its enclosing function?
 A. global
 B. local
 C. nonlocal
 D. outer
Ans: C. nonlocal


11. What is the output?
def outer():
    x = 10

    def inner():
        print(x)

    inner()

outer()
A. 0
 B. 10
 C. Error
 D. None
Ans: B. 10



12. What is the output?
x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)

    inner()

outer()
A. global
 B. enclosing
 C. local
 D. Error
Ans: B.  enclosing


13. Which scope is searched first according to LEGB?
 A. Global
 B. Built-in
 C. Enclosing
 D. Local
Ans: D. Local


14. Which scope is searched last according to LEGB?
 A. Local
 B. Enclosing
 C. Global
 D. Built-in
Ans: D. Built-in 


15. What is the output?
x = 100

def fun():
    x = 50
    print(x)

fun()
print(x)
A. 50, 50
 B. 100, 100
 C. 50, 100
 D. 100, 50
Ans: C. 50,100




16. What is the output?
def fun():
    y = 20

fun()
print(y)
A. 20
 B. 0
 C. None
 D. NameError
Ans: D. NameError


17. Which variable is accessible throughout a module, unless shadowed?
 A. Local variable
 B. Global variable
 C. Enclosing variable
 D. Temporary variable
Ans: B. Global variable



18. What is the output?
x = 5

def fun():
    print(x)
    x = 10

fun()
A. 5
 B. 10
 C. UnboundLocalError
 D. NameError
Ans:  C. UnboundLocalError


19. Why does Question 18 produce an error?
 A. x cannot be printed
 B. Assignment makes x local to the function
 C. Global variables cannot be used in functions
 D. Python does not support reassignment
Ans: B. Assignment makes x local to the function




20. What is the output?
x = 10

def fun():
    global x
    x += 5

fun()
print(x)
A. 10
 B. 15
 C. 5
 D. Error
Ans: B. 15



21. What is the output?
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)

outer()
A. 10
 B. 20
 C. Error
 D. None
Ans: B. 20



22. What does nonlocal refer to?
 A. A variable in the global scope
 B. A variable in the built-in scope
 C. A variable in an enclosing function scope
 D. A variable outside Python
Ans:  C. A variable in an enclosing function scope




23. Which of the following is an example of a built-in name?
 A. my_variable
 B. x
 C. len
 D. total
Ans: C. len



24. What is the output?
def fun():
    print(len([1, 2, 3]))

fun()
A. 2
 B. 3
 C. 1
 D. Error
Ans: B.3


25. What is variable shadowing?
 A. Deleting a variable
 B. Creating a variable with the same name in a narrower scope
 C. Making a variable global
 D. Copying a variable
Ans: B. Creating a variable with the same name in a narrower scope



26. What is the output?
x = 1

def outer():
    x = 2

    def inner():
        x = 3
        print(x)

    inner()

outer()
A. 1
 B. 2
 C. 3
 D. Error
Ans: C.3 


27. What is the output?
x = 1

def outer():
    x = 2

    def inner():
        print(x)

    inner()

outer()
A. 1
 B. 2
 C. Error
 D. None
Ans: B.2 



28. Which statement about local variables is TRUE?
 A. They are always accessible outside the function
 B. They are normally accessible only within the function where they are defined
 C. They are always global
 D. They can only contain numbers
Ans: B. They are normally accessible only within the function where they are defined



29. What is the output?
x = 10

def outer():
    x = 20

    def inner():
        nonlocal x
        x += 5

    inner()
    print(x)

outer()
A. 10
 B. 20
 C. 25
 D. Error
Ans: C. 25



30. What will Python do if a name is not found in Local, Enclosing, Global, or Built-in scope?
 A. Create the variable automatically
 B. Return None
 C. Raise a NameError
 D. Search the internet
Ans: C. Raise a NameError





