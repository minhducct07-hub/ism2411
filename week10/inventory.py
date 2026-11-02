# Reflection 1:
# The most surprising thing to me is that Python lists start counting at zero,
# while negative indices let me access items from the end. I also find it useful
# that a list can grow or shrink without needing to set its size first.
#
# Reflection 2:
# In my Business Information Systems class, a Python list could help me organize
# daily sales and calculate the total and average. It could also filter days with
# high sales automatically, saving time compared to checking Excel rows manually.


# Exercise 1: Build the list
print("Exercise 1")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# Exercise 2: Index practice
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
middle_index = len(inventory) // 2
print(inventory[middle_index])


# Exercise 3: Slicing
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4: Modify
print("\nExercise 4")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)


# Exercise 5: Tuple comparison
print("\nExercise 5")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: tuples cannot be changed after they are created.")
    print("Tuples are useful for coordinates because they prevent accidental changes.")
print(coords)


# Exercise 6: Average of a list of sales
print("\nExercise 6")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7: Accumulator pattern
print("\nExercise 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print("Original:", prices)
print("Discounted:", discounted)


# Exercise 8: Filter above threshold
print("\nExercise 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print("Count:", len(high_sales))
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")
