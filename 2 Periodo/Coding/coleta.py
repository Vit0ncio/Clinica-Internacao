# i. Orientar o usuário sobre a categoria correta de cada material e seu destino adequado,
# ii. Identificar diferentes tipos de resíduos descartados, como papel, plástico, vidro, metal e materiais orgânicos,
# iii. Registrar e contabilizar os materiais separados, possibilitando acompanhar a quantidade de resíduos destinados à coleta seletiva.


qtd_azul = 0
qtd_vermelho = 0
qtd_verde = 0
qtd_amarelo = 0
qtd_cinza = 0
qtd_marrom = 0
qtd_residuo = 0

loop1 = True
loop2 = True
#Ao utilizarmos o loop 1 e 2 como variável verdadeira, conseguimos ter controle sobre ele até o momento dele se tornar falso,
#quando o usuário digitar 0, dessa forma quebramos os while's.

print("Seja bem-vindo(a) ao Sistema de Coleta Seletiva!")
while loop1:
    print("Você deseja saber sobre a localização dos pontos de coleta?")
    print("1 - Sim")
    print("2 - Não")
    print("0 - Sair")
    escolha = ""
    escolha = input()
    #Para evitar que o usuário digite algo que vá gerar um erro,
    #optamos por inputar uma string, pois é melhor de ser feito o tratamento de erro.

    if escolha == "1":
        print("Pontos de Coleta Seletiva em Recife:")
        print("* Boa Viagem")
        print("* Ibura")
        print("* Imbiribeira")
        print("* Conde da Boa Vista")
        print("* Pina")
        print("--------------------------------------")
        print("Você deseja saber orientações a respeito do descarte do seu lixo?")
        print("1 - Sim")
        print("2 - Não")
        escolha = ""
        escolha = input()

        if escolha == "1":
            print("A coleta seletiva é o processo de separação e recolhimento dos resíduos descartados, ")
            print("classificados conforme sua origem e composição (como materiais recicláveis e lixo orgânico).")
            print("Cada cor que a lixeira contém representa o tipo de lixo adequado para o descarte, conforme os exemplos abaixo: ")
            print("Azul -> Para papel e papelão (jornais, revistas, caixas)")
            print("Vermelho -> Para plástico (garrafas PET, embalagens, sacolas)")
            print("Verde -> Para vidro (garrafas, potes, copos)")
            print("Amarelo -> Para metal (latas de alumínio e de aço)")
            print("Marrom -> Para materiais orgânicos (restos de comida, cascas de frutas)")
            print("Cinza -> Para materiais não recicláveis")
            print("--------------------------------------")
            print("Você deseja informar os tipos de resíduos que irá descartar?")
            print("1 - Sim")
            print("2 - Não")
            escolha = ""
            escolha = input()

            if escolha == "1":
                while loop2:
                    print("Quais os tipos de resíduos que você irá descartar?")
                    print("1 - Azul (Papel)")
                    print("2 - Vermelho (Plástico)")
                    print("3 - Verde (Vidro)")
                    print("4 - Amarelo (Metal)")
                    print("5 - Marrom (Orgânico)")
                    print("6 - Cinza (Não Reciclável)")
                    print("0 - Parar")
                    escolha = ""
                    escolha = input()

                    if escolha == "1":
                        qtd_azul += 1
                        qtd_residuo += 1
                    elif escolha == "2":
                        qtd_vermelho += 1
                        qtd_residuo += 1
                    elif escolha == "3":
                        qtd_verde+= 1
                        qtd_residuo += 1
                    elif escolha == "4":
                        qtd_amarelo += 1
                        qtd_residuo += 1
                    elif escolha == "5":
                        qtd_marrom += 1
                        qtd_residuo += 1
                    elif escolha == "6":
                        qtd_cinza += 1
                        qtd_residuo += 1
                    elif escolha == "0":
                        print(f"Quantidade de resíduos: {qtd_residuo}")
                        print(f"Quantidade de resíduos para a coleta azul: {qtd_azul}")
                        print(f"Quantidade de resíduos para a coleta vermelha: {qtd_vermelho}")
                        print(f"Quantidade de resíduos para a coleta verde: {qtd_verde}")
                        print(f"Quantidade de resíduos para a coleta amarelo: {qtd_amarelo}")
                        print(f"Quantidade de resíduos para a coleta marrom: {qtd_marrom}")
                        print(f"Quantidade de resíduos para a coleta cinza: {qtd_cinza}")
                        print("Saindo... \nObrigado por utilizar o sistema!")
                        loop1 = False
                        loop2 = False
                    else:
                        print("Entrada inválida! Digite novamente.")
            elif escolha == "2":
                print("Saindo... \nObrigado por utilizar o sistema!")
                loop1 = False
                loop2 = False


            else:
                print("Entrada inválida! Digite novamente.")
        elif escolha == "2":
            print("Você deseja informar os tipos de resíduos que irá descartar?")
            print("1 - Sim")
            print("2 - Não")
            escolha = ""
            escolha = input()

            if escolha == "1":
                while loop2:
                    print("Quais os tipos de resíduos que você irá descartar?")
                    print("1 - Azul (Papel)")
                    print("2 - Vermelho (Plástico)")
                    print("3 - Verde (Vidro)")
                    print("4 - Amarelo (Metal)")
                    print("5 - Marrom (Orgânico)")
                    print("6 - Cinza (Não Reciclável)")
                    print("0 - Parar")
                    escolha = ""
                    escolha = input()

                    if escolha == "1":
                        qtd_azul += 1
                        qtd_residuo += 1
                    elif escolha == "2":
                        qtd_vermelho += 1
                        qtd_residuo += 1
                    elif escolha == "3":
                        qtd_verde+= 1
                        qtd_residuo += 1
                    elif escolha == "4":
                        qtd_amarelo += 1
                        qtd_residuo += 1
                    elif escolha == "5":
                        qtd_marrom += 1
                        qtd_residuo += 1
                    elif escolha == "6":
                        qtd_cinza += 1
                        qtd_residuo += 1
                    elif escolha == "0":
                        print(f"Quantidade de resíduos: {qtd_residuo}")
                        print(f"Quantidade de resíduos para a coleta azul: {qtd_azul}")
                        print(f"Quantidade de resíduos para a coleta vermelha: {qtd_vermelho}")
                        print(f"Quantidade de resíduos para a coleta verde: {qtd_verde}")
                        print(f"Quantidade de resíduos para a coleta amarelo: {qtd_amarelo}")
                        print(f"Quantidade de resíduos para a coleta marrom: {qtd_marrom}")
                        print(f"Quantidade de resíduos para a coleta cinza: {qtd_cinza}")
                        print("Saindo... \nObrigado por utilizar o sistema!")
                        loop1 = False
                        loop2 = False
                    else:
                        print("Entrada inválida! Digite novamente.")

            elif escolha == "2":
                print("Saindo... \nObrigado por utilizar o sistema!")
                loop1 = False
                loop2 = False
            else:
                print("Entrada inválida! Digite novamente.")
        else:
            print("Entrada inválida! Digite novamente.")

    elif escolha == "2":
        print("Você deseja saber orientações a respeito do descarte do seu lixo?")
        print("1 - Sim")
        print("2 - Não")
        escolha = ""
        escolha = input()


        if escolha == "1":
            print("A coleta seletiva é o processo de separação e recolhimento dos resíduos descartados, classificados conforme sua origem e composição (como materiais recicláveis e lixo orgânico).")
            print("Cada cor que a lixeira contém representa o tipo de lixo adequado para o descarte, conforme os exemplos abaixo: ")
            print("Azul -> Para papel e papelão (jornais, revistas, caixas)")
            print("Vermelho -> Para plástico (garrafas PET, embalagens, sacolas)")
            print("Verde -> Para vidro (garrafas, potes, copos)")
            print("Amarelo -> Para metal (latas de alumínio e de aço)")
            print("Marrom -> Para materiais orgânicos (restos de comida, cascas de frutas)")
            print("Cinza -> Para materiais não recicláveis")
            print("Você deseja informar os tipos de resíduos que irá descartar?")
            print("1 - Sim")
            print("2 - Não")
            escolha = ""
            escolha = input()

            if escolha == "1":
                while loop2:
                    print("Quais os tipos de resíduos que você irá descartar?")
                    print("1 - Azul (Papel)")
                    print("2 - Vermelho (Plástico)")
                    print("3 - Verde (Vidro)")
                    print("4 - Amarelo (Metal)")
                    print("5 - Marrom (Orgânico)")
                    print("6 - Cinza (Não Reciclável)")
                    print("0 - Parar")
                    escolha = ""
                    escolha = input()

                    if escolha == "1":
                        qtd_azul += 1
                        qtd_residuo += 1
                    elif escolha == "2":
                        qtd_vermelho += 1
                        qtd_residuo += 1
                    elif escolha == "3":
                        qtd_verde+= 1
                        qtd_residuo += 1
                    elif escolha == "4":
                        qtd_amarelo += 1
                        qtd_residuo += 1
                    elif escolha == "5":
                        qtd_marrom += 1
                        qtd_residuo += 1
                    elif escolha == "6":
                        qtd_cinza += 1
                        qtd_residuo += 1
                    elif escolha == "0":
                                    print(f"Quantidade de resíduos: {qtd_residuo}")
                                    print(f"Quantidade de resíduos para a coleta azul: {qtd_azul}")
                                    print(f"Quantidade de resíduos para a coleta vermelha: {qtd_vermelho}")
                                    print(f"Quantidade de resíduos para a coleta verde: {qtd_verde}")
                                    print(f"Quantidade de resíduos para a coleta amarelo: {qtd_amarelo}")
                                    print(f"Quantidade de resíduos para a coleta marrom: {qtd_marrom}")
                                    print(f"Quantidade de resíduos para a coleta cinza: {qtd_cinza}")
                                    print("Saindo... \nObrigado por utilizar o sistema!")
                                    loop1 = False
                                    loop2 = False
                    else:
                        print("Entrada inválida! Digite novamente.")
            elif escolha == "2":
                print("Saindo... \nObrigado por utilizar o sistema!")
                loop1 = False
                loop2 = False
            else:
                print("Entrada inválida! Digite novamente.")
        elif escolha == "2":
            print("Você deseja informar os tipos de resíduos que irá descartar?")
            print("1 - Sim")
            print("2 - Não")
            eecolha = ""
            escolha = input()

            if escolha == "1":
                while loop2:
                    print("Quais os tipos de resíduos que você irá descartar?")
                    print("1 - Azul (Papel)")
                    print("2 - Vermelho (Plástico)")
                    print("3 - Verde (Vidro)")
                    print("4 - Amarelo (Metal)")
                    print("5 - Marrom (Orgânico)")
                    print("6 - Cinza (Não Reciclável)")
                    print("0 - Parar")
                    escolha = ""
                    escolha = input()

                    if escolha == "1":
                        qtd_azul += 1
                        qtd_residuo += 1
                    elif escolha == "2":
                        qtd_vermelho += 1
                        qtd_residuo += 1
                    elif escolha == "3":
                        qtd_verde+= 1
                        qtd_residuo += 1
                    elif escolha == "4":
                        qtd_amarelo += 1
                        qtd_residuo += 1
                    elif escolha == "5":
                        qtd_marrom += 1
                        qtd_residuo += 1
                    elif escolha == "6":
                        qtd_cinza += 1
                        qtd_residuo += 1
                    elif escolha == "0":
                        print(f"Quantidade de resíduos: {qtd_residuo}")
                        print(f"Quantidade de resíduos para a coleta azul: {qtd_azul}")
                        print(f"Quantidade de resíduos para a coleta vermelha: {qtd_vermelho}")
                        print(f"Quantidade de resíduos para a coleta verde: {qtd_verde}")
                        print(f"Quantidade de resíduos para a coleta amarelo: {qtd_amarelo}")
                        print(f"Quantidade de resíduos para a coleta marrom: {qtd_marrom}")
                        print(f"Quantidade de resíduos para a coleta cinza: {qtd_cinza}")
                        print("Saindo... \nObrigado por utilizar o sistema!")
                        loop1 = False
                        loop2 = False
                    else:
                        print("Entrada inválida! Digite novamente.")
            elif escolha == "2":
                print("Saindo... \nObrigado por utilizar o sistema!")
                loop1 = False
                loop2 = False

        else:
            print("Entrada inválida! Digite novamente.")

    elif escolha == "0":
        print("Saindo... \nObrigado por utilizar o sistema!")
        loop1 = False


    else:
        print("Entrada inválida! Digite novamente.")
