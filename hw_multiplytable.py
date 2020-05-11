factor = input("Factor: ")
factor = int(factor)

firstline = "n | {} * n".format(factor)
print(firstline)
print("-" * 10)

i = 1
while i < 10:
    rightside = i * factor
    print("{} | {}".format(i, rightside))
    i += 1
    