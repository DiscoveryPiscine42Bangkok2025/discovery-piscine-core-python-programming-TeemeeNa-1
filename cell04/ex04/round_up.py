A = float(input("Give me a number: "))
if A - int(A) != 0:
    A = int(A) + 1
else:
    A = int(A)
print(f"{A}")
