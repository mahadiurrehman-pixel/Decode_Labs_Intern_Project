# Expense Tracker (Python)

A simple command-line Expense Tracker built in Python. This application allows users to record expenses, assign categories, and view a summary of all expenses along with the total amount spent.

## Features

- Add multiple expenses
- Assign a category to each expense
- Prevents negative expense values
- Handles invalid input gracefully
- Displays a detailed expense summary
- Calculates the total amount spent

## Technologies Used

- Python 3
- Basic Python Concepts
  - Variables
  - Loops
  - Conditional Statements
  - Lists
  - Tuples
  - Exception Handling (`try-except`)
  - User Input

## How It Works

1. Run the program.
2. Enter an expense amount.
3. Enter a category for the expense.
4. Repeat until all expenses are entered.
5. Type `quit` to finish.
6. View the final expense summary and total spending.

## Example

```text
--- Expense Tracker ---

Enter Your Expense Or Enter "quit" to Exit: 25
What was this expense for? (e.g., Food, Travel): Food
Added $25.00 for 'Food' | Current Total: $25.00

Enter Your Expense Or Enter "quit" to Exit: 40
What was this expense for? (e.g., Food, Travel): Transport
Added $40.00 for 'Transport' | Current Total: $65.00

Enter Your Expense Or Enter "quit" to Exit: quit

===================================
          SUMMARY RECEIPT
===================================
• Food                : $25.00
• Transport           : $40.00
-----------------------------------
FINAL TOTAL SPENT: $65.00
===================================
```

## Error Handling

- Rejects negative expense values.
- Detects invalid (non-numeric) input.
- Continues running until the user enters `quit`.

## Learning Objectives

This project demonstrates:

- Working with user input
- Data validation
- Exception handling
- Managing collections using lists and tuples
- Loop control
- Building a simple CLI (Command Line Interface) application

## Future Improvements

- Save expenses to a file (CSV/JSON)
- Monthly expense reports
- Category-wise spending analysis
- Budget limit notifications
- Expense editing and deletion
- Graphical User Interface (GUI)

## Author

**Mahadi Ur Rehman**

BS Business & Information Technology (BBIT)
