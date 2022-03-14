user_names = ["Josh", "Bob", "Admin", "Sal", "Sally", "Syed", "Ali", "MJ"]

if user_names:
    for uname in user_names:
        if uname == "Admin":
            print("Hello " + uname + ", would you like a status report?")
        print("Hello " + uname + ", thank you for logging in again.")
else:
    print("We need usernames")
