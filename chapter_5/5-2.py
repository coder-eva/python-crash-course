# ignoring case when checking for equality
city = 'Montreal'
print(city == 'montreal')

city = 'Paris'
print(city.lower() == 'paris')

# checking for inequality
dog = 'Theo'
if dog != 'Foxy':
    print("Ok mama hush!")

# numerical comparison
Theo = 1.5

if Theo < 2:
    print("He's still a puppy")
else:
    print("He's a big boy now")

# checking multiple conditions with AND
Theo = 1.5
Finnley = 1
Foxy = 12

print("\nAre all these dogs puppies?")
print(Theo < 2 and Finnley < 2 and Foxy < 2)

print("\nAre all these dogs less than 15?")
print(Theo < 15 and Finnley < 15 and Foxy < 15)

print("\nAre all these dogs 1 or older?")
print(Theo >= 1 and Finnley >= 1 and Foxy >= 1)

# checking multiple conditions with OR
Theo = 1.5
Finnley = 1
Foxy = 12

print("\nAre any of these dogs puppies?")
print(Theo < 2 or Finnley < 2 or Foxy < 2)

print("\nAre any of these dogs more than 12")
print(Theo > 15 or Finnley > 15 or Foxy > 15)

print("\nAre any of these dogs 1 or older?")
print(Theo >= 1 or Finnley >= 1 or Foxy >= 1)


"""
# checking if value is in a list

print("\nWhat toy are you looking for?")
wanted_toy = input()

if wanted_toy.lower() in toys:
    print("\nYes, we have it in stock")
else:
    print("\nSorry out of luck")

print("\nHow old is your dog?")
"""
toys = ['sir bob-a-lot', 'snoop', 'snuffle mat', 'kong', 'ball']

# checking if value not in list
object = 'soccer ball'

if object not in toys:
    print(f"\n{object.title()} is not a toy")
