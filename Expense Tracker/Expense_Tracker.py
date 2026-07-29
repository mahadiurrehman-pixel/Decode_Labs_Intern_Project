total_spend = 0.0
expenses_list = [] 
print('\n--- Expense Tracker ---\n')
while True:
    user_input = input('Enter Your Expense Or Enter "quit" to Exit: ').strip()
    if user_input.lower() == 'quit':
        print('Bye! Take Care.\n')
        break
    try:
        expense = float(user_input)
        if expense < 0:
            print('Expense Cannot Be Negative.\n')
            continue
            
        category = input('What was this expense for? (e.g., Food, Travel): ').strip()
        
        total_spend += expense
        expenses_list.append((category if category else "Uncategorized", expense))
        
        print(f"Added ${expense:.2f} for '{category}' | Current Total: ${total_spend:.2f}\n")
    except ValueError:
        print("Invalid Data! Please enter a valid number or 'quit'.\n")
print("=" * 35)
print("          SUMMARY RECEIPT          ")
print("=" * 35)
if expenses_list:
    for item, amount in expenses_list:
        print(f"• {item:<20}: ${amount:.2f}")
    print("-" * 35)
print(f"FINAL TOTAL SPENT: ${total_spend:.2f}")
print("=" * 35)
