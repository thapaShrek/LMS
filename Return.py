#importing date and time
from datetime import date, datetime

def returnbook():

    returnlist = []
    returnfee = 0
    booksreturn = ""
    extrareturn = "yes"
    file = open('stock.txt', 'r')
    info = file.readlines()
    file.close()
    for j in info:
        x = j.replace("\n", "").split(",")
        returnlist.append(x)
    returndate = date.today()
    returneddate = str(returndate.strftime("%d/%m\%Y"))
    returntime = datetime.now()
    returnedtime = str(returntime.strftime("%H:%M"))
    file = open("Borrowers Name.txt", "r")
    borrowerlist = file.readlines()
    file.close()
    returnfile = ""

    name = input("Enter your full name: ")

    #txtfile to create new text file for the book returner
    txtfile = "Returned by " + name + ".txt"
    with open(txtfile, "w+") as file:
        file.write("\t\t Library of Kathmandu\n")
        file.write("\t\tReturned by: " + name + "\n")
        file.write("    \t Date: " + returneddate +"  \t   Time:" + returnedtime )
        file.write("\nS.N.\t\tBook\t\t\t\t\tTotal Price")

    notereturn = name
    updatelist = []
    returned = False
    correct = False
    updatedbook = ""

    for i in range(len(borrowerlist)):
        #Checking if returner has borrowed the book or not
        if name.lower() == borrowerlist[i].replace("\n", "").lower():
            correct = True
            break
        else:
            correct = False

    if correct == True:
        while extrareturn.lower() == "yes":
            print("\nWhich book would you like to return?")
            print("Enter 1 to return Days Without End\nEnter 2 to return Fugitive Pieces\nEnter 3 to return The Hobbit")
            bret = int(input("Enter the number of the book you want to return: "))
            if bret == 1:
                for i in range(len(updatelist)):
                    if (len(updatelist) > 0 and updatelist[i] == 1):
                        returned = True
                        break
                    else:
                        returned = False

                if returned == True:
                    print("The book has already been returned.")

                else:
                    #Updating the quantity of books.
                    updatelist.append(bret)
                    returnlist[0][2] = str(int(returnlist[0][2]) + 1)
                    returnfee = returnfee + float(returnlist[0][3].replace("$",""))
                    booksreturn = booksreturn + "Days Without End"

            elif bret == 2:
                for i in range(len(updatelist)):
                    if (len(updatelist) > 1 and updatelist[i] == 2):
                        returned = True
                        break
                    else:
                        returned = False

                if returned == True:
                    print("The book has already been returned.")

                else:
                    updatelist.append(bret)
                    returnlist[1][2] = str(int(returnlist[1][2])+ 1)
                    returnfee = returnfee + float(returnlist[1][3].replace("$",""))
                    booksreturn = booksreturn + "Fugitive Pieces"

            elif bret ==3:
                for i in range(len(updatelist)):
                    if (len(updatelist) > 2 and updatelist[i] == 3):
                        returned = True
                        break
                    else:
                        returned = False

                if returned == True:
                    print("The book has already been returned.")

                else:
                    updatelist.append(bret)
                    returnlist[2][2] = str(int(returnlist[2][2]) + 1)
                    returnfee = returnfee + float(returnlist[2][3].replace("$",""))
                    booksreturn = booksreturn + "The Hobbit"

            extrareturn = input("Do you want to return more books ? \nInput yes or no    ")

        if  extrareturn == "no":
            #Creating bill for the text file
            notereturn = "1" + "\t\t" + booksreturn + "\t\t\t\t\t" + "$" + str(returnfee)
            returnfile = "1" + "\t" + booksreturn + "\t\t\t" + "$" + str(returnfee)
            for i in range(len(returnlist)):
                qty = ""
                for j in range(len(returnlist[i])):
                    if j == len(returnlist[i]) + 1:
                        qty = qty + returnlist[i][j] + "\n"
                    else:
                        qty = qty + returnlist[i][j] + ","
                updatedbook = updatedbook + qty
            print("\n\t\tUpdated List of Books\n*************************************")
            print(updatedbook)
            print("\t\t \t\t\tLibrary of Kathmandu\n")
            print("\t\t\t\t\tReturned by: ", name)
            print("    \t\tDate: " + returneddate + "   \t\t Time:" + returnedtime + "\n\n")
            print("S.N.\t\t\tBook\t\t\t\t\t\t\tTotal Price")


            print(notereturn)

            print("\n[Note: The borrowed book must be returned within 10 days.]\n")

            inforet = open("stock.txt", "w")
            inforet.write(updatedbook)
            inforet.close()

            with open(txtfile, "a") as file:
                file.write("\n" + returnfile)

            print("\nIs the return date of the book expired?")
            expiry = input("Enter y for yes and n for no:  ")
            if  expiry == "y":
                print("By how many days late have you returned the book? \n")
                late = int(input("Your answer:  "))
                fine = 2 * late
                returnfee = float(returnfee) + fine
                print("Total Fine: $", fine)

                with open(txtfile, "a") as file:

                    file.write("\n\t\t\t\t\tTotal cost with fine: $" + str(returnfee))
            elif expiry == "n":
                print("\t\t\t\t\t\t\t\tTotal cost: $", str(returnfee))

            else:
                print("Input as suggested.")

        else:
            print("Enter suggested value only.")

    else:
        print("The name is incorrect.")












