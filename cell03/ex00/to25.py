A = int(input("Enter a number less than 25\n"))
if A > 25:
    print("ERROR")
else:
    while A-1 != 25:
        print(f"Inside the loop, my variable is {A}")
        A += 1