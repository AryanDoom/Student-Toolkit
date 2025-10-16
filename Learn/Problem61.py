c = ("Milk", "Bread", "Butter", "Cheese", "Jam", "Eggs")
i1, i2, i3, *rest = c
print("First three items:", i1, i2, i3)

remaining_items = list(rest)
print("Remaining items as list:", remaining_items)
print("Type of remaining items:", type(remaining_items))


print("All items in the cart:")
for item in c:
    print(item)

print("First 3 items:", c[:3])
print("Last 2 items:", c[-2:])


print("Is 'Butter' in cart?", "Butter" in c)
print("Is 'Honey' in cart?", "Honey" in c)


new_items = ("Juice", "Fruits")
updated_cart = c + new_items
print("\nUpdated cart:", updated_cart)


cheese_index = c.index("Cheese")
print("Index of 'Cheese':", cheese_index)


butter_count = c.count("Butter")
print("Count of 'Butter':", butter_count)

