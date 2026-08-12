Pattern-Based Programming Questions (All 34 Questions - Interview Style)
________________________________________
🔷 Square, Rectangle, and Triangle Patterns (1–15)
1.	Solid Square Pattern
Problem: Print a solid square of stars of size n.
Input: n = 4
Output:
* * * *
* * * *
* * * *
* * * *

n = 4

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

OUTPUT:
* * * *
* * * *
* * * *
* * * *

2.	Solid Rectangle Pattern
Problem: Print a solid rectangle of m rows and n columns.
Input: m = 3, n = 5
Output:
* * * * *
* * * * *
* * * * *

m = 3
n = 5

for i in range(m):
    for j in range(n):
        print("*", end=" ")
    print()

OUTPUT:
* * * * *
* * * * *
* * * * *

3.	Right-Angled Triangle (Left-Aligned)
Problem: Print a left-aligned right-angled triangle.
Input: n = 5
Output:
*
* *
* * *
* * * *
* * * * *
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

OUTPUT:

*
* *
* * *
* * * *
* * * * *



4.	Right-Angled Triangle (Right-Aligned)
Input: n = 5
Output:
        *
      * *
    * * *
  * * * *
* * * * *
n = 5

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

OUTPUT:


        *
      * *
    * * *
  * * * *
* * * * *


5.	Inverted Triangle (Left-Aligned)
Input: n = 5
Output:
* * * * *
* * * *
* * *
* *
*

n = 5

for i in range(n, 0, -1):
    print("* " * i)

OUTPUT:

* * * * *
* * * *
* * *
* *
*

6.	Inverted Triangle (Right-Aligned)
Input: n = 5
Output:
* * * * *
  * * * *
    * * *
      * *
        *
n = 5

for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)


OUTPUT:

* * * * *
  * * * *
    * * *
      * *
        *

7.	Centered Pyramid Pattern
Input: n = 4
Output:
      *
    * * *
  * * * * *
* * * * * * *

n = 4

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))


OUTPUT:

      *
    * * *
  * * * * *
* * * * * * *

8.	Diamond Pattern
Input: n = 3
Output:
    *
  * * *
* * * * *
  * * *
    *

n = 3

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))


OUTPUT:

    *
  * * *
* * * * *
  * * *
    *

9.	Butterfly Pattern
Input: n = 4
Output:
*       *
* *   * *
* * * * *
* *   * *
*       *
n = 4

for i in range(1, n + 1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i + "  " * (2 * (n - i)) + "* " * i)


OUTPUT:

*             *
* *         * *
* * *     * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *

10.	Left-Aligned Half Diamond
Input: n = 4
Output:
*
* *
* * *
* * * *
* * *
* *
*
n = 4

for i in range(1, n + 1):
    print("* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i)


OUTPUT:

*
* *
* * *
* * * *
* * *
* *
*

11.	Right-Aligned Half Diamond
Input: n = 4
Output:
      *
    * *
  * * *
* * * *
  * * *
    * *
      *
n = 4

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * i)

OUTPUT:

      *
    * *
  * * *
* * * *
  * * *
    * *
      *

12.	Sandglass Pattern
Input: n = 4
Output:
* * * *
  * * *
    * *
      *
    * *
  * * *
* * * *

n = 4

for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

for i in range(2, n + 1):
    print("  " * (n - i) + "* " * i)

OUTPUT:


* * * *
  * * *
    * *
      *
    * *
  * * *
* * * *

13.	Increasing Width Triangle
Input: n = 5
Output:
*
* *
* * *
* * * *
* * * * *
n = 5

for i in range(1, n + 1):
    print("* " * i)

OUTPUT:

*
* *
* * *
* * * *
* * * * *

14.	Decreasing Width Triangle
Input: n = 5
Output:
* * * * *
* * * *
* * *
* *
*

n = 5

for i in range(n, 0, -1):
    print("* " * i)


OUTPUT:

* * * * *
* * * *
* * *
* *
*

15.	Right-Aligned Hill Pattern
Input: n = 4
Output:
      *
    * *
  * * *
* * * *
n = 4

for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)


OUTPUT:

      *
    * *
  * * *
* * * *
________________________________________
🔲 Hollow Patterns (16–25)
16.	Hollow Square Pattern
Problem: Print a hollow square of stars of size n.
Input: n = 4
Output:
* * * *
*     *
*     *
* * * *

n = 4

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


OUTPUT:

* * * *
*     *
*     *
* * * *


17.	Hollow Rectangle Pattern
Problem: Print a hollow rectangle of m rows and n columns.
Input: m = 4, n = 5
Output:
* * * * *
*       *
*       *
* * * * *

m = 4
n = 5

for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

OUTPUT:

* * * * *
*       *
*       *
* * * * *

