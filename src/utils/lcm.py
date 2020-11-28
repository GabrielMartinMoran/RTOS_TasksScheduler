from math import gcd

def lcm(numbers):
    lcm_temp = numbers[0]
    for i in numbers[1:]:
        lcm_temp = lcm_temp * i // gcd(lcm_temp, i)
    return lcm_temp