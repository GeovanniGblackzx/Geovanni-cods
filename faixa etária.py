Nome= str(input("Digite o nome "))
idade= float(input("Digite a idade "))
faixaetaria = (idade)
if faixaetaria <= 3:
    print("Bebê")
elif faixaetaria <= 12:
    print ("Criança")
elif faixaetaria <= 17:
    print ("Adolescente")
elif faixaetaria >= 18:
    print ("Adulto")
elif faixaetaria >= 60:
    print ("Idoso")
else:
    print ("erro")