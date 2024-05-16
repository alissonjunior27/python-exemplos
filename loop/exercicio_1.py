n=int(input('digite quantos numeros voce quer calcular na media: '))
soma = 0
iteracao = 1
while iteracao<=n:
    numero = float(input("digite um numero: "))
    soma += numero
    iteracao+=1
print(f"a media é {soma/n}")
