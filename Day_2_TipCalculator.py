print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


total=round(bill*(tip/100)+bill,2)
bill_after_split=round(total/people,2)
print(f"Your total bill is ${total}.After split between {people} it is${bill_after_split}")