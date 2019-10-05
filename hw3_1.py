def calc(a):
    contador=len(str(a))
    return contador
a=int(input())
if a<=0:
    print('el contador incorecto')
else:
  print(calc(a))

