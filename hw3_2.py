def gcd(x, y):
    return x if not y else gcd(y, x % y)
 
def lcm(x, y):
    return x * y / gcd(x, y)
 
print(lcm(5, 2)) 
print(lcm(7, 1)) 
