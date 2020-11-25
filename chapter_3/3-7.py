# 3.4
guest_list = ['barack obama', 'taika waititi', 'terry fox']
for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")

# 3.5
print("\n" + f"Unfortunately {guest_list[2].title()} can't make it to dinner")
print("Let's invite Socrates instead, and make some new invites")

guest_list[2] = 'socrates'
for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")

# 3.6
print("\n" + "We have a bigger table so now we can invite 3 more people")

guest_list.insert(0, "michelle obama")
guest_list.insert(2, "alexandria ocasio-cortez")
guest_list.append("arnold schwarzenegger")

for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")

# shrinking guest list
print("\n" + "The table won't arrive in time, we only have 2 seats")

declined_invite = guest_list.pop(0)
print(f"Sorry {declined_invite.title()} the dinner is cancelled")

declined_invite = guest_list.pop(0)
print(f"Sorry {declined_invite.title()} the dinner is cancelled")

declined_invite = guest_list.pop(0)
print(f"Sorry {declined_invite.title()} the dinner is cancelled")

declined_invite = guest_list.pop(0)
print(f"Sorry {declined_invite.title()} the dinner is cancelled")


for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")

del guest_list[0]
del guest_list[0]

print(guest_list)
