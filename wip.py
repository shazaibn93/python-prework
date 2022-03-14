def say_hello(name, age):
    print(f"hello {name} you are {age} years old")

def say_goodbye():
    print("Goodbye")

def greet_back(feeling):
    if feeling == "good":
        print("Awesome, I feel good too")
    elif feeling == "bad":
        print("I'm so sorry")
    elif feeling == "stressed":
        print("Coding can be hard to learn")
    else:
        print("Well, have a good day!")


while True:
    response = input("What do you want to do? Say Hello [H] Say Goodbye [G] Talk to me [T], quit [Q]")
    if response.lower() == "q":
        break
    elif response.lower() == "h":
        n = input("What is your name?")
        a = input("What is your age?")
        say_hello(n, a)
    elif response.lower() == "g":
        say_goodbye()
    elif response.lower() == "t":
        f = input("How are you today?")
        greet_back(f)
    else:
        print("invalid input")