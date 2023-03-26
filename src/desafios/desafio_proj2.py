def mostrar_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Cliente
    [n] Cria Nova Conta
    [l] Listar Contas
    [q] Sair

    => """
    return menu

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
    else:
        print("Valor inválido para depósito")    
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques):
    
    if valor > limite:
        print("Limite de saque permitido é de R$ 500,00")
    elif valor > saldo:
        print("Não é possível sacar por falta de saldo")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque de R$ {valor:.2f}\n"
    else:
        print("Valor inválido para saque")    

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("***************** EXTRATO *****************")

    if extrato == "":
        print("Não foram realizadas movimentações")
    else:
        
        print(extrato)
        print(f"Saldo da conta é R$ {saldo:.2f}")

    print("*******************************************")    


def cadastrar_cliente(clientes):
    cpf = input("Informe o CPF: ")

    cliente = buscar_cliente(cpf, clientes)

    if cliente:
        print("Cliente já cadastrado")
        return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")
    clientes.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Cliente cadastrado com sucesso !")

def buscar_cliente(cpf, clientes):
    encontrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return encontrados[0] if encontrados else None


def criar_conta(agencia, contas, clientes):
    cpf = input("Informe o CPF do usuário: ")

    cliente = buscar_cliente(cpf, clientes)

    if cliente:
        num_conta = len(contas) + 1
        contas.append({"agencia": agencia, "numero_conta": num_conta, "cliente": cliente})
        print("Conta criada com sucesso !")
    else:
        print("Cliente não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(linha)


saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_depositos = 0
clientes = []
contas = []
AGENCIA = "0001"

print()
print("***************** DESAFIO *****************")

while True:

    opcao = input(mostrar_menu())

    if opcao == "d":
        print("Depositar valor R$: ", end=" ")
        valor = float(input())

        depositar(saldo, valor, extrato)

        numero_depositos += 1

    elif opcao == "s":

        if numero_saques < LIMITE_SAQUES:

            print("Sacar o valor R$: ", end=" ")
            valor = float(input())

            sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques)
        else:
            print("Limite de saque diário excedido")
        
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        cadastrar_cliente(clientes)

    elif opcao == "n":
        criar_conta(AGENCIA, contas, clientes)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break
       
