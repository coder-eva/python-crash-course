groceries = ['spinach', 'cheese', 'milk', 'dumplings', 'celery']

print(f"There are {len(groceries)} items on the list today")

# first 3 items in the grocery list

print("\nThe first three items in the list are:")

for grocery in groceries[:3]:
    print(grocery.title())

# three items from the middle

print("\nThree items from the middle of the list are:")

for grocery in groceries[1:4]:
    print(grocery.title())


# the last three items

print("\nThe last three items in the list are:")

for grocery in groceries[-3:]:
    print(grocery.title())
