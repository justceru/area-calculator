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
choose = 0
valid = False
while valid != True:
  try:
    choose = int(input("Which shape: "))
    if choose == 1:
      valid = True
      base = float(input("Base: "))
      height = float(input("Height: "))
      print(f'The area is {height * base / 2}')
    elif choose == 2:
      valid = True
      length = float(input("Length: "))
      width = float(input("Width: "))
      print(f'The area is {length * width}')
    elif choose == 3:
      valid = True
      side = float(input("Side: "))
      print(f'The area is {side ** 2}')
    elif choose == 4:
      valid = True
      radius = float(input("Radius: "))
      print(f'The area is {round((3.14 * radius ** 2), 2)}')
    elif choose == 5:
      valid = True
      print("See you later!")
    else:
      print("Invalid choice, please choose again.")
  except (ValueError, TypeError):
    valid = False
    print("Invalid choice, please choose again.")
