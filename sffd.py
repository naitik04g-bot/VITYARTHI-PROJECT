budget_limit = 2000

amounts = [ 250, 120, 450 ]
category_log = [ "Food", "Transport", "Food" ]

unique_categories = { "Food", "Transport" }

print("Personal Expense & Budget Tracker")
print("Monthly Budget Limit :", budget_limit)

while True:
    print("\n MENU ")
    print("1. Add New Expense")
    print("2. View All Transactions & Budget Status")
    print("3. View Spending Breakdown by Category")
    print("4. Undo Last Expense")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == "1":
        cost = int(input("Enter expense amount: "))
        category = input("Enter category (e.g., Food, Rent, Travel): ")

        if cost > 0:
            amounts.append(cost)
            category_log.append(category)
            
            if category not in unique_categories:
                unique_categories.add(category)
                
            print("Added :", cost, "under", category)
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == "2":
        if len(amounts) == 0:
            print("No expenses recorded yet.")
        else:
            print("--- Transaction History ---")
            total_spent = 0

            for i in range (0, len(amounts)):
                print(i + 1, category_log[i], ":", amounts[i])
                total_spent += amounts[i]

            usage_percent = (total_spent / budget_limit) * 100
            print("Total Spent :", total_spent, "/", budget_limit, "Percent :", usage_percent)

            if total_spent > budget_limit:
                over_by = total_spent - budget_limit
                print("ALERT Over budget by :", over_by)
            elif usage_percent >= 80:
                print("WARNING : You have used 80% or more of your budget.")
            else:
                remaining = budget_limit - total_spent
                print("SAFE Remaining balance :", remaining)

    elif choice == "3":
        if len(unique_categories) == 0:
            print("No categories to display.")
        else:
            print("--- Spending by Category ---")
            for x in unique_categories:
                cat_total = 0
                
                for i in range (0, len(category_log)):
                    if category_log[i] == x:
                        cat_total += amounts[i]
                
                print(x, ":", cat_total)

    elif choice == "4":
        if len(amounts) > 0:
            removed_cost = amounts.pop()
            removed_cat = category_log.pop()
            print("Removed last entry :", removed_cost, removed_cat)

            count = 0
            for x in category_log:
                if x == removed_cat:
                    count += 1

            if count == 0:
                unique_categories.remove(removed_cat)
        else:
            print("Nothing to undo.")

    elif choice == "5":
        print("Closing tracker. Goodbye!")
        break

    else:
        print("Invalid option. Please enter a number from 1 to 5.")