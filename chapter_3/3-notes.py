# p.28 multiple assignment
x, y, z = 5, 10, 50
print(x)
print(y)
print(z)

# p.39 pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

last_owned = motorcycles.pop()
print(f"the last motaorcycle I owned was {last_owned.title()}")
print("\n")

dogs = ['theo', 'finnley', 'icy', 'lana']
for dog in dogs:
    print(f"{dog.title()} is a good dog.")
    print(f"{dog.title()}, would you like a treat?.\n")
print("Okay pups, go play!")
