# allpy.py
print("Welcome to the Python program!")


# Generate a switch of 30 cases with titles for each practical
switch = {
    1: lambda: (
        print("Practical 1: Implementing User Data Input and Display"), 
        user_input := input("Please enter some data: "), 
        print("You entered:", user_input)
    ),
    2: lambda: (
        print("Practical 2: Implement a python programs using following operators"),
        # Identity Operations
        a := [1, 2, 3],
        b := [1, 2, 3],
        c := a,
        print("\nIdentity Operations:"),
        print("a is b:", a is b),
        print("a is not b:", a is not b),
        print("a is c:", a is c),
        
        # Membership Operations
        fruits := ["apple", "banana", "cherry"],
        print("\nMembership Operations:"),
        print("'apple' in fruits:", 'apple' in fruits),
        print("'orange' not in fruits:", 'orange' not in fruits),
        
        # Bitwise Operations
        x := 0b1010,  # Binary 10
        y := 0b1100,  # Binary 12
        print("\nBitwise Operations:"),
        print("x & y:", x & y),
        print("x | y:", x | y),
        print("x ^ y:", x ^ y),
        print("~x:", ~x),
        print("x << 2:", x << 2),
        print("x >> 2:", x >> 2),
        
        # Assignment and Arithmetic Operations
        num := 10,
        print("\nArithmetic and Assignment Operations:"),
        print("Initial num:", num),
        num := num + 5,
        print("After adding 5:", num),
        num := num * 2,
        print("After multiplying by 2:", num),
        
        # Relational and Logical Operations
        p := 10,
        q := 20,
        print("\nRelational and Logical Operations:"),
        print("p > q:", p > q),
        print("p < q:", p < q),
        print("p and q > 0:", p > 0 and q > 0),
        print("p > 20 or q > 15:", p > 20 or q > 15)
    ),
    3: lambda: (
        print("Practical 3: Implementing Control Structures"),
        def lader():
            score = 85
            print("\nGrade Calculation:")
            print("Score:", score)
            if score >= 90:
                print("Grade: A")
            elif score >= 80:
                print("Grade: B")
            elif score >= 70:
                print("Grade: C")
            else:
                print("Grade: D")
        lader()
        
        def nesting():
            age = 25
            student = True
            print("\nAge and Student Status Check:")
            print("Age:", age)
            if student:
                print("Student Status: Student")
            else:
                print("Student Status: Not a student")
            if age >= 18:
                print("You are an adult")
                if student:
                    print("Status: Adult student")
                else:
                    print("Status: Adult non-student")
            else:
                print("You are a minor")
                print("Status: Minor")
        nesting()
    ),
    4: lambda: print("Practical 4: Title Here"),  # Insert code for Practical 4
    5: lambda: print("Practical 5: Title Here"),  # Insert code for Practical 5
    6: lambda: print("Practical 6: Title Here"),  # Insert code for Practical 6
    7: lambda: print("Practical 7: Title Here"),  # Insert code for Practical 7
    8: lambda: print("Practical 8: Title Here"),  # Insert code for Practical 8
    9: lambda: print("Practical 9: Title Here"),  # Insert code for Practical 9
    10: lambda: print("Practical 10: Title Here"),  # Insert code for Practical 10
    11: lambda: print("Practical 11: Title Here"),  # Insert code for Practical 11
    12: lambda: print("Practical 12: Title Here"),  # Insert code for Practical 12
    13: lambda: print("Practical 13: Title Here"),  # Insert code for Practical 13
    14: lambda: print("Practical 14: Title Here"),  # Insert code for Practical 14
    15: lambda: print("Practical 15: Title Here"),  # Insert code for Practical 15
    16: lambda: print("Practical 16: Title Here"),  # Insert code for Practical 16
    17: lambda: print("Practical 17: Title Here"),  # Insert code for Practical 17
    18: lambda: print("Practical 18: Title Here"),  # Insert code for Practical 18
    19: lambda: print("Practical 19: Title Here"),  # Insert code for Practical 19
    20: lambda: print("Practical 20: Title Here"),  # Insert code for Practical 20
    21: lambda: print("Practical 21: Title Here"),  # Insert code for Practical 21
    22: lambda: print("Practical 22: Title Here"),  # Insert code for Practical 22
    23: lambda: print("Practical 23: Title Here"),  # Insert code for Practical 23
    24: lambda: print("Practical 24: Title Here"),  # Insert code for Practical 24
    25: lambda: print("Practical 25: Title Here"),  # Insert code for Practical 25
    26: lambda: print("Practical 26: Title Here"),  # Insert code for Practical 26
    27: lambda: print("Practical 27: Title Here"),  # Insert code for Practical 27
    28: lambda: print("Practical 28: Title Here"),  # Insert code for Practical 28
    29: lambda: print("Practical 29: Title Here"),  # Insert code for Practical 29
    30: lambda: print("Practical 30: Title Here"),  # Insert code for Practical 30
}

# Example of how to call a specific practical
case_number = int(input("Enter the case number (1-30): "))
if case_number in switch:
    switch[case_number]()
else:
    print("Invalid case number.")