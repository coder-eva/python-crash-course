# convert items in list to title case first
dogs = ['theo', 'finnley', 'icy', 'lana']
dogs = [dog.title() for dog in dogs]
print(dogs)

for dog in dogs:
    print(f"{dog} is a good dog.")
    print(f"{dog}, would you like a treat?.\n")
print("Okay pups, go play!")


for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

# cap stores, and print first 3
stores = ['lululemon', 'gap', 'uniqlo', 'simons', 'pharmaprix']
stores = [store.title()for store in stores]
print(stores[:3])

# first 3 stores in the mall
for store in stores[1:3]:
    print(store.title())

print("\n")

# tuples, which are immutable
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# tuples for loop
for dimension in dimensions:
    print(dimension)

# reassigning values in tuple
pets = ('cat', 'dog')
print("\nOriginal pets")
for pet in pets:
    print(pet)

pets = ('parrot', 'hamster')
print("\nModified pets")
for pet in pets:
    print(pet)
