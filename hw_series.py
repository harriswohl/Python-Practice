#estimates the sum of an infinite series
#based on the number of terms given by user input
try:
    userterms = int(input("number of terms: "))
except ValueError:
    quit("Please enter a numeric value")

def main(terms):
        sum = 0 
        i = 1 
        while i <= terms:
            term = 1/(i**2)
            sum += term
            left = str(i) + ": "
            right = "{:.5f}".format(sum)
            print(left + right)
            i += 1
        return("")
        
print(main(userterms))           

            
