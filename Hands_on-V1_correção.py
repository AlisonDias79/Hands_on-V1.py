menu = """

[1] Depositar
[2] sacar
[3] Extrato
[0] sair

=>"""

saldo = 300
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "1":
      valor = float(input("Informe o valor do depósito: "))

      if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
      else:
         print("Erro na operação, o valor informado é invalido")

  elif opcao == "2":
     valor = float(input("Informe o valor do saque: "))

     excedeu_saldo = valor > saldo
     excedeu_limite = valor > limite
     excedeu_saque = numero_saques >= LIMITE_SAQUES

     if excedeu_saldo:
        print("Erro na operação, saldo insuficiente. ")
     elif excedeu_limite:
        print("Erro na operação, valor de saque excede o limite. ")  
     elif excedeu_saque:
        print("Erro na operação, numero maximo de saque excedido. ") 
     elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

     else:
        print("Erro na operação, o valor informado é invalido. ")




  elif opcao == "3":
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"saldo: R$ {saldo:.2f}")
    print("===============================") 

  elif opcao == "0":
     
     print("Obrigado por usar nosso sistema bancario!")
     break
    

  else:
       print("Operação inválida, por favor selecione novamente a operação desejada.")
       
         