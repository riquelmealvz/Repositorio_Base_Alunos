try:
    numero = int(input("Digite um numero: "))
    i = 1 
    while i <= 10:
        print(f"{i} x {numero} = {i * numero}")
        i += 1

except ValueError:
    print("Erro: Voce nao digitou um numero valido. ")