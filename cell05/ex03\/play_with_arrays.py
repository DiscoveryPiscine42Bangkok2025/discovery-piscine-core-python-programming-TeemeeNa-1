A = [2, 8, 9, 48, 8, 22, -12, 2]
new = [x + 2 for x in A if x >= 8]
last = list(set(new))

print(last)
