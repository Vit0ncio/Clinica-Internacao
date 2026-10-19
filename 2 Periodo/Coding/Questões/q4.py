# =====================================================================
# CONFIGURAÇÃO INICIAL E CRIAÇÃO DE VARIÁVEIS
# Aqui criamos as variáveis que vão guardar as informações
# durante todo o funcionamento do jogo.
# =====================================================================

# Solicita os dados do administrador do jogo (quem vai esconder as bombas)
nome_administrador = input("Digite o nome do administrador: ")
senha_administrador = input("Digite a senha do administrador: ")

# Variável para contar quantas vezes o administrador tentou digitar a senha
cont_tentativas = 1

# Variáveis "bandeira" (Verdadeiro ou Falso) para controlar as repetições (loops)
loop_dificuldade = True
loop_bomba = True
loop_jogadas = True

# Variáveis que vão guardar as escolhas (palpites) de cada jogador durante a partida
palpite_jogador1 = 0
palpite_jogador2 = 0

# Variáveis que vão guardar onde as bombas estão escondidas (de 1 a 15)
posicao_bomba1 = 0
posicao_bomba2 = 0
posicao_bomba3 = 0
posicao_bomba4 = 0
posicao_bomba5 = 0

# Variáveis de contagem de bombas e palpites
qtd_bombas = 0
qtd_palpite_jogador1 = 0
qtd_palpite_jogador2 = 0

# Variáveis para saber se algum jogador "explodiu" (perdeu)
jogador1_morto = False
jogador2_morto = False

# Variáveis para controlar de quem é a vez de jogar
vez_jogador1 = False
vez_jogador2 = False

# Variável para somar todos os palpites no final
total_palpites = 0

bombas_cadastradas = 0

# =====================================================================
# ETAPA 1: AUTENTICAÇÃO DO ADMINISTRADOR
# =====================================================================

# Loop (repetição) que dá até 3 tentativas para o administrador confirmar a senha
while cont_tentativas <= 3:
    senha_confirmacao = input("Digite a senha do administrador novamente: ")

    # Se a senha digitada for diferente da senha original...
    if senha_confirmacao != senha_administrador:
        print("Senha errada, tente novamente!")
        cont_tentativas += 1 # Aumenta 1 na contagem de tentativas

        # Se chegar a 3 tentativas ou mais, bloqueia o acesso e o jogo não continua
        if cont_tentativas >= 3:
            print("Acesso bloqueado. Excesso de tentativas.")

    # Se a senha estiver correta...
    else:
        print("Senha correta.")
        break # O comando 'break' quebra (encerra) o loop, permitindo que o jogo continue


# =====================================================================
# ETAPA 2: CONFIGURAÇÃO DO JOGO (DIFICULDADE E BOMBAS)
# =====================================================================

# Loop onde o administrador escolhe a dificuldade e esconde as bombas
while loop_dificuldade:
    print("* 1 - Fácil (Digite a posição de 3 bombas)")
    print("* 2 - Difícil (Digite a posição de 5 bombas)")
    escolha_dificuldade = input("Digite a dificuldade: ")

    # --- CASO A ESCOLHA SEJA 1 (FÁCIL) ---
    if escolha_dificuldade == "1":
        qtd_bombas = 3
        print("Dificuldade fácil escolhida!")
        loop_dificuldade = False # Desliga o loop de dificuldade para iniciar o jogo

    # --- CASO A ESCOLHA SEJA 2 (DIFÍCIL) ---
    elif escolha_dificuldade == "2":
        qtd_bombas = 5
        print("Dificuldade difícil escolhida!")
        loop_dificuldade = False # Encerra a configuração

    # Caso digite algo diferente de 1 ou 2 na dificuldade
    else:
        print("Opção inválida, tente novamente.")
        continue # O 'continue' faz o loop voltar para o início imediatamente

