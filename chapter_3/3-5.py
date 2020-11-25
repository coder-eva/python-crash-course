"""
import 3-4.py
import sys
sys.path.insert(0, '/Users/EvaLu/Documents/2020/automate/chapter_3')
"""

# 3.4
guest_list = ['barack obama', 'taika waititi', 'terry fox']
for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")

# changing guest list

"""
# pop() to remove just one person

declined_invite = guest_list.pop(2)
print(f"{declined_invite.title()} can't make it to dinner.")

print("We're going to invite Socrates instead. New invites!")
guest_list.append('socrates')

for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")
"""

print(f"Unfortunately {guest_list[2].title()} can't make it to dinner")
print("Let's invite Socrates instead, and make some new invites")

guest_list[2] = 'socrates'
for i in guest_list:
    print("Hi " + i.title() + ", would you like to join us for dinner?")
