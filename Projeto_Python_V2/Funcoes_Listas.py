import time

#LISTAS
#lista carrinho
carrinho = [[],[],[]]
historico = [[],[],[]]

def imprimir_carrinho():
  somaFatura = 0
  for y in range(len(carrinho[0])): #AMOSTRA DO CARRINHO
    print(f'[{y+1}] - {carrinho[0][y]:.<30} --> R${carrinho[1][y]} Quantidade: {carrinho[2][y]}')
    somaFatura += ((carrinho[1][y])*(carrinho[2][y])) 
    time.sleep(0.25)
  print(f"\nValor total R${somaFatura:.2f}") #VALOR TOTAL
  return somaFatura

def incluindo_historico():
  for i in range(len(carrinho[0])):
    historico[0].append(carrinho[0][i])
    historico[1].append(carrinho[1][i])
    historico[2].append(carrinho[2][i])

def imprimir_historico():
  if len(historico[0]) != 0:
    somaFatura = 0
    for y in range(len(historico[0])): #AMOSTRA DO CARRINHO
      print(f'[{y+1}] - {historico[0][y]:.<30} --> R${historico[1][y]} Quantidade: {historico[2][y]}')
      somaFatura += ((historico[1][y])*(historico[2][y])) 
      time.sleep(0.25)
    print(f'\nValor total R${somaFatura:.2f}') #VALOR TOTAL
    if FormaPagamento == "C":
      if credito_debito == "C":
        print(f'Forma de pagamento: Cartão - Crédito\nParcelado em {parcelas}x de R${valorParceladoHistorico}')
      else:
        print('Forma de pagamento: Cartão - Débito')
    elif FormaPagamento == "D":
      print('Forma de pagamento: Dinheiro')
    else:
      print('Forma de pagamento: PIX')
    print('='*50)
    print('          Agradecemos pela preferência!')
    print('             OFICINA BORRACHA FORTE    ')
    print('='*50)
  else:
    print('='*50)
    print('          Agradecemos pela preferência!')
    print('             OFICINA BORRACHA FORTE    ')
    print('='*50)

# if FormaPagamento == "C":
    # if credito_debito == "C":
      # print(f'Forma de pagamento: Cartão - Crédito\nParcelado em {parcelas}x de R${valorParceladoHistorico}')
    # else:
      # print('Forma de pagamento: Cartão - Débito')
  # elif FormaPagamento == "D":
    # print('Forma de pagamento: Dinheiro')
  # else:
    # print('Forma de pagamento: PIX')
  # print('='*50)
  # print('Agradecemos pela preferência!')
  # print('   OFICINA BORRACHA FORTE    ')
  # print('='*50)

# Lista de Produtos
lista_prod = (
    [['Pneu(s)', 'Calota(s)', 'Palheta(s)',
    'Protetor(es) de Volante', 'Cheirinho(s) de Carro', 
    'Óleo de Motor', 'Bateria(s)'],
    [339.00, 15.00, 55.00, 30.00, 15.00, 27.00, 270.00]]
)

def imprimir_prod():
    for i in range(len(lista_prod[0])):
        print(f'[{i+1}] - {lista_prod[0][i]:.<30} --> R${lista_prod[1][i]}')
        time.sleep(0.25)

# Lista de Serviços
lista_serv = (
    [['Troca de Óleo', 'Alinhamento', 'Revisão Geral',
     'Troca de Lampada', 'Troca de Correia','Troca de Pastilha de Freio'],
     [200.00, 60.00, 300.00, 40.00, 220.00, 150.00]]
)

def imprimir_serv():
    for i in range(len(lista_serv[0])):
        print(f'[{i+1}] - {lista_serv[0][i]:.<30} --> R${lista_serv[1][i]}')
        time.sleep(0.25)

# Lista menu principal
lista_menu_principal = (
    ['Adicionar Produto','Adicionar Serviço','Remover Produto ou Serviço',
    'Limpar carrinho','Extrato','Finalizar Compra','Sair']
)

def imprimir_menu_principal():
    for x in range(len(lista_menu_principal)):
        print(f'[{x+1}] - {lista_menu_principal[x]}')
        time.sleep(0.8)

