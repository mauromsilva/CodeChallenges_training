import random

random.seed(1)
print(random.random())

# with seed get the same number
random.seed(1)
print(random.random())

# without seed get another random number
print(random.randint(300, 1000))


numbers = {1,2,3}
number  = random.choice(tuple(numbers))
print(number)
# 3

# list - random.choices for multiple elements
cities = ['Munich','Rome','Madrid','Barcelona','Paris']
city2 = random.choices(cities, k=2)
print(city2)
# ['Paris', 'Madrid']

# tuple
letters = ('a','b','c')
letter = random.choice(letters)
print(letter)