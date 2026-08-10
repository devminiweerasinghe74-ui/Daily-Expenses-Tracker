expenses_list = []
total = 0.0

print("Welcome to the Daily Expense Tracker!")

# Display menu once
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

while True:
    choice = input("")

    if choice == '1':
        expenses_value = float(input())
        expenses_list.append(expenses_value)
        print("Expense added successfully!")
        continue

    elif choice == '2':
        if len(expenses_list) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses_list)):
                print(f"{i+1}. {expenses_list[i]}")

    elif choice == '3':
        if len(expenses_list) == 0:
            print("No expenses recorded yet.")

        else:
            for i in range(len(expenses_list)):
                total = total+expenses_list[i]
            average = total/len(expenses_list)
            print(f"Total expense: {total}")
            print(f"Average expense: {average}")

    elif choice == '4':
        expenses_list.clear()
        print("All expenses cleared.")
                    
    elif choice == '5':
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
