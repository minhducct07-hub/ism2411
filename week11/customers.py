# Reflection 1:
# I would use .get() for optional fields, such as a customer's phone number,
# because I can provide a default when the field is missing. I would use bracket
# notation for required fields, such as a product price, so missing data raises
# an error that I can investigate. My rule is .get() for optional data and
# brackets for data the program requires.
#
# Reflection 2:
# Building a summary dictionary reminds me of an Excel PivotTable or SUMIF,
# because both group records and add values for each group. Python can be more
# useful for large datasets because the same script can process new files
# automatically without manually copying formulas or refreshing ranges.

# Exercise 1: Create one customer and access each field.
print("\nEXERCISE 1: One customer")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2: Print the dictionary after each change.
print("\nEXERCISE 2: Update and add")
customer["phone"] = "555-0101"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# Exercise 3: Compare safe lookup with bracket notation.
print("\nEXERCISE 3: Safe lookup")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as error:
    print(f"Caught KeyError: {error}")

# Exercise 4: Iterate over pairs, then over keys alone.
print("\nEXERCISE 4: Iterate")
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), iteration returns only keys, not key-value tuples.
print("Keys only:")
for key in customer:
    print(key)

# Exercise 5: Use a lookup table to calculate the final purchase price.
print("\nEXERCISE 5: Lookup table")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
final_price = 200 * (1 - discount_rate)
print(f"Tier: {tier}")
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")

# Exercise 6: Calculate the dollar discount for three customers.
print("\nEXERCISE 6: List of dicts")
dict1 = {"name": "Alice", "tier": "platinum"}
dict2 = {"name": "Bob", "tier": "silver"}
dict3 = {"name": "Calvin", "tier": "bronze"}
customers = [dict1, dict2, dict3]
for current_customer in customers:
    discount_rate = tier_discounts.get(current_customer["tier"], 0)
    discount_amount = 300 * discount_rate
    print(f"{current_customer['name']} | {current_customer['tier']} | "
          f"Discount on $300: ${discount_amount:.2f}")

# Exercise 7: Display an alert only for products below the stock threshold.
print("\nEXERCISE 7: Nested catalog")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - {details['stock']} remaining")

# Exercise 8: Accumulate sales totals, then print in alphabetical region order.
print("\nEXERCISE 8: Sales by region")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for transaction in transactions:
    region = transaction["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + transaction["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
