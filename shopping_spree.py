# Shopping spree calculator
item1_price = 7000  # Dress cost (integer)
item2_price = 2000.75  # Shoes cost (float)
budget = 10000  # Your budget
is_on_sale = False  # Sale status (boolean)
is_vip = True # VIP Status

# Calculate total with 20% discount if on sale
total = item1_price + item2_price
if is_on_sale:
    total *= 0.8  # 20% discount (same as total = total * 0.8)

if is_vip and total > 5000:
    total *=0.1 # 20% discount (same as total = total * 0.8)
    print("VIP Extra Discount Applied!")

# add a tax of 8% to total
total *=1.08

# Check if within budget and apply loyalty bonus
can_afford = total <= budget
if can_afford and is_on_sale:
    budget -= total  # Deduct total from budget
    budget += 500  # Add loyalty bonus

print(f"The total is:{total}")