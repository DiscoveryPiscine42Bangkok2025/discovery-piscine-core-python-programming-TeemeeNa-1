first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number:\n"))
com = first * second
print(f"{first} x {second} = {com}")
if com > 0:
    print("The result is positive.")
elif com < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