# =====================================================================
# ESCONDENDO AS BOMBAS
# =====================================================================
# Ele vai rodar enquanto o número de bombas que já escondemos (bombas_cadastradas)
# for menor que o total de bombas que a dificuldade exige (qtd_bombas).
while bombas_cadastradas < qtd_bombas:

    # Pede a posição da bomba.
    # Usamos {bombas_cadastradas + 1} porque a contagem começa no zero,
    # mas queremos que apareça "Bomba 1", "Bomba 2", etc., para o usuário.
    entrada = input(f"Digite a posição da bomba {bombas_cadastradas + 1} (de 1 a 15): ")

    # O comando '.isdigit()' verifica se tem apenas números no que foi digitado.
    # O 'not' na frente inverte a lógica: "Se não for apenas número..."
    if not entrada.isdigit():
        print("Apenas números são válidos!")
        # O 'continue' ignora tudo o que está abaixo dele
        # e faz o loop voltar imediatamente para a primeira linha do 'while'.
        continue

    # Se o código não parou no 'continue' acima, sabemos que é um número válido.
    # Então, convertemos o texto (string) para número matemático (int).
    posicao = int(entrada)

    # Verifica se o número escolhido está fora dos limites do jogo (1 a 15)
    if posicao < 1 or posicao > 15:
        print("Posição inválida! Digite novamente.")
        continue # Volta para o início do loop para pedir a mesma bomba de novo

    # Agora guardamos a posição na variável correta.
    # O valor de 'bombas_cadastradas' nos diz exatamente em qual bomba estamos.
    if bombas_cadastradas == 0:
        posicao_bomba1 = posicao
    elif bombas_cadastradas == 1:
        posicao_bomba2 = posicao
    elif bombas_cadastradas == 2:
        posicao_bomba3 = posicao
    elif bombas_cadastradas == 3:
        posicao_bomba4 = posicao
    elif bombas_cadastradas == 4:
        posicao_bomba5 = posicao

    # Confirma para o administrador que deu certo
    print(f"Bomba {bombas_cadastradas + 1} escondida na posição {posicao}.")

    # Adiciona 1 ao contador de bombas cadastradas.
    bombas_cadastradas += 1

# 'Limpa' a tela imprimindo 50 linhas em branco (assim os jogadores não veem onde estão as bombas)
print("\n" * 50)


# =====================================================================
# ETAPA 3: O JOGO COMEÇA
# =====================================================================

# Cadastra o nome dos jogadores
nome_jogador1 = input("Digite o nome do jogador 1: ")
nome_jogador2 = input("Digite o nome do jogador 2: ")

