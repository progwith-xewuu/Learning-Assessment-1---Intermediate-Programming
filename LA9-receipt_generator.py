item_name = input("Item name: ").strip()
item_quantity = int(input("Quantity: "))
unit_price = float(input("Price: "))

total = item_quantity * unit_price

print("\nRECEIPT")
print("-" * 35)

print(f"{item_name:<15}{item_quantity:>5}  {unit_price:>10,.2f}")

print("-" * 35)

print(f"{'TOTAL':<20} ₱{total:>12,.2f}\n")