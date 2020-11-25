# seeing the world
print("Here is the original travel list:")
destination = ['tokyo', 'amsterdam', 'paris',
               'seoul', 'new york', 'california']
print(destination)

print("\nHere is the sorted list:")
print(sorted(destination))

print("\nHere is the original list again, sorted() is temporary")
print(destination)

print("\nHere is the reverse list:")
destination.reverse()
print(destination)

print("\nHere is the reverse list back to the original order:")
destination.reverse()
print(destination)

print("\nUsing sort() to permanently store alphabetically:")
destination.sort()
print(destination)

print("\nUsing sort() to permanently store alphabetically in reverse:")
destination.sort(reverse=True)
print(destination)