def imprimir_rmvProduto():
  lista_rmvProduto = (['Digite [P] para remover um produto/serviço',
  'Digite [Q] para diminuir a quantidade de seu produto',
  'Digite [M] para voltar ao MENU PRINCIPAL']
  )

  for l in lista_rmvProduto:
    print(l)
    time.sleep(0.8)

def imprimir_forma_pagamento():
  lista_forma_pagamento = (
      ['[C] - Cartão',
      '[D] - Dinheiro',
      '[P] - PIX']
      )

  for l in lista_forma_pagamento:
    print(l)
    time.sleep(0.8)

#FUNÇÕES

def carregando():
    lista_carregando = (
      ["Carregando","Carregando.",
      "Carregando..","Carregando..."]
      )

    for l in lista_carregando:
      time.sleep(0.25)
      print(l, end="\r")
      time.sleep(0.25)
    print(lista_carregando[-1])
    print('='*50)

def saindo():
  lista_saindo = (
    ["saindo","saindo.",
    "saindo..","saindo..."]
    )

  for l in lista_saindo:
    time.sleep(0.25)
    print(l, end="\r")
    time.sleep(0.25)
  print(lista_saindo[-1])
  print('='*50)

def adicionando_prod(nome_produto):

  lista_adicionando = (
    [f'Adicionando "{nome_produto}" ao seu carrinho',
    f'Adicionando "{nome_produto}" ao seu carrinho.',
    f'Adicionando "{nome_produto}" ao seu carrinho..',
    f'Adicionando "{nome_produto}" ao seu carrinho...']
    )

  for l in lista_adicionando:
    time.sleep(0.25)
    print(l, end="\r")
    time.sleep(0.25)
  print(lista_adicionando[-1])

def adicionando_serv(nome_servico):
    lista_adicionando = (
      [f'Adicionando "{nome_servico}" ao seu carrinho',
      f'Adicionando "{nome_servico}" ao seu carrinho.',
      f'Adicionando "{nome_servico}" ao seu carrinho..',
      f'Adicionando "{nome_servico}" ao seu carrinho...']
      )

    for l in lista_adicionando:
      time.sleep(0.25)
      print(l, end="\r")
      time.sleep(0.25)
    print(lista_adicionando[-1])

def limpando():
    lista_limpando = (
      ['Limpando seu carrinho',
      'Limpando seu carrinho.',
      'Limpando seu carrinho..',
      'Limpando seu carrinho...']
      )

    for l in lista_limpando:
      time.sleep(0.25)
      print(l, end="\r")
      time.sleep(0.25)
    print(lista_limpando[-1])
    print('='*50)

def removendo(nome_produto, quantidade):
  lista_removendo = (
    [f'Removendo {quantidade} {nome_produto} do seu carrinho',
    f'Removendo {quantidade} {nome_produto} do seu carrinho.',
    f'Removendo {quantidade} {nome_produto} do seu carrinho..',
    f'Removendo {quantidade} {nome_produto} do seu carrinho...']
    )

  for l in lista_removendo:
    time.sleep(0.25)
    print(l, end="\r")
    time.sleep(0.25)
  print(lista_removendo[-1])
  print('='*50)

def inicio():
  print('='*50)
  print('''Como deseja prosseguir?\n
  > Para acessar o programa basta digitar [A]
  > Caso queira finalizar o programa, digite [F]\n''')
  acessar = input('Escolha sua opção: ').upper()
  print('='*50)
  time.sleep(1)
  while acessar != 'A' and acessar != 'F':
    print("""Opção inválida!\n     
    > Para acessar o programa basta digitar [A]
    > Caso queira finalizar o programa, digite [F]\n""")
    acessar = input('Escolha sua opção: ').upper()
    print('='*50)
    time.sleep(3)
  return acessar

def boas_vindas():
  print('Bem vindo a Oficina Borracha Forte!')
  time.sleep(1.75)
  print('='*50)
  time.sleep(1.75)

def menu_principal():
  #Valor total gasto
  somaFatura = 0
  for y in range(len(carrinho[0])): #AMOSTRA DO CARRINHO
    somaFatura += ((carrinho[1][y])*(carrinho[2][y])) 
  
  #MENU
  print(f'MENU PRINCIPAL   Valor total R${somaFatura:.2f}\n')
  time.sleep(1)
  imprimir_menu_principal()
  opcao = int(input('\nEscolha a opção que deseja: '))
  print('='*50)
  time.sleep(0.8)
  while opcao < 1 or opcao > 7:
    print('Opção inválida!')
    opcao = int(input('\nEscolha a opção que deseja: '))
    print('='*50)
    time.sleep(3)
  return opcao

