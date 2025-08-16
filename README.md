# Atualizações do Sistema Bancário em Python (V2)

Esta atualização traz melhorias significativas para o sistema bancário, focando em modularização do código e adição de novas funcionalidades essenciais para o gerenciamento de usuários e contas.

## Melhorias na Modularização

As operações existentes de depósito, saque e extrato foram refatoradas em funções dedicadas, seguindo regras específicas de passagem de argumentos para demonstrar diferentes abordagens de design de funções em Python:

-   **`depositar(saldo, valor, extrato, /)`**: Esta função agora aceita argumentos **apenas por posição**. Isso significa que `saldo`, `valor` e `extrato` devem ser passados na ordem correta, sem o uso de palavras-chave.
    -   **Retorno**: Retorna o `saldo` atualizado e o `extrato` da conta.

-   **`sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`**: Esta função agora aceita argumentos **apenas por nome (keyword-only)**. Todos os argumentos devem ser passados utilizando suas palavras-chave (`saldo=...`, `valor=...`, etc.), o que aumenta a clareza e evita erros de ordem.
    -   **Retorno**: Retorna o `saldo` atualizado, o `extrato` e o `numero_saques` realizados.

-   **`exibir_extrato(saldo, /, *, extrato)`**: Esta função utiliza uma combinação de argumentos **por posição e por nome**. `saldo` deve ser passado por posição, enquanto `extrato` deve ser passado por nome.

## Novas Funcionalidades

Foram adicionadas duas novas funcionalidades cruciais para expandir as capacidades do sistema:

### 1. Cadastro de Usuário (`criar_usuario`)

-   Permite o cadastro de novos clientes no sistema.
-   Cada usuário é composto por: `nome`, `data de nascimento`, `cpf` e `endereço`.
-   O `CPF` é armazenado apenas com números e é utilizado como identificador único; o sistema impede o cadastro de usuários com CPFs duplicados.
-   O `endereço` é uma string formatada como: `logradouro, nro - bairro - cidade/sigla estado`.

### 2. Cadastro de Conta Corrente (`criar_conta_corrente`)

-   Permite a criação de novas contas bancárias e as vincula a um usuário existente.
-   Cada conta é composta por: `agência`, `número da conta` e `usuário` (referência ao objeto do usuário).
-   O `número da conta` é gerado sequencialmente, iniciando em 1.
-   O `número da agência` é fixo: `"0001"`.
-   Um usuário pode ter múltiplas contas, mas cada conta pertence a apenas um usuário.

### 3. Listagem de Contas (`listar_contas`)

-   Uma nova função foi adicionada para listar todas as contas cadastradas no sistema, exibindo a agência, número da conta e o nome do titular.

## Estrutura do Código

O código foi refatorado para incluir uma função `main()` que orquestra o fluxo principal do programa, gerenciando as variáveis de estado (saldo, extrato, usuários, contas) e integrando todas as novas funções através de um menu interativo no terminal.
