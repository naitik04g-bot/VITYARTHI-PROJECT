# VITYARTHI-PROJECT
# Personal Expense & Budget Tracker

A small command-line Python program for tracking spending against a monthly budget. It keeps a list of expenses, shows how much of the budget has been used, breaks spending down by category, and can undo the last entry.

## Features

- Monthly budget limit (default: 2000)
- Starts with three sample expenses: Food 250, Transport 120, Food 450
- Add a new expense with an amount and a category
- View every transaction with the total spent, the percentage of the budget used, and a status message:
  - **ALERT** when spending is over the budget (shows how much over)
  - **WARNING** when 80% or more of the budget has been used
  - **SAFE** otherwise (shows the remaining balance)
- View total spending for each category
- Undo the last expense (a category is removed once its last expense is undone)
- Rejects zero and negative amounts

## Requirements

- Python 3 (no external libraries, no imports)

## How to run

Save the code as `main.py` and run it from its folder:

```
python main.py
```

On Windows you can also use `py main.py`.

## Menu

| Option | Action |
|--------|--------|
| 1 | Add New Expense |
| 2 | View All Transactions & Budget Status |
| 3 | View Spending Breakdown by Category |
| 4 | Undo Last Expense |
| 5 | Exit |

Any other input prints `Invalid option. Please enter a number from 1 to 5.`

## Example session

```
Select an option (1-5): 1
Enter expense amount: 900
Enter category (e.g., Food, Rent, Travel): Rent
Added : 900 under Rent

Select an option (1-5): 2
--- Transaction History ---
1 Food : 250
2 Transport : 120
3 Food : 450
4 Rent : 900
Total Spent : 1720 / 2000 Percent : 86.0
WARNING : You have used 80% or more of your budget.

Select an option (1-5): 3
--- Spending by Category ---
Food : 700
Rent : 900
Transport : 120

Select an option (1-5): 4
Removed last entry : 900 Rent
```

## How it works

| Name | Type | Purpose |
|------|------|---------|
| `budget_limit` | int | Monthly budget |
| `amounts` | list of int | Expense amounts |
| `category_log` | list of str | Category of each expense, at the same index as `amounts` |
| `unique_categories` | set of str | Distinct categories currently in use |

1. A `while True` loop prints the menu and reads the choice; an `if / elif` chain runs the matching block.
2. **Add:** a positive amount is appended to `amounts` and its category to `category_log`. The category is added to the set if it is new.
3. **View:** loops through both lists together, adds up the total, computes `(total_spent / budget_limit) * 100`, and prints the ALERT, WARNING or SAFE message.
4. **Breakdown:** for each category in the set, loops through `category_log` and adds up the matching amounts.
5. **Undo:** `pop()` removes the last amount and category. If no remaining expense uses that category, it is removed from the set.
6. **Exit:** prints a goodbye message and breaks out of the loop.

## Known limitations

- Entering a non-integer amount (for example `abc` or `12.5`) stops the program with a `ValueError`; only whole numbers are supported.
- Data is kept in memory only and is lost when the program exits (except the three built-in sample expenses, which load each time).
- Categories are case-sensitive, so `Food` and `food` are counted separately, and an empty category is accepted.
- The category breakdown prints in no fixed order, because it loops over a set.
- The budget limit is fixed in the code and cannot be changed from the menu.
- The percentage is printed unrounded.

## Possible improvements

- Wrap the amount input in `try / except` and accept decimal amounts
- Normalise categories with `strip()` and `title()` and reject empty ones
- Save expenses to a file so they persist
- Let the user set the budget at start-up
- Round the percentage with `round(usage_percent, 1)`
- Sort the category breakdown
