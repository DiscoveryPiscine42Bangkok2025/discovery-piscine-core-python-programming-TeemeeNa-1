A = float(input("Give me a number: "))
if A - int(A) != 0:
    T = "decimal"
else:
    T = "integer"
print(f"This number is {T}")
