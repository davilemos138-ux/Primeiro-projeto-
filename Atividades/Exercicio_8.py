
val_compra = float(input("Digite o valor da sua compra: "))

if val_compra <= 100:
    print(f"Sua compra foi de R$ {val_compra}, voce não teve desconto")

elif val_compra <=300:
    desconto = val_compra * 0.05
    valor_total = val_compra - desconto
    print (f"Sua compra foi de R$ {val_compra}, recebeu um desconto de R$ {desconto} e seu pagamento final será R$ {valor_total}")

elif val_compra <=500:
    desconto = val_compra *0.1
    valor_total = val_compra - desconto
    print (f"Sua compra foi de R$ {val_compra}, recebeu um desconto de R$ {desconto} e seu pagamento final será R$ {valor_total}")

else:
    desconto = val_compra * 0.15
    valor_total = val_compra - desconto
    print (f"Sua compra foi de R$ {val_compra}, recebeu um desconto de R$ {desconto} e seu pagamento final será R$ {valor_total}")








