print("This program will find the roots of a quadratic equation")
print("The standard form of a quadratic equation is : \n")

# For those who don't know,
# x**y is x raised to power y
print("ax**2 + bx + c")

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

d = b**2 - 4*a*c

if d < 0:
    print("The roots are imaginary")
else:
    x = (-b -d) / 2*a
    y = (-b +d) / 2*a
    print(f"The roots of the quadratic equation {a}x**2 + {b}x + {c} are {x} and {y}")
