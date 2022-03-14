#Looping through all key-value pairs

user_0 = {
    "username" : "efermi",
    "first" : "enrico",
    "last" : "fermi"
}

for key, value in user_0.items():
    print("\nKey:" + key)
    print("Value: " + value)

rivers_0 = {
    "nile" : "Egypt",
    "black sea" : "Middle East",
    "Mississippi" : "United States of America"
}

for river, country in rivers_0.items():
    print("The " + river.title() + " runs through " + country.title())

for river in rivers_0.keys():
    print("The river is " + river.title())

for country in rivers_0.values():
    print("The country is " + country.title()) 