from datetime import datetime
#if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
discout_rate = 0.10
tax_rate = 0.06
today = datetime.now()
day_of_week = today.weekday()
subtotal = float(input("Enter the subtotal: "))
discount = 0.0
print(f"Discount: ${discount}")
if day_of_week == 2 or day_of_week == 3:
    if subtotal >= 50:
        discount = subtotal * discout_rate
subtotal -= discount
tax = subtotal * tax_rate
total = subtotal + tax
print(f"Tax: ${tax}")
print(f"Total: ${total}")
print(f"Total due: ${total}")