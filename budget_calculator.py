# Each element is the product code, the individual price, and the quantity.
order_list = [("tom", 0.87, 4),
              ("sug", 1.09, 3),
              ("ws", 0.29, 4),
              ("juc", 1.89, 1),
              ("fo", 1.29, 2)]

# This dictionary gives the full name of each product code.
names = {"tom": "Tomatoes",
         "sug": "Sugar",
         "ws": "Washing Sponges",
         "juc": "Juice",
         "fo": "Foil"}

budget = 10.00
running_total = 0
receipt = []

for entry in order_list:
    (code, price, quantity) = entry
    receipt.append(names[code])
    total_cost = price * quantity
    running_total += total_cost
    budget -= total_cost
    print(f"Current total: {running_total}. Remaining budget: {round(budget, 2)}")
    if budget < 0:
        print(f"You have exceeded your budget by {budget}")
        break

print(f"Receipt: {receipt}")