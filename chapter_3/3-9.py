guest_list = ['barack obama', 'taika waititi', 'terry fox']
for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")

print("\n" + f"Unfortunately {guest_list[2].title()} can't make it to dinner")
print("Let's invite Socrates instead, and make some new invites")

guest_list[2] = 'socrates'
for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")

print("\n" + "We have a bigger table so now we can invite 3 more people")

guest_list.insert(0, "michelle obama")
guest_list.insert(2, "alexandria ocasio-cortez")
guest_list.append("arnold schwarzenegger")

for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")

# dinner guests

print("\nI'm getting confused, how many people are we inviting now?")

print(f"We are inviting {len(guest_list)} people")
