# index      0        1        2          3
foods = ["pizza", "tacos", "dim sum", "sushi"]

print(foods[1])

#for PLACEHOLDER in THE LIST WE WANT TO LOOK AT:
    # this is a code block
    # this code block will run for every item in the list

for food in foods:
    print(f"I like to eat {food}")

    print(type(food))
print("Loop is over")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

for food in foods:
    print(f"I like {food} because they are yummy")
    if food == "sushi":
        break 

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

#loop of the index
print(list(range(4)))
print(len(foods))

for index in range(len(foods)):
    print(index)
    print(foods[index])

print(list(enumerate(foods)))

for tup in enumerate(foods):
    print(tup)

for index, food in enumerate(foods):
    print(index, food)
    print(f"My No {index +1} food is {food.title()}")

