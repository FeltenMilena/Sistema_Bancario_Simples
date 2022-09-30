from math import floor
import os
nome_do_cliente = ""
saldo_atual = 0
saldo_inicial = 0
qtd_dep_realizados = 0
valor_total_dep_realizados = 0
taxa_de_juros = 0
qtd_saques_realizados = 0
valor_total_saques_realizados = 0
valor_total_juros_recebidos = 0
saldo_min_conta = 0
saldo_max_conta = 0
saqueAtual = 0

imprimeNota200 = 0
imprimeNota100 = 0
imprimeNota50 = 0
imprimeNota20 = 0
imprimeNota10 = 0
imprimeNota5 = 0
imprimeNota2 = 0

def menu():
  os.system('cls' if os.name == 'nt' else 'clear')
  print('\n..:: Bem Vindo ao Sistema Bancário ::..\n')
  #print('1 - Abrir Conta')
  print('2 - Realizar Depósito')
  print('3 - Realizar Saque')
  print('4 - Aplicar Juros')
  print('5 - Simular Empréstimo')
  print('6 - Extrato')
  print('7 - Sair\n')
  item = input('Escolha uma opção: ')
  return item

def abrir_conta(conta):
  try:
    print('\n..:: Abertura de conta ::..\n')
    global nome_do_cliente
    nome_do_cliente = input("Digite seu nome: ")
    global saldo_atual
    saldo_atual = float(input("\nDigite o saldo inicial da conta: "))
    global saldo_inicial
    saldo_inicial = saldo_atual
    saldos_min_max_inicial() 
    return True
  except ValueError as err:
    print('\n..:: Operação Inválida ::..\n',err)
    return abrir_conta(False) 

def opcao_2():
  print('\n..:: Depósito Bancário ::..\n')
  try:
    valordeposito = float(input("Digite o valor a ser depositado: "))
    global saldo_atual
    saldo_atual += valordeposito
    print("Saldo atual: ", saldo_atual)
    global qtd_dep_realizados
    qtd_dep_realizados += 1
    global valor_total_dep_realizados
    valor_total_dep_realizados += valordeposito
    saldo_maximo()
  except ValueError as err:
    print("\n..:: Operação Inválida ::..\n", err)
    return opcao_2()

def opcao_3():
  print('\n ..:: Saque Bancário ::..\n')
  try:
    saque = float(input("Digite o valor a ser sacado: "))
    global saldo_atual
    if saldo_atual > saque and saque > 0:
      global valor_total_saques_realizados
      global saqueAtual
      saqueAtual = 0
      saqueAtual = saque
      funNota200(saque)
      saldo_minimo()
    else:
      return print("\n..:: Valor de Saque Não Permitido ::..")
  except ValueError as err:
    print("\n..:: Operação Inválida ::..\n", err)
    return opcao_3()

def opcao_4():
  print('\n..:: Aplicar Juros ::..\n')
  try:
    taxa_juros = float(input("Digite o valor da taxa de juros: "))
    if taxa_juros > 0:
      global taxa_de_juros
      taxa_de_juros = taxa_juros
      global valor_total_juros_recebidos
      valor_total_juros_recebidos += taxa_de_juros
      global saldo_atual
      saldo_atual = (saldo_atual * (1 + taxa_de_juros/100))
      saldo_maximo()
    else:
        print("\n..:: Taxa de Juros Inválida ::..")
  except ValueError as err:
    print("\n..:: Operação Inválida ::..\n", err)
    return opcao_4()

def opcao_5():
  print('\n..:: Simular Empréstimo ::..\n')
  try:
    valor = float(input("Digite o valor desejado: "))
    parcelasDig = int(input("\nDigite a quatidade de parcelas: "))
    parcelas = float(parcelasDig/12)
    montante= valor * ((1 + 7 / 100)** parcelasDig)
    global por_mes
    por_mes=montante % parcelas
    jurs = montante - valor
    por_mes= montante//parcelasDig

    print("\nValor total do empréstimo R${:.2f}".format(montante))
    print("Valor total de juros R${:.2f}".format(jurs))
    print("Serão {} parcelas de R${:.2f} por mês".format(parcelasDig, por_mes))
  except ValueError as err:
    print("\n..:: Operação Inválida ::..\n", err)
    return opcao_5()

