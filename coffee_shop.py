customer_name = "Customer Name"
coffee_count = 3
price_per_coffee = 4.25
is_paid = True
total = coffee_count * price_per_coffee
if is_paid:
    total = total * 0.9  # to calculate 10% discount
print("Receipt for", customer_name, "Total: $", total)
