import csv
with open ("book22.csv", newline="") as csvfile:
    rows = csv.reader(csvfile, delimiter=",")
    data = []

def searchByNumber():
    number = input("Enter pokedex number\n")
    csv_file = csv.reader(open("book22.csv", "r"))

    for row in csv_file:
        if number == row[0]:
            if row[3]=="None":
                print("--------------------------------------------------------------")
                print("Name:", row[1])
                print("Type:", row[2])
                print("Base Stat Total:",row[4])
                print("--------------------------------------------------------------")
                askAgain()
            else:
                print("--------------------------------------------------------------")
                print("Name:", row[1])
                print("Type:",row[2],row[3])
                print("Base Stat Total:", row[4])
                print("--------------------------------------------------------------")
                askAgain()
    else:
        print("Re-enter an existing pokedex number")
        askAgain()
        
def searchByName():
    name = input("Enter pokemon's name\n")
    name=str.title(name)
    csv_file = csv.reader(open("book22.csv", "r"))
    for row in csv_file:
        if name == row[1]:
            if row[3]=="None":
                print("--------------------------------------------------------------")
                print("Name:", row[1])
                print("Type:", row[2])
                print("Base Stat Total:",row[4])
                print("--------------------------------------------------------------")
                askAgain()
            else:
                print("--------------------------------------------------------------")
                print("Name:", row[1])
                print("Type:",row[2],row[3])
                print("Base Stat Total:", row[4])
                print("--------------------------------------------------------------")
                askAgain()
    else:
        print("Re-enter existing pokemon name")
        askAgain()
    
         
        

def askAgain():          
    print("Enter 1 to search by pokemon number")
    print("Enter 2 to search by pokemon name")
    print("Enter 3 to stop")

    src = input("Enter here: ")

    if src == "1":
        searchByNumber()
    elif src == "2":
        searchByName()
    elif src == "3":
        print("Thank you, Have a great day!")
    else:
        print("Invalid")
        askAgain()
askAgain()
