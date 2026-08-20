import csv
from os import name
from unicodedata import category

def main():
    while(True):
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            addexpense()
        elif choice == '2':
            csvfileread()
        elif choice == '3':
            searchexpense()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def csvfileappend(exp, cat, money, time): #Add Expenses to file
    try:
        # append a row to a CSV file
        with open("Personal Expense Tracker.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([exp, cat, money, time])
    except FileNotFoundError:
        print(" Date not written in file. ")

def csvfileread(): #View Expenses
    try:
        # reading from csv
        with open("Personal Expense Tracker.csv", "r", newline='') as file:
            reader = csv.reader(file)
            for iterate, read in enumerate(reader, start = 1):
                Id, Nam, Type, mon = read
                copy_data = [
                    {
                        "ID": Id, "Name": Nam, "category": Type, "Amount": mon
                    }
                ]
                print(f"ID: {Id}, Name: {Nam}, Type: {Type}, Amount: {mon}")
    except FileNotFoundError:
        print(" Date not read from the file. ")

def searchexpense():
    while(True):
        entry = input(" In order to search expense enter category or name of it:  ")
        if not entry:
            break
        print(f"Searching for {entry} in the file...")

        try:
            with open("Personal Expense Tracker.csv", "r", newline='') as file:
                reader = csv.reader(file)
                found = False
                for row in reader:
                    if len(row) >= 2:
                        if entry.lower() in row[0].lower() or entry.lower() in row[1].lower():
                            print(f"Found {entry} in the file.")
                            found = True
                if not found:
                    print(f"{entry} not found in the file.")
        except FileNotFoundError:
            print("Date not read from the file.")


def addexpense():
    Expense = input("Expense name: ")
    Category = input("Category name: ")
    Amount = input("Amount: ")
    Date = input("Date: ")
    csvfileappend(Expense, Category, Amount, Date)
    
main()