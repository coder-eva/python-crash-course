usernames = ['admin', 'lue', 'getzs', 'eval', 'samg']

for username in usernames:
    if username == 'admin':
        print(
            f"Hello {username.upper()}, would you like to see a report?")
    else:
        print(f"Hello {username.upper()}, thank you for logging in again")
