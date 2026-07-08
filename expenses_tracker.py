import json 
import os

expenses=[]

### ADDING EXPENSES 
def add_expense():
    ### READING DETAILS
    while True:
        try:
            amount=float(input("Enter expense amount:"))
            if amount<=0:
                print("Amount must be greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid amount")
    while True:
        category=input("Enter category: ").strip()
        if category=="":
            print("Category cannot be empty.")
        else:
            break
    while True:
        description=input("Enter description: ").strip()
        if description=="":
            print("Description cannot be empty.")
        else:
            break
    while True:
        date=input("Enter Date (DD-MM-YYYY): ").strip()
        if date=="":
            print("Date cannot be empty.")
        else:
            break

    ### STORING THE EXPENSE
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    expenses.append(expense)
    print("Expenses Added Successfully")

### VIEW EXPENSES
def view_expense():
    ### CHECKS IF EXPENSES LIST IS EMPTY
    if not expenses:
        print("No expenses found.")
    else:
        for expense in expenses:
            print(f"Amount: {expense["amount"]}")
            print(f"Category: {expense["category"]}")
            print(f"Description: {expense["description"]}")
            print(f"Date: {expense["date"]}")
    print("Expenses viewed successfully.")

### PRINTING TOTAL EXPENSES
def total_expenses():
    total_amount=0
    for expense in expenses:
        total_amount += expense["amount"]
    print(f"Total Expenses: {total_amount}")

### DELETING EXPENSE

def delete_expense():
    ### CHECKING IF EXPENSES LIST IS EMPTY
    if not expenses:
        print("No expenses to delete.")
    else:
        expense_index=int(input("Enter expense number to delete: "))
        if expense_index<0 or expense_index>=len(expenses):
            print("Invalid expense number.")
        expenses.pop(expense-1)
        print(f"Expense number {expense} deleted successfully.")

### UPDATING OR EDITING AN EXPENSE
def update_expense():
    ### CHECKING IF EXPENSES LIST IS EMPTY
    if not expenses:
        print("No expenses found.")
    else:
        num=1
        for expense in expenses:
            ### PRINTING ALL THE EXPENSES PRESENT IN THE DICTIONARY
            print(f"{num} {expense["category"]} - {expense["amount"]}")
            num=num+1     
        ### TAKING EXPENSE NUMBER
        expense_index=int(input("Which expense number you want to edit: "))
        if expense_index<0 or expense_index>=len(expenses):
            print("Invalid expense number.")
        
        expense=expenses[expense_index-1]
        ### TAKING NEW DETAILS
        amount=float(input("Enter new expenses amount:"))
        category=input("Enter new category: ")
        description=input("Enter new description: ")
        date=input("Enter new date: ")
        ### UPDATING DICTIONARY VALUES
        expense["amount"]=amount
        expense["category"]=category
        expense["description"]=description
        expense["date"]=date
        print("Expense updated successfully.")

### SEARCHING FOR AN EXPENSE
def search_expenses():
    ### CHECKING IF EXPENSES LIST IS EMPTY
    if not expenses:
        print("No expenses found.")
    else:
        ### ASKING USER FOR THE CATEGORY TO SEARCH
        search_expense=input("Enter category to search: ") 
        if search_expense<0 or search_expense>=len(expenses):
            print("Invalid expense number.")
             
        ### SEARCHING IN THE DICTIONARY
        found=False
        for expense in expenses:
            ### CHECKING IF IT MATCHES OR NOT
            if expense["category"]==search_expense:
                found=True
                print(f"Amount: {expense["amount"]}")
                print(f"Category: {expense["category"]}")
                print(f"Description: {expense["description"]}")
                print(f"Date: {expense["date"]}")             
        if not found:
            print("No matching expenses found")

### FILTERING
def save_expenses():
    ### OPENING A JSON FILE
    save_expense=open("expenses.json","w")  
    ### WRITES TO JSON FILE
    json.dump(expenses,save_expense)
    save_expense.close()
    print("Expenses saved successfully")

### LOADING EXPENSES
def load_expenses():
    global expenses
    ### CHECKING IF EXPENSES LIST IS EMPTY
    if os.path.exists("expenses.json"):
        ### OPENING JSON FILE IN READ MODE
        load_expense=open("expenses.json","r")
        ### READS DATA FROM JSON FILE 
        expenses=json.load(load_expense)
        load_expense.close()   
    print("Expenses loaded successfully.")
      
while True:
    try:
        choice=int(input("Enter Your Choice: \n 1. Add Expenses\n 2. View Expenses \n 3. Total Expenses \n 4. Delete Expense \n 5. Update or Edit Expense \n 6. Search Expenses \n 7. Save Expenses to a File \n 8. Load Expenses from a file\n 9. Exit \n"))
    except ValueError:
        print("Please enter a valid choice.")
        continue
    if choice==1:
        add_expense()
    elif choice==2:
        view_expense()
    elif choice==3:
        total_expenses()
    elif choice==4:
        delete_expense()
    elif choice==5:
        update_expense()
    elif choice==6:
        search_expenses()
    elif choice==7:
        save_expenses()
    elif choice==8:
        load_expenses()
        print(expenses)
    elif choice==9:
        print("Thank you")
        break
    else:
        print("Invalid Choice")