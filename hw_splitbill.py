try:
    billamount = float(input("Bill amount in dollars: "))
    tip = float(input("Percent tip: "))
    people = float(input("Number of people: "))
except ValueError:
    quit("Please enter a numerical value.")


totalamount = billamount + tip
print("The tip is {:.2f} dollars".format(tip))
print("The total cost is {:.2f} dollars.".format(totalamount))

perperson = totalamount/ people

print("The cost per person is {:.2f} dollars".format(perperson))
