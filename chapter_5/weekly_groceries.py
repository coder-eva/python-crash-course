# coping a fridge inventory
wk13_fridge = ['spinach', 'cheese', 'milk', 'dumplings', 'celery']
wk14_fridge = wk13_fridge[:]

print("In week 13, we had the following left in the fridge:")
for item in wk13_fridge:
    print(item)

# used input() to update lists

print("\nWhat can be removed from week 13?")
gone = input()
wk13_fridge.remove(gone.lower())

print("\nWhat was added in week 14?")
added = input()
wk14_fridge.append(added.lower())

print("\nIn week 14, this is what we have in the fridge:")
for item in wk14_fridge:
    print(item)