def opcao_6():
  print('\n..........:: Extrato Bancário ::..........\n')
  print ('Nome do cliente . . . . . . . . . . . . . : ',nome_do_cliente)
  print ('Saldo Atual . . . . . . . . . . . . . . . : ',round(saldo_atual, 2))
  print ('Saldo Inicial . . . . . . . . . . . . . . : ',round(saldo_inicial, 2)) 
  print ('Quantidade de Depósitos Realizados. . . . : ',qtd_dep_realizados) 
  print ('Valor Total dos Depósitos Realizados. . . : ',round(valor_total_dep_realizados, 2)) 
  print ('Quantidade de Saques Realizados . . . . . : ',qtd_saques_realizados) 
  print ('Valor Total dos Saques Realizados . . . . : ',round(valor_total_saques_realizados, 2)) 
  print ('Valor Total dos Juros Recebidos . . . . . : ',round(valor_total_juros_recebidos, 2)) 
  print ('Saldo Mínimo da Conta . . . . . . . . . . : ',round(saldo_min_conta, 2)) 
  print ('Saldo Máximo da Conta . . . . . . . . . . : ',round(saldo_max_conta, 2))

def funNota200(saque):
    global imprimeNota200
    imprimeNota200 = 0
    if saque >= 200:
        nota200 = float(saque/200)
        notaFormatada = int(floor(nota200))
        resultado = float(nota200 - notaFormatada)
        if resultado == 0:
            imprimeNota200 = (nota200 - resultado)
            return  imprimirNotas()
        else:
            imprimeNota200 = (nota200 - resultado)
            return funNota100(resultado)
    else:
        return funNota100(saque/200)

def funNota100(resultado):
  global imprimeNota100
  imprimeNota100 = 0
  resultado100 = round((resultado*200), 4)
  if resultado100 >= 100:
      nota100 = float(resultado100/100)
      notaFormatada = int(floor(nota100))
      resultado100 = float(nota100 - notaFormatada)
      if resultado100 == 0:
          imprimeNota100 = (nota100 - resultado100)
          return  imprimirNotas()
      else:
          imprimeNota100 = (nota100 - resultado100)
          return funNota50((resultado100/2))
  else:
      return funNota50(resultado)

def funNota50(resultado):
    global imprimeNota50
    imprimeNota50 = 0
    resultado50 = round((resultado*200),4)
    if resultado50 >= 50:
        nota50 = float(resultado50/50)
        notaFormatada = int(floor(nota50))
        resultado50 = float(nota50 - notaFormatada)
        if resultado50 == 0:
            imprimeNota50 = (nota50 - resultado50)
            return  imprimirNotas()
        else:
            imprimeNota50 = (nota50 - resultado50)
            return funNota20((resultado50/4))
    else:
        return funNota20(resultado)

def funNota20(resultado):
    global imprimeNota20
    imprimeNota20 = 0
    resultado20 = round((resultado*200),4)
    if resultado20 >= 20:
        nota20 = float(resultado20/20)
        notaFormatada = int(floor(nota20))
        resultado20 = float(nota20 - notaFormatada)
        if resultado20 == 0:
            imprimeNota20 = (nota20 - resultado20)
            return  imprimirNotas()
        else: 
            imprimeNota20 =  (nota20 - resultado20)
            return funNota10((resultado20/10))
    else:
        return funNota10(resultado)

def funNota10(resultado):
    global imprimeNota10
    imprimeNota10 = 0
    resultado10 = round((resultado*200),4)
    if resultado10 >= 10:
        nota10 = float(resultado10/10)
        notaFormatada = int(floor(nota10))
        resultado10 = float(nota10 - notaFormatada)
        if resultado10 == 0: 
            imprimeNota10 = (nota10 - resultado10)
            return  imprimirNotas()
        else: 
            imprimeNota10 = (nota10 - resultado10)
            return funNota5e2((resultado10/20))
    else:
        return funNota5e2(resultado)