# Loop principal da partida (onde as jogadas acontecem)
while loop_jogadas:

    # --- TURNO DO JOGADOR 1 ---
    vez_jogador1 = True
    while vez_jogador1:
        escolha_jogador1 = input(f"{nome_jogador1}, faça seu palpite: ")

        # Verifica se ele digitou um número válido
        if escolha_jogador1.isdigit():
            escolha_jogador1 = int(escolha_jogador1)

            # CONDIÇÃO 1: Acertou uma bomba exatamente (morreu)
            if escolha_jogador1 == posicao_bomba1 or escolha_jogador1 == posicao_bomba2 or escolha_jogador1 == posicao_bomba3 or escolha_jogador1 == posicao_bomba4 or escolha_jogador1 == posicao_bomba5:
                print(f"Você explodiu! A bomba estava no campo {escolha_jogador1}. {nome_jogador2} é o vencedor!")
                jogador1_morto = True # Marca que ele perdeu
                loop_jogadas = False # Encerra a partida

            # CONDIÇÃO 2: Chegou perto (uma casa antes [-1] ou uma depois [+1] de qualquer bomba)
            elif escolha_jogador1 == posicao_bomba1 - 1 or escolha_jogador1 == posicao_bomba2 - 1 or escolha_jogador1 == posicao_bomba3 - 1 or escolha_jogador1 == posicao_bomba4 - 1 or escolha_jogador1 == posicao_bomba5 - 1 or escolha_jogador1 == posicao_bomba1 + 1 or escolha_jogador1 == posicao_bomba2 + 1 or escolha_jogador1 == posicao_bomba3 + 1 or escolha_jogador1 == posicao_bomba4 + 1 or escolha_jogador1 == posicao_bomba5 + 1:
                print("Opa! Você está muito perto de uma bomba! Fique atento.")
                qtd_palpite_jogador1 += 1 # Conta a jogada válida

            # CONDIÇÃO 3: Está seguro
            else:
                print(f"Bomba não encontrada no campo {escolha_jogador1}.")
                qtd_palpite_jogador1 += 1 # Conta a jogada válida

            # Se sobreviveu por 3 turnos, ele ganha
            if qtd_palpite_jogador1 == 3:
                print(f"Jogador {nome_jogador1} vence a partida!")
                loop_jogadas = False # Encerra a partida

            vez_jogador1 = False # Passa a vez para o jogador 2

        else:
            print("Digite apenas números!")

    # Se a partida acabou no turno do jogador 1, quebra o loop para não deixar o jogador 2 jogar
    if not loop_jogadas:
        break

    # --- TURNO DO JOGADOR 2 ---
    vez_jogador2 = True
    while vez_jogador2:
        escolha_jogador2 = input(f"{nome_jogador2}, faça seu palpite: ")

        # As regras são idênticas as do jogador 1
        if escolha_jogador2.isdigit():
            escolha_jogador2 = int(escolha_jogador2)

            # Verifica se pisou na bomba
            if escolha_jogador2 == posicao_bomba1 or escolha_jogador2 == posicao_bomba2 or escolha_jogador2 == posicao_bomba3 or escolha_jogador2 == posicao_bomba4 or escolha_jogador2 == posicao_bomba5:
                print(f"Você explodiu! A bomba estava no campo {escolha_jogador2}. {nome_jogador1} é o vencedor!")
                jogador2_morto = True
                loop_jogadas = False

            # Verifica se passou perto da bomba
            elif escolha_jogador2 == posicao_bomba1 - 1 or escolha_jogador2 == posicao_bomba2 - 1 or escolha_jogador2 == posicao_bomba3 - 1 or escolha_jogador2 == posicao_bomba4 - 1 or escolha_jogador2 == posicao_bomba5 - 1 or escolha_jogador2 == posicao_bomba1 + 1 or escolha_jogador2 == posicao_bomba2 + 1 or escolha_jogador2 == posicao_bomba3 + 1 or escolha_jogador2 == posicao_bomba4 + 1 or escolha_jogador2 == posicao_bomba5 + 1:
                print("Opa! Você está muito perto de uma bomba! Fique atento.")
                qtd_palpite_jogador2 += 1

            # Se for um lugar seguro
            else:
                print(f"Bomba não encontrada no campo {escolha_jogador2}.")
                qtd_palpite_jogador2 += 1

            # Se sobreviveu a 3 turnos, ele ganha
            if qtd_palpite_jogador2 == 3:
                print(f"Jogador {nome_jogador2} vence a partida!")
                loop_jogadas = False

            vez_jogador2 = False # Termina a vez do jogador 2

        else:
            print("Digite apenas números!")


# =====================================================================
# ETAPA 4: RESULTADO FINAL E ESTATÍSTICAS
# =====================================================================

# Com a partida encerrada, o código verifica quem morreu ou sobreviveu e exibe o placar final
if jogador1_morto:
    print(f"{nome_jogador1}: Perdeu! Pisou em uma bomba.")
    print(f"{nome_jogador2}: Ganhou! {nome_jogador1} pisou em uma bomba.")
elif jogador2_morto:
    print(f"{nome_jogador1}: Ganhou! {nome_jogador2} pisou em uma bomba.")
    print(f"{nome_jogador2}: Perdeu! Pisou em uma bomba..")
elif qtd_palpite_jogador1 == 3:
    print(f"{nome_jogador1}: Ganhou! Fez 3 palpites e não acertou nenhuma bomba.")
    print(f"{nome_jogador2}: Perdeu! {nome_jogador1} Acertou todos os palpites.")
elif qtd_palpite_jogador2 == 3:
    print(f"{nome_jogador1}: Perdeu! {nome_jogador2} Acertou todos os palpites.")
    print(f"{nome_jogador2}: Ganhou! Fez 3 palpites e não acertou nenhuma bomba.")

# Calcula o total de jogadas somando os palpites válidos dos dois jogadores
total_palpites = qtd_palpite_jogador1 + qtd_palpite_jogador2

# Mostra o total de palpites no final do jogo
print(f"Palpites totais: {total_palpites}")
