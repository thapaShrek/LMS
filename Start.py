import Borrow
import Return

def start():
    # to run same loop again
    while(True):
        print("\t\t\t\nWelcome to the Library of Kathmandu \t\t\t")
        print("-----------------------------------------------------------------------\n")
        print("Enter 1 to display")
        print("Enter 2 to borrow a book")
        print("Enter 3 to return a book")
        print("Enter 4 to exit\n")
        # try to catch exception
        try:
            val = int(input("Enter a number:  "))

            if val == 1:
                # opens stock.txt file in reading mode
                file = open('stock.txt', 'r')
                print(file.read())
                file.close()


            elif val == 2:
                #calling borrowbook() function
                Borrow.borrowbook()

            elif val == 3:
                #calling returnbook() function
                Return.returnbook()

            elif val == 4:
                print("\nThank you for visiting Library of Kathmandu.")
                #Breaking the loop
                break

            else:
                print("Enter a valid value between 1-4.\n")

        except ValueError:
            print("Please input suggested value only.\n")
start()
