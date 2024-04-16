nota= float(input("Digite a nota "))
if nota >= 4 and nota <= 6:
    print ("Nota D")
elif nota >= 6 and nota <= 7.5:
    print ("Nota C")
elif nota >= 7.5 and nota <= 8.9:
    print ("Nota B")
elif nota >= 9:
    print("Nota A")
elif nota <= 3.9:
    print("Nota F")
else:
    print("error")