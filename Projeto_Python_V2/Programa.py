import Funcoes_Listas as funlis

while True:
    acessar_finalizar = funlis.inicio()
    funlis.carregando()
    if acessar_finalizar == "A":
        funlis.boas_vindas()
        while True:
            escolha_opcao = funlis.menu_principal()
            if escolha_opcao == 1:
                while True:
                    funlis.adcProd()
                    break
            elif escolha_opcao == 2:
                while True:
                    funlis.adcServ()
                    break
            elif escolha_opcao == 3:
                while True:
                    funlis.rmvProduto()
                    break
            elif escolha_opcao == 4:
                while True:
                    funlis.limparcar()
                    break
            elif escolha_opcao == 5:
                while True:
                    funlis.extrato()
                    break
            elif escolha_opcao == 6:
                while True:
                    funlis.pagamento()
                    break
            else:
                funlis.sairLoja()
                break
    else:
        funlis.imprimir_historico()
        break


