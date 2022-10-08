# Sistema Bancário Simplificado

O programa deverá conter um menu com as seguintes funcionalidades:

1. Abrir conta:  Inicializa a conta de um cliente, solicitando seu nome e saldo inicial. Após
criada, esta opção do menu deve ser desabilitada. Sem conta aberta, as demais opções do
menu também devem ser desabilitadas, com exceção do item “Sair”.

2. Realizar depósito: Solicita ao usuário o valor a ser depositado, obrigatoriamente numérico e
maior que zero. Caso afirmativo, atualiza e mostra na tela o novo saldo.

3. Realizar saque: Solicita ao usuário o valor a ser sacado, obrigatoriamente numérico e maior
que zero. Caso o saldo seja insuficiente, mostra mensagem na tela e não realiza o saque. Caso
tenha saldo suficiente, mostra na tela uma lista com as quantidades e valores das notas a
serem liberadas, priorizando sempre notas de valores mais altos. Como o caixa eletrônico
possui somente notas, não moedas, deve ser possível gerar o valor solicitado com as notas
disponíveis. Do contrário, mostra mensagem na tela e não realiza o saque. Se a operação foi
realizada, atualiza e mostra na tela o novo saldo.

4. Aplicar juros: Solicita uma taxa de juros, obrigatoriamente maior que zero, atualiza e mostra
na tela o novo saldo.

5. Simular   empréstimo:  Solicita o valor a ser emprestado,  a taxa  de  juros mensal  e a
quantidade de parcelas para pagamento, todos obrigatoriamente numéricos e maiores que
zero. Em seguida, mostre na tela o valor de cada parcela, a quantidade total de juros a ser
pago e o somatório dos valores de todas as parcelas.

6. Extrato: Mostra um relatório na tela com as seguintes informações:

  	• Nome do cliente

  	• Saldo inicial

  	• Saldo atual

  	• Quantidade de depósitos realizados

  	• Valor total dos depósitos realizados

  	• Quantidade de saques realizados

  	• Valor total dos saques realizados

  	• Valor total dos juros recebidos

  	• Saldos mínimo e máximo da conta

7. Sair: Encerra o programa.
