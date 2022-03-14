persons_age = 65

if persons_age < 2:
    print("You are a baby")
elif persons_age >= 2 and persons_age < 4:
    print("You are a toddler")
elif persons_age>= 4 and persons_age < 13:
    print("You are a kid")
elif persons_age >= 13 and persons_age < 20:
    print("You are a teenager")
elif persons_age >= 20 and persons_age < 65:
    print("You are an adult")
else:
    print("You are an elder")

usernames = ["Josh", "Bob", "Admin", "Sal", "Sally", "Syed", "Ali", "MJ"]

for uname in usernames:
    if uname == "Admin":
        print("Hello " + uname + ", would you like a status report?")
    print("Hello " + uname + ", thank you for logging in again.")
