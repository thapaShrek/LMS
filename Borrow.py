from datetime import date, datetime


def borrowbook():
    global number, borrow_price, books_borrow
    borrow_price = 0
    books_borrow = ""
    number = []
    borrowednote = ""
    file = open('stock.txt', 'r')
    book = file.readlines()
    file.close()

    for j in book:
        x = j.replace("\n","").split(",")
        number.append(x)

    updatedinfo = ""
    borrowdate = date.today()
    borroweddate = str(borrowdate.strftime("%d/%m\%Y"))
    borrowtime = datetime.now()
    borrowedtime = str(borrowtime.strftime("%H:%M"))
    books_enter = []
    borrowing = "yes"
    borrowed = False
    details = ""
    borrowfile = ""

    Fullname = str(input("Enter your full name: "))
        
    #text is used for naming convention of text file
    text = "Borrowed by " + Fullname + ".txt"


    #creates a new text file when a new user borrows a book
    with open(text,"w+") as file:
        file.write("\t\t Library of Kathmandu\n")
        file.write("\t\tBorrowed by: " + Fullname + "\n")
        file.write("    \t Date: " + borroweddate +"  \t   Time:" + borrowedtime )
        file.write("\nS.N.\t\tBook\t\t\t\t\tTotal Price")

    #This loop will run until borrowing == "yes"
    while borrowing.lower() == "yes":

        print("\nInput the value as suggested only.")
        print("Enter 1 to borrow 'Days Without End'")
        print("Enter 2 to borrow 'Fugitive Pieces'")
        print("Enter 3 to borrow 'The Hobbit'")
        #try:
        select = int(input("Enter a number to borrow a book: "))
    #except :
      #  print("\nPlease enter suggested values only.\n")
      #  exit()

        if select == 1:

            for i in books_enter:
                #checking if book has already been borrowed or not
                if len(books_enter) > 1 and books_enter[i] == 1:
                    borrowed = True
                    break
                else:
                    borrowed = False

            if borrowed == True:
                print("\nThe book has been borrowed already.")

            else:
                #Checking if book is available or not
                if int(number[0][2]) > 0:
                    books_enter.append(select)
                    number[0][2] = str(int(number[0][2]) - 1)
                    borrow_price = borrow_price + float(number[0][3].replace("$",""))
                    books_borrow = books_borrow + "|   " + "Days Without End" + " | "
                    print("\nThe total cost of the book is ",borrow_price)

                else:
                    print("The book is not available")

        elif select == 2:
            for i in books_enter:
                #Checking if book 2 has already been borrowed
                if (len(books_enter) > 0 and books_enter[i] == 2):
                    borrowed = True
                    break
                else:
                    borrowed = False
            if borrowed == True:
                print('The book has been borrowed already.')
            else:
                if int(number[1][2]) > 0:
                    #Reducing the quantity of book after borrow process
                    books_enter.append(select)
                    number[1][2] = str(int(number[1][2]) - 1)
                    borrow_price =  borrow_price + float(number[1][3].replace("$",""))
                    books_borrow =  books_borrow + " | "  +"Fugitive Pieces" + " | "

                else:
                    print("The book is not available")

        elif select == 3:
            for i in books_enter:
                # Checking if book 3 has already been borrowed
                if len(books_enter) > 1 and books_enter[i] == 1:
                    borrowed = True
                    break
                else:
                    borrowed = False

            if borrowed == True:
                print("The book has been borrowed already.")

            else:
                if int(number[2][2]) > 0:
                    # Reducing the quantity of book after borrow process
                    books_enter.append(select)
                    number[2][2] = str(int(number[2][2]) - 1)
                    borrow_price = borrow_price + float(number[1][3].replace("$",""))
                    books_borrow = books_borrow + " |   "+"The Hobbit" + " |  "

                else:
                    print("The book is not available.")

        borrowing = str(input("\nDo you want to borrow more books?\nType yes or no\t"))
    if borrowing == "no":
        #Creating note to be entered in the text file
        borrowednote = ("1" + "\t\t "  + books_borrow + "\t\t\t" + "$" + str(borrow_price))
        borrowfile = ("1" + "\t "  + books_borrow + "\t\t\t" + "$" + str(borrow_price))
        for i in range(len(number)):
            lang = ""
            for j in range(len(number[i])):
                if j == len(number[i]) - 1:
                    lang = lang + number[i][j] + "\n"
                else:
                    lang = lang + number[i][j] + ","
            #Deducting the quantity of book in stock.txt file
            updatedinfo = updatedinfo + lang
        print("\n\t\t\t Updated list of books \n-------------------------------------------------\n")
        print(updatedinfo)
        #Printing bill in the shell
        print("\t\t \t\t\tLibrary of Kathmandu\n")
        print("\t\t\t\t\tBorrowed by: ",Fullname)
        print("    \t\tDate: " + borroweddate +"   \t\t Time:" + borrowedtime +"\n\n")
        print("S.N.\t\t\t\tBook\t\t\t\tTotal Price")

        print(borrowednote)
        print("\t\t\t\t\t\t\t\tTotal cost: $",str(borrow_price))
        print("\n[Note: The borrowed book must be returned within 10 days.]\n")

        #Updating the new list to the stock.txt file
        infobor = open("stock.txt","w")
        infobor.write(updatedinfo)
        infobor.close()

        #New text file to store name of borrower
        borrowerlist = open("Borrowers Name.txt","w+")
        borrowerlist.write(Fullname + "\n")
        borrowerlist.close()

        with open(text,"a") as file:
            file.write("\n" + borrowfile)
    else:
        print("Please input suggested value only.")
























