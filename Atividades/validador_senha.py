senha = 223344

for i in range(3):
    senha_digitada = int(input("Digite a sua senha: "))
    if senha_digitada == senha:
        print("Acesso permitido")
        break
else:
    print("Conta bloqueada")