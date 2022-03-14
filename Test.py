
usernames = ["Josh", "Bob", "Admin", "Sal", "Sally", "Syed", "Ali", "MJ"]

new_usernames = ["Michael", "Bob", "Karl", "Admin", "Shazaib"]
for n_users in new_usernames:
    if n_users in usernames:
        print("This username is already taken, please enter a different one")
    else:
        print("Username is available")
