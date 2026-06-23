soma = 0
for i in range(3,100,3):
    if i%2 == 1:
        soma += i
        print(i)
print(f"A soma dos ímpares múltiplos de 3 é igual a {soma} ")