def adcProd():
  while True:
    print('Opções de produto:\n')
    time.sleep(0.8)
    imprimir_prod()
    print('\nPara voltar ao menu principal basta digitar [0]')
    print('='*50)
    #CARRINHO 
    prod_serv = int(input('Adicione um produto ao seu carrinho: '))
    print('='*50)
    if prod_serv >= 1 and prod_serv <= (len(lista_prod[0])):
      carrinho[0].append(lista_prod[0][prod_serv-1])
      carrinho[1].append(lista_prod[1][prod_serv-1])
      quant = int(input(f'Qual seria a quantidade de "{lista_prod[0][prod_serv-1]}" (MÁX. 10): ')) #QUANTIDADE DE PRODUTO
      print('='*50)
      while quant <= 0 or quant > 10:
        quant = int(input('Valor inválido! Digite novamente a quantidade: '))
        print('='*50)
      adicionando_prod(lista_prod[0][prod_serv-1])
      print('='*50)
      time.sleep(3)
      carrinho[2].append(quant)
    elif prod_serv == 0: #SAÍDA DA FUNÇÃO
      saindo()
      break
    else: #OPÇÃO INVÁLIDA
      print('Este número não está entre as opções!!')
      print('='*50)
      time.sleep(3)

def adcServ():
  while True:
    print('Opções de serviços:\n')
    time.sleep(0.8)
    imprimir_serv()
    print('\nPara voltar ao menu principal basta digitar [0]')
    print('='*50)
    #CARRINHO 
    prod_serv = int(input('Adicione um serviço ao seu carrinho: '))
    print('='*50)
    if prod_serv >= 1 and prod_serv <= (len(lista_serv[0])):
      carrinho[0].append(lista_serv[0][prod_serv-1])
      carrinho[1].append(lista_serv[1][prod_serv-1])
      quant = int(input(f'Qual seria a quantidade de "{lista_serv[0][prod_serv-1]}" (MÁX. 10): ')) #QUANTIDADE DE PRODUTO
      print('='*50)
      while quant <= 0 or quant > 10:
        quant = int(input('Valor inválido! Digite novamente a quantidade: '))
        print('='*50)
      adicionando_prod(lista_serv[0][prod_serv-1])
      print('='*50)
      time.sleep(3)
      carrinho[2].append(quant)
    elif prod_serv == 0: #SAÍDA DA FUNÇÃO
      saindo()
      break
    else: #OPÇÃO INVÁLIDA
      print('Este número não está entre as opções!!')
      print('='*50)
      time.sleep(3)

def limparcar(): #FUNÇÃO LIMPEZA DO CARRINHO
  somaFatura = 0
  for y in range(len(carrinho[0])): #AMOSTRA DO CARRINHO
    print(f'[{y+1}] - {carrinho[0][y]:.<30} --> R${carrinho[1][y]} Quantidade: {carrinho[2][y]}')
    somaFatura += ((carrinho[1][y])*(carrinho[2][y])) 
  print(f'\nValor total R${somaFatura:.2f}') #VALOR TOTAL
  print('='*50)
  print('\n[S] para sim\n[N] para não\n') #CONFIRMAÇÃO DA AÇÃO
  certeza = input(f'Tem certeza que deseja remover TUDO de seu carrinho? ').upper()[0] 
  print('='*50)
  while (certeza != 'S') and (certeza != 'N'):
    certeza = input('Opção inválida! Digite [S] para sim [N] para não: ').upper()[0] 
    print('='*50)
  if certeza == 'S': #CONFIRMAÇÃO = SIM - LIMPEZA DO CARRINHO
    carrinho[0].clear()
    carrinho[1].clear()
    carrinho[2].clear()
    limpando()
  else: #CONFIRMAÇÃO = NÃO
    print('Seus produtos foram mantidos no carrinho!')
    print('='*50)
    time.sleep(3)


    
