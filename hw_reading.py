#ask user how many pages they haev to read and how
#many days they have left, keep track of daily
#number of pages read and return how many 
#pages are needed each day.

try:
    totalpages = int(input("pages to read? "))
    totaldays = int(input("days until due? "))
except ValueError:
    quit("Please enter numerical values")

def main(pages, days):
    i = 1
    totalread = 0
    while i <= days:
        try:
            daypages = int(input("Pages for day {}: ".format(i)))
        except ValueError:
            quit("Please enter a numerical value")
        
        totalread += daypages
        print("You've read {} out of {} pages.".format(totalread, pages))
        print()

        remainingpages = pages - totalread
        
        if totalread > pages:
            print("Error: pages read exceed number of pages in book.")
            return
        remainingdays = days - i
        
        if remainingdays == 1:
            print("** You've got {} pages left and 1 day to go.".format(remainingpages))
        else:
            print("** You've got {} pages left and {} days to go.".format(remainingpages, remainingdays))
        i += 1
    
main(totalpages, totaldays)