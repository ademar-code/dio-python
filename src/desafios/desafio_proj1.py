menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_depositos = 0

print()
print("***************** DESAFIO *****************")

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depositar valor R$: ", end=" ")
        valor = float(input())
        saldo += valor

        extrato += f"Depósito de R$ {valor:.2f}\n"
        numero_depositos += 1

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            print("Sacar o valor R$: ", end=" ")
            valor = float(input())

            if valor > limite:
                print("Limite de saque permitido é de R$ 500,00")
            elif valor > saldo:
                print("Não é possível sacar por falta de saldo")
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque de R$ {valor:.2f}\n"

        else:
            print("Limite de saque diário excedido")

    elif opcao == "e":
        print("***************** EXTRATO *****************")

        if numero_depositos == 0 and numero_saques == 0:
            print("Não foram realizadas movimentações")
        else:
            
            print(extrato)
            print(f"Saldo da conta é R$ {saldo:.2f}")

        print("*******************************************")    

    elif opcao == "q":
        break
       