def rmvProduto(): #FUNÇÃO REMOVER PRODUTO/SERVIÇO
  while True:
    print('Dentro do carrinho:\n')
    time.sleep(0.8)
    imprimir_carrinho()
    print('='*50)
    #ESCOLHA DE OPÇÕES DE REMOÇÃO - PRODUTO OU QUANTIDADE
    imprimir_rmvProduto()
    produto_ou_quantidade = input('\nEscolha uma das opções acima: ').upper()[0]
    print('='*50)
    time.sleep(1)
    while (produto_ou_quantidade != 'P') and (produto_ou_quantidade != 'Q') and (produto_ou_quantidade != 'M'):
      produto_ou_quantidade = input('As únicas opções válidas são [P], [Q] ou [M]: ').upper()[0]
      print('='*50)
      time.sleep(3)
    if produto_ou_quantidade == 'M': #SAÍDA DA FUNÇÃO
      saindo()
      break
    elif produto_ou_quantidade == 'P': #REMOÇÃO DE PRODUTO
      remove = int(input('Informe qual produto irá remover: '))
      print('='*50)
      time.sleep(1)
      while remove < 1 or remove > len(carrinho[0]):
        remove = int(input('Este produto não está na lista! Informe novamente qual produto irá remover: '))
        print('='*50)
        time.sleep(3)
    elif produto_ou_quantidade == 'Q': #REMOÇÃO POR QUANTIDADE
      escolheProdRem = int(input('Informe de qual item irá reduzir a quantidade: ')) #APONTAR PRODUTO
      print('='*50)
      time.sleep(1)
      while escolheProdRem < 1 or escolheProdRem > len(carrinho[2]):
        escolheProdRem = int(input('Este produto não está na lista! Informe novamente qual produto irá reduzir a quantidade: '))
        print('='*50)
        time.sleep(3)
      removeQuantidade = int(input(f'Gostaria de remover quantos de "{carrinho[0][escolheProdRem-1]}": ')) #REMOÇÃO DA QUANTIDADE DESSE PRODUTO
      print('='*50)
      time.sleep(1)
      while removeQuantidade <= 0 or removeQuantidade > carrinho[2][escolheProdRem-1]:
        removeQuantidade = int(input(f'Tirar este valor é impossível! Gostaria de remover quantos de "{carrinho[0][escolheProdRem-1]}": '))
        print('='*50)
        time.sleep(3)
    print('[S] para sim\n[N] para não\n')
    certeza = input(f'Confirme a sua ação: ').upper()[0] #CONFIRMAÇÃO DA AÇÃO
    print('='*50)
    time.sleep(1)
    while (certeza != 'S') and (certeza != 'N'):
      certeza = input('Opção inválida! Digite [S] para sim [N] para não: ').upper()[0] 
      print('='*50)
      time.sleep(3)
    if certeza == 'S': #CONFIRMAÇÃO = SIM
      if produto_ou_quantidade == 'P': #REMOÇÃO DO PRODUTO
        removendo(carrinho[0][remove-1],carrinho[2][remove-1])
        del carrinho[0][remove-1]
        del carrinho[1][remove-1]
        del carrinho[2][remove-1]        
      elif produto_ou_quantidade == 'Q':
        if removeQuantidade == carrinho[2][escolheProdRem-1]: #SE REMOÇÃO DA QUANTIDADE FOR IGUAL A QUANTIDADE DO CARRINHO
          removendo(carrinho[0][escolheProdRem-1],removeQuantidade)
          del carrinho[0][escolheProdRem-1]
          del carrinho[1][escolheProdRem-1]
          del carrinho[2][escolheProdRem-1]         
        else:
          removendo(carrinho[0][escolheProdRem-1],removeQuantidade)
          carrinho[2][escolheProdRem-1] -= removeQuantidade #REMOVE QUANTIDADE PEDIDA QUANDO MENOR QUE A QUANTIDADE DO PRODUTO         
    else: #CONFIRMAÇÃO = NÃO - MANTÉM PRODUTO OU MESMA QUANTIDADE NO CARRINHO
      print('O produto não foi removido de seu carrinho!')
      print('='*50)
      time.sleep(3)
  
