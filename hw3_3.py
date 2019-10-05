print("circle")
def areaCircle(radio):
  pi=3.1416
  area = pi * radio ** 2
  return area

radio = float(input())
if radio <= 0:
  print('El radio es incorrecto (<=0)')
else:
  print(areaCircle(radio))


print("rectangle")

def arearectangle(base, altura):
  area= altura*base
  return area
altura=float(input())
base=float(input())
if base <= 0:
    print('el radio es incorecto')
else:
  print(arearectangle(base, altura))


print("triangle")
def areatriangle(lado1, lado2, lado3):
  s=(lado1+lado2+lado3)/2
  area=float(s*(s-lado1)*(s-lado2)*(s-lado3))**(1/2)
  return area
lado1=float(input())
lado2=float(input())
lado3=float(input())
if lado1 <= 0:
    print('el radio es incorecto')
else:
  print(areatriangle(lado1,lado2,lado3))

