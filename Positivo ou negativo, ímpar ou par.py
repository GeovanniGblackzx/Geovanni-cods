num1 = float(input("Digite um número: "))
if num1 %2 == 0:
    print ("O número ", num1, "é par.")
    if num1 > 0:
        print("O Numero é Positivo")
    else:
        print("O Numero é Negativo")
elif num1 %1 == 0:
    print ("O número ", num1, "é ímpar.")
    if num1 > 0:
        print("O Numero é Positivo")
    else:
        print("O Numero é Negativo")
else:
    print ("Operação inválida.")