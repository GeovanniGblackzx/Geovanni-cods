print (" 1 milhas, 2 polegadas, 3 centímetros, 4 quilômetros, 5 metros, 6 pés")
medida = float(input("Qual a distância? "))
Opcao = int(input("Digite o numero correspondente: "))

if Opcao == 1:
    print ("A conversão de milhas para polegadas é", medida * 39370)
    print ("Para centímetros é ", (medida * 100000))
    print ("Para quilômetros é",  (medida / 1000))
    print ("Para pés é", (medida * 3281))
    print ("Para metros é", (medida * 1609))
elif Opcao == 2:
    print ("A conversão de polegadas para milhas é", medida / 63360)
    print ("Para centímetros é", (medida * 2,54))
    print ("Para quilômetros é", (medida / 39370))
    print ("Para pés é", (medida / 12))
    print ("Para metros é", (medida / 3937))
elif Opcao == 3:
    print ("A conversão de centímetros para milhas é", medida / 160900)
    print ("Para polegadas é", (medida / 2,54))
    print ("Para quilômetros é", (medida / 100000))
    print ("Para metros é", (medida / 100))
    print ("Para pés é", (medida / 3048))
elif Opcao == 4:
    print ("A conversão de quilômetros para milhas é", medida / 1609)
    print ("Para centímetros é", (medida * 100000))
    print ("Para polegadas é", (medida * 39370))
    print ("Para metros é", (medida / 1603))
    print ("Para pés é", (medida * 3281))
elif Opcao == 5:
    print ("A conversão de metros para milhas é", medida / 1609)
    print ("Para centímetros é", medida * 100))
    print ("Para polegadas é", medida * 3937))
    print ("Para pés é", medida * 3281))
    print ("Para quilômetros é", medida / 1000))
elif Opcao == 6:
    print ("A conversão de pés para milhas é", medida / 5280))
    print ("Para polegadas é", (medida / 12))
    print ("Para centímetros é", (medida * 3048))
    print ("Para quilômetros é", (medida / 3281))
    print ("Para metros é", (medida / 3281))
else:
    ("ERRO")
