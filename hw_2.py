print("Вычисление площади треугольника по формуле Герона")
a=float(input("сторона a "))
b=float(input("сторона b "))
c=float(input("сторона c "))
s=float(a+b+c)/2
area=float(s*(s-a)*(s-b)*(s-c))**(1/2)
print("площад:", str(area))
