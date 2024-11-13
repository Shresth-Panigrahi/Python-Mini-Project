from Expense import Expense

def main():
    print("Running the Expense Tracker")
    expense = get_user_expense()

    save_expense_to_a_file()
    
    summarize_expense()

def get_user_expense():
    print("Getting the USer Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))

    expense_categories = ["Food", "Home", "Work", "Fun", "Misc"]

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
        

def save_expense_to_a_file():
    print("Saving the User Expense")

def summarize_expense():
    print("Summarizing User Expense")

if __name__ == "__main__":
    main()