def funNota5e2(resultado):
    global imprimeNota5
    imprimeNota5 = 0
    resultado5 = round((resultado*200),4)
    if (resultado5 >=2 and resultado5 < 3) or resultado5 > 3  :
      if resultado5>=9 or (resultado5>=5 and resultado5<6) or (resultado5>=7 and resultado5<8):
        nota5 = float(resultado5/5)
        notaFormatada = int(floor(nota5))
        resultado5 = float(nota5 - notaFormatada)
        if resultado5 == 0:
            imprimeNota5 = (nota5 - resultado5)
            return  imprimirNotas()
        else: 
            imprimeNota5 = (nota5 - resultado5)
            return funNota2((resultado5/40))
      else:
        return funNota2(resultado)
    else:
      global saldo_atual
      print("Saldo Atual: ", saldo_atual)
      return print("\n..:: Operação Inválida ::..")

def funNota2(resultado):
  global imprimeNota2
  imprimeNota2 = 0
  resultado2 = round((resultado*200),4)
  nota2 = floor(resultado2/2)
  imprimeNota2 = (nota2 - resultado)
  return  imprimirNotas()

def imprimirNotas():
  global imprimeNota200
  global imprimeNota100
  global imprimeNota50
  global imprimeNota20
  global imprimeNota10
  global imprimeNota5
  global imprimeNota2
  global qtd_saques_realizados
  print("")
  if imprimeNota200 > 0:
    print("{:.0f} nota(s) de R$ 200 para saque".format(imprimeNota200))
  if imprimeNota100 > 0:
    print("{:.0f} nota(s) de R$ 100 para saque".format(imprimeNota100))
  if imprimeNota50 > 0:
    print("{:.0f} nota(s) de R$ 50 para saque".format(imprimeNota50))
  if imprimeNota20 > 0:
    print("{:.0f} nota(s) de R$ 20 para saque".format(imprimeNota20))
  if imprimeNota10 > 0:
    print("{:.0f} nota(s) de R$ 10 para saque".format(imprimeNota10))
  if imprimeNota5 > 0:
    print("{:.0f} nota(s) de R$ 5 para saque".format(imprimeNota5))
  if imprimeNota2 > 0:
    print("{:.0f} nota(s) de R$ 2 para saque".format(imprimeNota2))
  print("\nSaque Realizado com Sucesso...\n")
  qtd_saques_realizados += 1
  global saqueAtual
  global saldo_atual
  global valor_total_saques_realizados
  valor_total_saques_realizados += saqueAtual
  saldo_atual = saldo_atual - saqueAtual
  print("Saldo Atual: ", saldo_atual)

def saldo_minimo():
  global saldo_min_conta
  global saldo_atual
  
  if saldo_atual < saldo_min_conta:
    saldo_min_conta = saldo_atual

def saldo_maximo():
  global saldo_max_conta
  global saldo_atual
  
  if saldo_atual > saldo_max_conta:
    saldo_max_conta = saldo_atual

def saldos_min_max_inicial():
    global saldo_min_conta
    global saldo_max_conta
    global saldo_atual
    saldo_min_conta = saldo_atual
    saldo_max_conta = saldo_atual

if __name__ == '__main__':
  escolha = '0'
  abertaconta = False
  while(escolha != '7'):
    if abertaconta !=True:
      conta = False
      abertaconta = abrir_conta(conta)
    else:
      escolha = menu()
      if escolha == '2':
        opcao_2()
      elif escolha == '3':
        opcao_3()
      elif escolha == '4':
        opcao_4()
      elif escolha == '5':
        opcao_5()
      elif escolha == '6':
        opcao_6()
      elif escolha == '7':
        print('\nSaindo...')
      else:
        print('\n..:: Opção desconhecida! ::..\n')
      
    input('\nPressione ENTER para continuar ')