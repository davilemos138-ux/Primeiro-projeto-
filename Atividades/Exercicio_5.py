salario = int(input("Digite seu salário bruto: "))
parcela = int(input("Digite o valor da parcela que deseja pagar: "))

parcela_max = salario * 0.3

if parcela <= parcela_max:
    print("Crédito Aprovado")
else:
    print("Crédito Recusado")