def extrato(): #FUNÇÃO EXTRATO CARRINHO
  while True:
    imprimir_carrinho()
    sair_extrato = int(input('\nDigite [0] para sair: '))
    print('='*50)
    while sair_extrato != 0:
      sair_extrato = int(input('Dado inválido! Digite 0 para sair: '))
      print('='*50)
    if sair_extrato == 0: #OPÇÃO DE SAÍDA DA FUNÇÃO
      saindo()
      break

def pagamento():
  global valorParceladoHistorico
  carregando()
  print('Gostaria de dar procedimento a finalização da compra ou gostaria de desistir?\n') #CHANCE DE DESISTÊNCIA DA COMPRA
  print('[P] para prosseguir\n[D] para desistir\n')
  certeza = input(f'Confirme a sua ação: ').upper()[0] 
  print('='*50)
  time.sleep(1)
  while (certeza != 'P') and (certeza != 'D'):
    certeza = input('Opção inválida! Digite [P] para prosseguir [D] para desistir: ').upper()[0] 
    print('='*50)
    time.sleep(3)
  if certeza == 'D': #DESISTÊNCIA (1ªCONFIRMAÇÃO) - MOSTRA OS PRODUTOS QUE ESTÁ DESISTINDO
    print('Você tem certeza? Essa é o conteúdo de seu carrinho:\n')
    imprimir_carrinho()
    print('='*50)
    print('[S] para sim\n[N] para não\n') #DESISTÊNCIA (2ªCONFIRMAÇÃO) - LIMPEZA DO CARRINHO E SAÍDA DIRETA DO PROGRAMA
    certeza = input('Confirme sua ação: ').upper()[0]
    print('='*50)
    time.sleep(1)
    while (certeza != 'S') and (certeza != 'N'):
      certeza = input('Opção inválida! Confirme sua ação: ').upper()[0]
      print('='*50)
      time.sleep(3)
    if certeza == 'S':
      carrinho[0].clear()
      carrinho[1].clear()
      carrinho[2].clear()
      limpando()
      print('VOLTE SEMPRE!')
      print('='*50)
      time.sleep(3)
      return "desistir"
    else:
      carregando()
  else: #FINALIZAR COMPRA - FORMA DE PAGAMENTO
    imprimir_carrinho()
    print('='*50)
    print('Qual será a forma de pagamento?\n')
    time.sleep(0.8)
    imprimir_forma_pagamento()
    global FormaPagamento
    FormaPagamento = str(input('\nEscolha a forma de pagamento: ')).upper()[0]
    print('='*50)
    time.sleep(1)
    while (FormaPagamento != 'D') and (FormaPagamento != 'C') and (FormaPagamento != 'P'):
      FormaPagamento = str(input('Esta opcção não é válida! Escolha a forma de pagamento: ')).upper()[0]
      print('='*50)
      time.sleep(3)
    if FormaPagamento == 'D': #FORMA DE PAGAMENTO - DINHEIRO
      somaFatura = imprimir_carrinho()
      dinheiro = int(input('\nDigite o valor do pagamento: '))
      print('='*50)
      time.sleep(1)
      while dinheiro < somaFatura:
        dinheiro = int(input('Quer sair devendo? Digite o valor: '))
        print('='*50)
        time.sleep(3)
      troco = dinheiro - somaFatura
      print(f'Troco do cliente: R${troco}')
      cont50n = 0
      cont20n = 0
      cont10n = 0
      cont5n = 0
      cont2n = 0
      cont1n = 0
      while troco > 0:
        if troco >= 50:
          troco -= 50
          cont50n +=1
        elif troco >= 20:
          troco -= 20
          cont20n += 1
        elif troco >= 10:
          troco -= 10
          cont10n += 1
        elif troco >= 5:
          troco -= 5
          cont5n += 1
        elif troco >= 2:
          troco -= 2
          cont2n += 1
        elif troco >= 1:
          troco -= 1
          cont1n += 1
      lista_cont = [cont50n, cont20n, cont10n, cont5n, cont2n, cont1n]
      lista_cedulas = [50, 20, 10, 5, 2, 1]
      for i, v in zip(lista_cont, lista_cedulas):
        if i > 0:
          print(f'{i} cédula(s) de {v} reais')
      print('='*50)
      incluindo_historico()
      carrinho[0].clear()
      carrinho[1].clear()
      carrinho[2].clear()
      time.sleep(3)
    elif FormaPagamento == 'C': #FORMA DE PAGAMENTO - CARTÃO
      somaFatura = imprimir_carrinho()
      print('='*50)
      print('\n[C] - Crédito\n[D] - Débito') #CRÉDITO OU DÉBITO
      global credito_debito
      credito_debito = str(input('\nEscolha entre Crédito ou Débito: ')).upper()[0]
      print('='*50)
      time.sleep(1)
      while (FormaPagamento != 'D') and (FormaPagamento != 'C'):
        credito_debito = str(input('Dado inválido! Escolha entre Crédito ou Débito: ')).upper()[0]
        print('='*50)
        time.sleep(3)
      if credito_debito == 'C': #CRÉDITO
        print('Obs: Parcelas acima de 3x acarretará juros de 3%. Máximo de parcelas: 10') #
        global parcelas
        parcelas = int(input('\nDeseja parcelar em quantas vezes: '))
        print('='*50)
        time.sleep(1)
        while parcelas <= 0 or parcelas > 10:
          parcelas = int(input('Inválido! Deseja parcelar em quantas vezes: '))
          print('='*50)
          time.sleep(1)
        if parcelas >= 1 and parcelas <= 3:
          somaFatura /= parcelas
          valorParceladoHistorico = somaFatura
          print(f'O valor parcelado em {parcelas}x fica: R${somaFatura:.2f}')
          print('='*50)
          time.sleep(3)
          print('Pago com sucesso!')
          print('='*50)
          time.sleep(3)
          incluindo_historico()
          carrinho[0].clear()
          carrinho[1].clear()
          carrinho[2].clear()
          time.sleep(3)
        elif parcelas == 0:
          valorParceladoHistorico = somaFatura
          print(f'O valor parcelado em {parcelas}x fica: R${somaFatura:.2f}')
          print('='*50)
          time.sleep(3)
          print('Pago com sucesso!')
          print('='*50)
          incluindo_historico()
          carrinho[0].clear()
          carrinho[1].clear()
          carrinho[2].clear()
          time.sleep(3)
        else:
          somaFatura /= parcelas
          somaFatura * 1.03
          valorParceladoHistorico = somaFatura
          print(f'O valor parcelado em {parcelas}x fica: R${somaFatura:.2f}')
          print('='*50)
          time.sleep(3)
          print('Pago com sucesso!')
          print('='*50)
          incluindo_historico()
          carrinho[0].clear()
          carrinho[1].clear()
          carrinho[2].clear()
          time.sleep(3)
      elif credito_debito == 'D': #DÉBITO
        print('Pagamento realizado com sucesso!')
        print('='*50)
        incluindo_historico()
        carrinho[0].clear()
        carrinho[1].clear()
        carrinho[2].clear()
        time.sleep(3)       
    else: #FORMA DE PAGAMENTO - PIX
      print('Pagamento com PIX realizado com sucesso!')
      print('='*50)
      incluindo_historico()
      carrinho[0].clear()
      carrinho[1].clear()
      carrinho[2].clear()
      time.sleep(3)


def sairLoja():
  carregando()
  if len(carrinho[0]) == 0: #CARRINHO SEM ITEM - SAÍDA DIRETA
    print('VOLTE SEMPRE!')
    print('='*50)
    time.sleep(3)
    saindo()
  else:
    print('Tem certeza que deseja sair? Todo o conteúdo do seu carrinho será removido.\n\n[S] para sim\n[N] para não') #CONFIRMAÇÃO DA AÇÃO
    certeza = input('\nConfirme sua ação: ').upper()[0]
    print('='*50)
    time.sleep(1)
    while (certeza != 'S') and (certeza != 'N'):
      certeza = input('Dado inválido! Digite [S] para sim [N] para não:\n').upper()[0]
      print('='*50)
      time.sleep(3)
    if certeza == 'S': #LIMPEZA DO CARRINHO
      carrinho[0].clear()
      carrinho[1].clear()
      carrinho[2].clear()
      limpando()
      print('VOLTE SEMPRE!')
      print('='*50)
      time.sleep(3)
      saindo()
    else: #CASO DESISTA DA AÇÃO - CARRINHO MANTIDO
      print('Seus produtos foram mantidos no carrinho!')
      print('='*50)
      time.sleep(3)