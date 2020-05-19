#takes user text as an input and arranges 
#it vertically such that the first half of 
#the text is on the left side of the line 
#and the second half is on the right side.
#If the length of the string is odd, the right
#side contains one more character than left

userinput = input("text: ")

def main(text):
    numchars = len(text)
    mid = numchars // 2
    i = 0
    while i < mid:
        line = text[i] + "|"
        print(line)
        i += 1
    while i < len(text):
        line = " |" + text[i]
        print(line)
        i += 1

main(userinput)