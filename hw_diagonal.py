#takes user input as a string and displays 
#the string diagonally, 3 characters at a time
userinput = input("text: ")

def main(text):
    i = 0 
    numspaces = 0
    while i < (len(text)-2):
        line = numspaces * " " + text[i:i + 3]
        print(line)
        i += 1
        numspaces += 3
main(userinput)
