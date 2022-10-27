from collections import Counter
cities = ['Madrid','Rome','Rome','Munich','Madrid','Madrid','Madrid','Madrid','Rome']

counter_cities = dict(Counter(cities))
print(counter_cities)

print(sorted(counter_cities, key=counter_cities.get, reverse=False))
