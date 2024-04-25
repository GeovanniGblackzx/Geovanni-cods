preco = float(input("Qual o valor do produto? R$"))
desconto = float (input("Qual a porcentagem de desconto? %"))
preco_final = preco - (preco * desconto / 100)
print ("O produto que custava", "R$",preco, "com o desconto ficou", "R$",preco_final)