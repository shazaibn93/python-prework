numbers = range(1, 11)
sums = 0

for number in numbers:
    sums += number

print(sums)

odd_numbers = range(1, 20, 2)

for odd in odd_numbers:
    print(odd)

print(max(numbers))
print(min(numbers))
print(sum(numbers))

thirds = range(3, 31, 3)

for third in thirds:
    print(third)

foods = ["pizza", "tacos", "dim sum", "sushi", "fries", "gyro"]

print("The first three items in my list are", end=" ")
for food in foods[:3]:
    print(food, end = ", ")

print("\nThe last three items in my list are", end=" ")
for food in foods[3:]:
    print(food, end = ", ")

print("\nThe last three items in my list are", foods[3:])

my_pizzas = ["cheese", "veggie", "pepporoni", "deep dish"]

friends_pizza = my_pizzas[:]

my_pizzas.append("mushroom")
friends_pizza.append("meat")

print("\nMy favorite pizzas are", end = " ")
print(my_pizzas)

print("\nMy friends favorite pizzas are", end = " ")
print(friends_pizza)

print("\nMy favorite pizzas are", end = " ")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are", end = " ")
for fpizza in friends_pizza:
    print(fpizza)

