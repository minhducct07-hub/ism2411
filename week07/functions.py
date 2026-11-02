# ISM 2411 - Functions Lab
#
# Self-Assessment 1 (sample response - edit to match your experience):
# The first bug I noticed was the missing colon after the for loop.
# The traceback helped me find the line with the syntax error.
# I learned that reading error messages carefully is a good first step.
#
# Self-Assessment 2:
# apply_discount takes a price and a customer tier as inputs.
# It checks the tier and removes the right discount from the price.
# It returns the new price after the discount, before tax.
# Someone else can use it by giving a price and a tier name.
#
# Self-Assessment 3 - AI disclosure:
# I used ChatGPT to help explain the exercises, identify bugs, and
# prepare a runnable example. The explanations helped me understand
# functions, loops, errors, and scope. I will review the code myself.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0
    return price * (1 - discount)


for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier + ':':<8}${apply_discount(200, tier):.2f}")

# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
after_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---
# Fixed code from broken_sales.py.
# Bug 1: The old code replaced total instead of adding each sale.
# Fix: Use += to add each sale to the running total.
# Bug 2: The second for statement was missing a colon.
# Fix: Add a colon to complete the for-loop statement.
# Bug 3: <= allowed the index to go past the end of the list.
# Fix: Use < so the final index is len(sales) - 1.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---
# Scope means where a variable can be used.
# The x inside double_it is local, so it does not change the global x.
x = 100  # global variable


def double_it():
    x = 999  # local variable
    return x * 2


print(x)            # 100: the global x
print(double_it())  # 1998: doubles the local x of 999
print(x)            # 100: the global x is unchanged
