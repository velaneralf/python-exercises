nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if (media == 10.0):
    print ("Aprovado com Distinção.")
elif (media < 7.0):
    print ("Reprovado.")
elif (media >= 7.0):
    print ("Aprovado.")
