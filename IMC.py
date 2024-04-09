altura= float(input("Digite a altura "))
kg= float(input("Digite o Peso "))
imc= (kg/(altura*altura))
if imc < 18.5:
    print("Abaixo do peso ideal")
elif imc <= 24.9:
    print ("Peso ideal")
elif imc <= 29.9:
    print ("Levemente acima do peso")
elif imc <= 34.9:
    print ("Obesidade grau 1")
elif imc <= 39.9:
    print ("Obesidade grau 2(severa)")
elif imc >= 40:
    print("Obesidade grau 3 (mórbida)")
else:
    print ("erro")