persons_info = {
    "first_name" : "Shazaib",
    "last_name" : "Nasrullah",
    "age" : 28,
    "city" : "New York"
    }

persons_info2 = {
    "first_name" : "Bob",
    "last_name" : "The Builder",
    "age" : 30,
    "city" : "Queens"
    }

persons_info3 = {
    "first_name" : "King",
    "last_name" : "Of Spades",
    "age" : 100,
    "city" : "The deck"
    }

people = [ persons_info, persons_info2, persons_info3 ]



print(persons_info)

print("Persons name is " + persons_info["first_name"] + " " + persons_info["last_name"])
print(persons_info["first_name"] + "'s age is " + str(persons_info["age"]))
print(persons_info["first_name"] + "'s city is " + persons_info["city"])

