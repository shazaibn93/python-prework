name = "shazaib nasrullah"
quote = '"A person who never made a mistake never tried anything new."'
print(name.title() + " once said " + quote)

my_list = []
print(type(my_list))
my_list = list()
print(type(my_list))

# index    0, 1, 2,  3,   4
numbers = [2, 6, 10, 12.5, 0]
print(numbers)
print(type(numbers))

print(numbers[1])
print(type(numbers[1]))
print(numbers[1]*2.5)

print(numbers[3])
print(type(numbers[3]))

foods = ["pizza", "tacos", "dim sum", "sushi"]

print(foods[1])
print(type(foods[1]))



x = 12
y = 15.5
z = "z"

random_list = [x, y, z]
print(random_list[0])
print(type(random_list[0]))

print(random_list[1])
print(type(random_list[1]))

print(random_list[2])
print(type(random_list[2]))

foods = ["pizza", "tacos", "dim sum", "sushi"]

foods.append("cheeseburger")
print(foods)

foods.insert(0, "pho")
print(foods)

foods.remove("pho")
print(foods)

foods.remove("pizza")
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
del foods[1]
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.pop())
print(foods)

foods = ["pizza", "tacos", "dim sum", "sushi"]
print(foods.sort())
print(foods)
foods.sort(reverse=True)
print(foods)

print(sorted(foods))
print(foods)
 
