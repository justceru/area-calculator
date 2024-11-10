print("""
==================
Area Calculator 📐
==================

1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit
      
""")
try:
    choose = int(input("Which shape: "))
    if choose == 1:
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area}")
    elif choose == 2:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"The area of the rectangle is {area}")
    elif choose == 3:
        side = float(input("Enter the side: "))
        area = side ** 2
        print(f"The area of the square is {area}")
    elif choose == 4:
        radius = float(input("Enter the radius: "))
        area = 3.14 * radius ** 2
        print(f"The area of the circle is {area}")
    elif choose == 5:
        print("Goodbye!")
    else:
        print("Invalid choice!")
except ValueError:
    print("Invalid input! Please enter a number.")