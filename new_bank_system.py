def formatar_valor(valor):
    return f"R$ {valor:.2f}"

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: {formatar_valor(valor)}")
        print(f"Depósito de {formatar_valor(valor)} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: {formatar_valor(valor)}")
        numero_saques += 1
        print(f"Saque de {formatar_valor(valor)} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n### EXTRATO ###")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo atual: {formatar_valor(saldo)}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None

    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    print("\n=== Conta corrente criada com sucesso! ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES_DIARIOS = 3
    AGENCIA = "0001"

    saldo = 0
    limite_saque = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta_sequencial = 1

    while True:
        menu = """
        \n### Menu ###
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas
        [q] Sair
        => """
        opcao = input(menu).lower()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite_saque, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES_DIARIOS)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            conta = criar_conta_corrente(AGENCIA, numero_conta_sequencial, usuarios, contas)
            if conta:
                numero_conta_sequencial += 1

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            print("Saindo do sistema. Obrigado por usar nossos serviços!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()


