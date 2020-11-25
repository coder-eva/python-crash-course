import random

lemmings = ['align leggings', 'air pods', 'raspberry pi 400']
today_lemmings = random.choice(lemmings)

stores = ['lululemon', 'uniqlo', 'apple', 'simons']
today_store = random.choice(stores)
message = f"I want to go to {today_store.title()} to buy {today_lemmings.title()} today."
print(message)
