r1 = input("Digite o primeiro comprimento da reta de um triangulo: ")
r2 = input("Digite o segundo comprimento da reta de um triangulo: ")
r3 = input("Digite o terceiro comprimento da reta de um triangulo: ")

soma = r1 + r2
soma = r1 + r3
soma = r2 + r3

if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1:
    print("Triangulo inválido")
elif r1 != r2 != r3:
    print ("Escaleno")
elif r1 == r2 == r3:
    print ("Equilátero")
else:
    print("Isósceles")





