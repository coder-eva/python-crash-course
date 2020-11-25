my_pizzas = ['hawaiian', 'margherita', 'capricciosa', 'diavola']
friend_pizzas = my_pizzas[:]

my_pizzas.append('supreme')
friend_pizzas.append('bbq chicken')

print("My favourite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())

print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
