try:
     nome = input("Digite seu nome: ")

     peso = float(input("Digite seu peso: "))
     altura = float(input("Digite sua altura: "))

     imc = peso / (altura * altura)

     if imc < 18.5:
          print("ABAIXO DO PESO🟦")
     elif imc < 24.9:
           print("PESO NORMAL🟩")
     elif imc < 29.9:
          print("SOBRE PESO🟨")
     elif imc < 34.9:
          print("OBESIDADE GRAU 1🟧")
     elif imc < 39.9:
          print("OBESIDADE GRAU 2🟥")
     else:
          print("OBESIDADE GRAU 3⬛")



     print(f"O IMC do aluno {nome} é : {imc}")

     with open("imc.txt", "a") as arquivo:
          arquivo.write(f"O nome do aluno e: {nome}e o imc e: {imc: .2f} ")

except ValueError:
     print("Peso invalido")