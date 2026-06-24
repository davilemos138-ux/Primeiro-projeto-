maiores = 0
menores = 0

for i in range (1,8):
    ano_nasc = int(input(f"Digite o ano de nascimento {i} : "))
    idade = 2026 - ano_nasc

    if idade >= 18:
        maiores += 1

    else:
        menores += 1

print(f"Os maiores de idade são {maiores} e os menores {menores}")


