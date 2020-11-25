# every function

list_functions = ['indexing', 'append', 'insert', 'pop', 'remove',
                  'sorted', 'reverse', 'index', 'len', 'sort']
print(list_functions)

# index
list_functions[0] = 'index'
print(list_functions)

# append
list_functions.append('sorted')
print(list_functions)

# pop
popped_function = list_functions.pop(0)
print(list_functions)
print(f"We've lost the {popped_function} function")

# insert
list_functions.insert(0, 'index')
print(list_functions)

# remove
removed_function = list_functions.remove("index")
print(list_functions)

list_functions.insert(0, 'index')
print(list_functions)

# sorted - temporarily
print(sorted(list_functions))
print(list_functions)

# reverse
list_functions.reverse()
print(list_functions)

# len
print(len(list_functions))

# sort reverse - permanently
list_functions.sort(reverse=True)
print(list_functions)

# sort - permanently
list_functions.sort()
print(list_functions)
