lado1 = float(input("Digite o primeiro lado "))
lado2 = float(input("Digite o segundo lado "))
lado3 = float(input("Digite o terceiro lado "))
if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print ("É possível formar um triângulo equilátero")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print ("É possível formar um triângulo escaleno")
else:
    print ("É possível formar um triângulo isósceles")
