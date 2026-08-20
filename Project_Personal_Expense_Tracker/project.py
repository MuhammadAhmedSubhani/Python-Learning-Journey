import csv

def main():
    while(True):
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. View Expense Statistics")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            addexpense()
        elif choice == '2':
            csvfileread()
        elif choice == '3':
            searchexpense()
        elif choice == '4':
            print(stats())
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def addexpense():
    Expense = input("Expense name: ")
    Category = input("Category name: ")
    Amount = input("Amount: ")
    Date = input("Date: ")
    ID = increment()
    csvfileappend(ID, Expense, Category, Amount, Date)


def increment():
    try:
        with open("Personal Expense Tracker.csv", "r", newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if rows:
                last_id = int(rows[-1][0])
                return last_id + 1
            else:
                return 1
    except FileNotFoundError:
        return 1
    

def csvfileappend(ID, Expense, Category, Amount, Date): #Add Expenses to file
    try:
        # append a row to a CSV file
        with open("Personal Expense Tracker.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ID, Expense, Category, Amount, Date])
    except FileNotFoundError:
        print(" Date not written in file. ")
        print(stats())

def csvfileread(): #View Expenses
    try:
        # reading from csv
        with open("Personal Expense Tracker.csv", "r", newline='') as file:
            reader = csv.reader(file)
            for iterate, read in enumerate(reader, start = 1):
                ID, Expense, Category, Amount, Date = read
                print("============= EXPENSES =============")
                print(f"ID , Name , Type , Amount , Date", sep=", ")
                print("====================================")
                print(f"{ID}  , {Expense} , {Category} , {Amount}    , {Date}", sep=", ")
                print("====================================")
                
    except FileNotFoundError:
        print(" Date not read from the file. ")

def searchexpense():
    search = input("Enter the expense name or category to search: ")
    print("Searching for expense...")
    try:
        with open("Personal Expense Tracker.csv", "r", newline='') as file:
            reader = csv.reader(file)
            found = False
            for read in reader:
                ID, Expense, Category, Amount, Date = read
                if Expense.lower() == search.lower() or Category.lower() == search.lower():
                    print("====================================")
                    print(f"ID , Name , Type , Amount , Date", sep=", ")
                    print("====================================")
                    print(f"{ID}  , {Expense} , {Category} , {Amount}    , {Date}", sep=", ")
                    print("====================================")
                    found = True
            if not found:
                print("Expense not found.")
    except FileNotFoundError:
        print(" Date not read from the file. ")    


def stats():
    try:
        with open("Personal Expense Tracker.csv", "r", newline='') as file:
            reader = csv.reader(file)
            total_expenses = 0
            category_expenses = {}
            for read in reader:
                ID, Expense, Category, Amount, Date = read
                total_expenses += float(Amount)
                if Category in category_expenses:
                    category_expenses[Category] += float(Amount)
                else:
                    category_expenses[Category] = float(Amount)
            print("============= EXPENSE STATISTICS =============")
            print(f"Total Expenses: {total_expenses}")
            print("Expenses by Category:")
            for category, amount in category_expenses.items():
                print(f"{category}: {amount}")
            print("===============================================")
    except FileNotFoundError:
        print(" Date not read from the file. ")

main()