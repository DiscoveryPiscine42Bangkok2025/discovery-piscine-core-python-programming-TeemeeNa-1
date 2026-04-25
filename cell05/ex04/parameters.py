A = input("")
B = A.split()
C = len(B)
count = 0
while count != C:
    print(B[count],end=" ")
    count += 1
print("")
print(f"Number of parameters: {C}")
