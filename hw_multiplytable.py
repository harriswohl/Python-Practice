factor = input("Factor: ")
try:
    factor = int(factor)
except ValueError:
    quit("Please enter an integer.")

firstline = "n | {} * n".format(factor)
print(firstline)
print("-" * 10)

i = 1
while i < 10:
    rightside = i * factor
    print("{} | {}".format(i, rightside))
    i += 1
    