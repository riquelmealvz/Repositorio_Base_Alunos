try:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    possui_carteira = input("1-sim | 2-nao: ")

    if idade >= 18:
        print("Voce é maior de idade !!!")
        if possui_carteira == "sim":
            print("Pode DIRIGIR")
        else:    
            print("NAO PODE DIRIGIR!")
    else:
        print("Menor de idade!")
   
except ValueError:
    print("Idade errada")