# Question 1 - Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    print(f"Hello_{user_name}")

hello_name("Shazaibn93")

# Question 2 - Write a python function, 
# first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    odd_nums = range(1, 100, 2)
    for odd in odd_nums:
        print(odd)

first_odds()

# Question 3 - Please write a Python function, 
# max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    return max(a_list)

list_b = [23,41,21,67,113,4256,754257,9876,76532,2345678]
print(max_num_in_list(list_b))

# Question 4 - Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    l_year = 1993
    if (l_year % 4 == 0 ):
        if(l_year % 100 != 0):
            if(l_year % 400 == 0):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    print(str(is_leap_year(l_year)))


