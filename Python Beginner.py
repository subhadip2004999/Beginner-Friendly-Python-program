import math
import sys
import random

print("Welcome to the Python program that performs various tasks! Its a simple program that can be used to perform basic operations. Beginner friendly.")
print("Choose an option:")
print("1. Calculator")
print("2. Number Properties")
print("3. DSA (Data Structures and Algorithms)")
print("4. Exit")
choice = input("Enter your choice (1-4): ")
if choice == '1':
    print("You chose the calculator.")
    def run_calculator():
        class Calculator:
            def __init__(self):
                print("Welcome to the calculator program!")
                self.a = float(input("Enter First number: "))
                self.b = float(input("Enter Second number: "))
                self.menu()

            def menu(self):
                print("Select operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Modulus")
                print("6. Exponentiation")
                print("7. Floor Division")
                choice = input("Enter your choice (1-7): ")
                a, b = self.a, self.b
                if choice == '1':
                    result = a + b
                    print("Result: ", result)
                elif choice == '2':
                    result = a - b
                    print("Result: ", result)
                elif choice == '3':
                    result = a * b
                    print("Result: ", result)
                elif choice == '4':
                    if b == 0:
                        print("Error! Division by zero.")
                    else:
                        result = a / b
                        print("Result: ", result)
                elif choice == '5':
                    result = a % b
                    print("Result: ", result)
                elif choice == '6':
                    result = a ** b
                    print("Result: ", result)
                elif choice == '7':
                    result = a // b
                    print("Result: ", result)
                else:
                    print("Invalid choice.")

        Calculator()

    run_calculator()
elif choice == '2':
    print("You chose the number properties.")
    def run_number_properties():
        class Numeric_properties:
            def __init__(self, n):
                self.n = n

            def show_properties(self):
                n = self.n
                print(f"Properties for number: {n}")

                print(f"sin({n}) = {math.sin(n)}")
                print(f"cos({n}) = {math.cos(n)}")
                print(f"tan({n}) = {math.tan(n)}")
                print(f"Absolute value: {abs(n)}")

                def is_prime(num):
                    if num < 2 or int(num) != num:
                        return False
                    for i in range(2, int(num ** 0.5) + 1):
                        if num % i == 0:
                            return False
                    return True
                print(f"Prime: {is_prime(n)}")

                def is_palindrome(num):
                    s = str(int(abs(num)))
                    return s == s[::-1]
                print(f"Palindrome: {is_palindrome(n)}")

                def is_armstrong(num):
                    s = str(int(abs(num)))
                    power = len(s)
                    return int(num) == sum(int(d) ** power for d in s)
                print(f"Armstrong: {is_armstrong(n)}")

                print(f"Square root: {math.sqrt(abs(n))}")
                print(f"Cube root: {math.copysign(abs(n) ** (1/3), n)}")

                if n >= 0 and int(n) == n:
                    print(f"Factorial: {math.factorial(int(n))}")
                else:
                    print("Factorial: Not defined for negative or non-integer numbers")

                if n > 0:
                    print(f"log10({n}) = {math.log10(n)}")
                    print(f"ln({n}) = {math.log(n)}")
                else:
                    print("Logarithm: Not defined for non-positive numbers")

                if int(n) == n:
                    print(f"Even: {int(n) % 2 == 0}")
                    print(f"Odd: {int(n) % 2 != 0}")
                else:
                    print("Even/Odd: Not defined for non-integer numbers")

                if int(n) == n:
                    print(f"Binary: {bin(int(n))}")
                    print(f"Octal: {oct(int(n))}")
                    print(f"Hexadecimal: {hex(int(n))}")
                else:
                    print("Binary/Octal/Hexadecimal: Not defined for non-integer numbers")

                print(f"Sign: {'Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'}")

                if int(n) == n:
                    print(f"Multiples of 2: {int(n) % 2 == 0}")
                    print(f"Multiple of 3: {int(n) % 3 == 0}")
                    print(f"Multiple of 5: {int(n) % 5 == 0}")
                    print(f"Multiple of 7: {int(n) % 7 == 0}")
                else:
                    print("Multiples: Not defined for non-integer numbers")

                if n >= 0 and int(n) == n:
                    print(f"Perfect square: {int(math.sqrt(n)) ** 2 == n}")
                else:
                    print("Perfect square: Not defined for negative or non-integer numbers")

                if int(n) == n:
                    print(f"Perfect cube: {round(abs(n) ** (1/3)) ** 3 == abs(n)}")
                else:
                    print("Perfect cube: Not defined for non-integer numbers")

                if int(n) == n:
                    divisors = [i for i in range(1, int(abs(n)) + 1) if int(n) % i == 0]
                    print(f"Divisors: {divisors}")
                else:
                    print("Divisors: Not defined for non-integer numbers")

        try:
            n = float(input("Enter a number: "))
            num = Numeric_properties(n)
            num.show_properties()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    run_number_properties()
elif choice == '3':
    print("You chose DSA (Data Structures and Algorithms).")
    def run_dsa():
        class DSA:
            def __init__(self):
                print("Welcome to the DSA program!")
                self.menu()

            def menu(self):
                print("Select operation:")
                print("1. Sorting Algorithms")
                print("2. Searching Algorithms")
                print("3. Exit")
                list1 = [random.randint(1, 100) for _ in range(10)]
                print("Generated List: ", list1)
                choice = input("Enter your choice (1-3): ")
                if choice == '1':
                    print("You chose Sorting Algorithms.")       
                    print("Sorted List: ", sorted(list1))
                elif choice == '2':
                    print("You chose Searching Algorithms.")
                    target = int(input("Enter the number to search: "))
                    if target in list1:
                        print(f"{target} found in the list.")
                    else:
                        print(f"{target} not found in the list.")
                elif choice == '3':
                    print("Exiting the program.")
                    sys.exit()
                else:
                    print("Invalid choice.")

            def sorting_algorithms(self):
                print("Sorting algorithms will be implemented here.")
                # Placeholder for sorting algorithms
                self.menu()

            def searching_algorithms(self):
                print("Searching algorithms will be implemented here.")
                # Placeholder for searching algorithms
                self.menu()

        DSA()

    run_dsa()
elif choice == '4':
    print("Exiting the program.")
    sys.exit()
     
else:
    print("Invalid choice. Please enter a number between 1 and 4.")