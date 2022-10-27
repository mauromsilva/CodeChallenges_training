n = 35
def solution(n):
    prime_nums = []
    for num in range(n):
        if num > 1: # all prime numbers are greater than 1
            vprime = True
            for i in range(2, num):
                if (num % i) == 0: # if the modulus == 0 is means that the number can be divided by a number preceding it
                    vprime = False
                    break
            if vprime:
               prime_nums.append(num)
    return (prime_nums)

print(solution(n))