18.	Hollow Right-Angled Triangle (Left-Aligned)
Input: n = 5
Output:
*
* *
*   *
*     *
* * * * *

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


OUTPUT:

*
* *
*   *
*     *
* * * * *


19.	Hollow Right-Angled Triangle (Right-Aligned)
Input: n = 5
Output:
        *
      * *
    *   *
  *     *
* * * * *

n = 5

for i in range(1, n + 1):
    print("  " * (n - i), end="")

    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("* ", end="")
        else:
            print("  ", end="")
    
    print()


OUTPUT:

        *
      * *
    *   *
  *     *
* * * * *

20.	Hollow Inverted Triangle (Left-Aligned)
Input: n = 5
Output:
* * * * *
*     *
*   *
* *
*

n = 5

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


OUTPUT:

* * * * *
*     *
*   *
* *
*

21.	Hollow Inverted Triangle (Right-Aligned)
Input: n = 5
Output:
* * * * *
  *     *
    *   *
      * *
        *

n = 5

for i in range(n, 0, -1):
    print("  " * (n - i), end="")

    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("* ", end="")
        else:
            print("  ", end="")

    print()


OUTPUT:

* * * * *
  *     *
    *   *
      * *
        *

22.	Hollow Pyramid Pattern
Input: n = 4
Output:
      *
    *   *
  *       *
* * * * * * *

n = 4

for i in range(1, n + 1):
    print("  " * (n - i), end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("* ", end="")
        else:
            print("  ", end="")

    print()

OUTPUT:

      *
    *   *
  *       *
* * * * * * *


23.	Hollow Diamond Pattern
Input: n = 3
Output:
    *
  *   *
*       *
  *   *
    *

n = 3

for i in range(1, n + 1):
    print("  " * (n - i), end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("* ", end="")
        else:
            print("  ", end="")

    print()

for i in range(n - 1, 0, -1):
    print("  " * (n - i), end="")

    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("* ", end="")
        else:
            print("  ", end="")

    print()


OUTPUT:

    *
  *   *
*       *
  *   *
    *


24.	Hollow Butterfly Pattern
Input: n = 4
Output:
*       *
* *   * *
*   *   *
*       *
*   *   *
* *   * *
*       *

n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print("  " * (2 * (n - i)), end="")

    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print("  " * (2 * (n - i)), end="")

    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


OUTPUT:

*             *
* *         * *
*   *     *   *
*     * *     *
*     * *     *
*   *     *   *
* *         * *
*             *



25.	Hollow Hourglass Pattern
Input: n = 5
Output:
* * * * *
*       *
  *   *
    *
  *   *
*       *
* * * * *

n = 5

# Top
print("* " * n)

# Upper hollow part
for i in range(1, n - 2):
    print("  " * i, end="")
    
    for j in range(n - i):
        if j == 0 or j == n - i - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    
    print()

# Middle
print("  " * 2 + "*")

# Lower hollow part
for i in range(n - 3, 0, -1):
    print("  " * i, end="")
    
    for j in range(n - i):
        if j == 0 or j == n - i - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    
    print()

# Bottom
print("* " * n)


OUTPUT:

* * * * *
*       *
  *   *
    *
  *   *
*       *
* * * * *
________________________________________
🔢 Number-Based Patterns (26–34)
26.	Increasing Number Triangle
Problem: Print numbers from 1 to n in triangle form.
Input: n = 5
Output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

OUTPUT:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

27.	Repeating Row Number Triangle
Input: n = 5
Output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()


OUTPUT:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5


28.	Continuous Number Triangle
Input: n = 4
Output:
1
2 3
4 5 6
7 8 9 10

n = 4
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


OUTPUT:

1
2 3
4 5 6
7 8 9 10


29.	Reverse Row Number Triangle
Input: n = 5
Output:
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

n = 5

for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

OUTPUT:

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1

30.	Inverted Number Triangle
Input: n = 5
Output:
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

n = 5

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


OUTPUT:

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

31.	Right-Aligned Number Triangle
Input: n = 5
Output:
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

n = 5

for i in range(1, n + 1):
    print("  " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()


OUTPUT:

        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

32.	Pyramid Number Pattern
Input: n = 4
Output:
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1

n = 4

for i in range(1, n + 1):
    print("  " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()


OUTPUT:

      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1

33.	Even Number Triangle
Input: n = 5
Output:
2
2 4
2 4 6
2 4 6 8
2 4 6 8 10

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(2 * j, end=" ")
    print()


OUTPUT:

2
2 4
2 4 6
2 4 6 8
2 4 6 8 10

34.	Odd Number Triangle
Input: n = 5
Output:
1
1 3
1 3 5
1 3 5 7
1 3 5 7 9

n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")
    print()


OUTPUT:

1
1 3
1 3 5
1 3 5 7
1 3 5 7 9

