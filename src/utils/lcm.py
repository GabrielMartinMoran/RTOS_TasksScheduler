from math import gcd

def lcm(numbers):
    if len(numbers) < 1:
        return 0

    lcm_temp = numbers[0]
    for i in numbers[1:]:
        lcm_temp = lcm_temp * i // gcd(lcm_temp, i)
    return lcm_temp