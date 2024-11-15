import calendar
from datetime import datetime
from Expense import Expense


def main():
    print("Running the Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 3000
    expense = get_user_expense()
    
    save_expense_to_a_file(expense,expense_file_path)
    
    summarize_expense(expense_file_path,budget)

def get_user_expense():
    print("Getting the User Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))
    expense_categories = ["🍔 Food", "🏠 Home", "💼 Work", "🎉 Fun", "🎵 Music"]

    while True:
        print("Select a Category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}.{category_name}")

        values_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter Category Number {values_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name = expense_name, amount = expense_amount, category = selected_category
                )
            return new_expense
        else:
            print("Invalid Category, Please Try Again !!!")
 
     

def save_expense_to_a_file(expense:Expense,expense_file_path):
    print(f"Saving the User Expense {expense} to {expense_file_path}")
    with open(expense_file_path,"a", encoding="utf-8") as f :
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path,budget):
    print("Summarizing User Expense") 
    expenses: list[Expense] = []
    with open(expense_file_path, "r",encoding="utf-8") as f :
        lines = f.readlines()
        for line in lines: 
            expense_name,expense_amount,expense_category = line.strip().split(",")
            line_expense = Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
            expenses.append(line_expense)
        
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key]+= expense.amount
        else:
            amount_by_category[key] = expense.amount    
    
    print("Expenses by categories..")
    for key, amount in amount_by_category.items():
        print(f"{key}: ₹{amount:.2f}")
    
    total_spent = sum([expense.amount for expense in expenses])      
    print(f"You have spent ₹{total_spent:.2f}.")
    remaning_money = budget - total_spent
    if remaning_money>0:
        print(f"The money left is ₹{remaning_money:.2f}")
    else:
        print(f"You are out of budget by ₹{abs(budget-total_spent):.2f}")
        
    # Get the current date
    today = datetime.today()
    current_day = today.day
    
    # Get the total number of days in the current month
    total_days_in_month = calendar.monthrange(today.year, today.month)[1]
    
    # Calculate remaining days
    remaining_days = total_days_in_month - current_day
    
    print(f"Remaining days in the current month: ",remaining_days)

if __name__ == "__main__":
    main()

