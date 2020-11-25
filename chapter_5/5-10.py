current_users = ['theo', 'lue', 'getzs', 'eval', 'samg']
new_users = ['getzs', 'lue', 'bellca', 'charltok', 'doodle']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is not availaible")
    else:
        print("This username is available")
