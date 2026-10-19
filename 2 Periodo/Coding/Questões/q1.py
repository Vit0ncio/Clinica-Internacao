while True:
    #Perguntamos o nome da turma ou se deseja sair
    turma = input("Digite o nome da turma ou 'sair' para encerrar ")

    #Condição de parada: se o usuário digita "sair", para o laço
    #O lower garante que funcione se o usuário digitar "SAIR" ou "Sair"
    if turma.lower() == "sair":
        print("Encerrando o sistema...")
        break # O break interrompe a repetição do while

    # Perguntamos o nome da disciplina
    disciplina = input("Digite o nome da disciplina: ")

    #Perguntamos a quantidade de alunos
    qtd_alunos = input("Digite a quantidade de alunos: ")
    soma_notas = 0 #Acumulador para somar as notas
    contador = 1 #Contador para controlar qual aluno está sendo lido

    if qtd_alunos.isdigit():
        qtd_alunos = int(qtd_alunos)
        # Por uma condicional, para que a quantidade de alunos seja maior que 0
        if qtd_alunos < 1 :
            print("A quantidade de alunos deve ser maior que 0. Tente novamente.")
            continue # Volta para o início do while
        while contador <= qtd_alunos:
            nota = float(input(f"Digite a nota do aluno {contador} (0 a 10): "))

        #Validação: Enquanto a nota for menor que 0 e maior que 10, pedimos novamente
            while nota < 0 or nota > 10:
                print("Nota inválida! A nota deve ser entre 0 e 10")
                nota = float(input(f"Digite novamente a nota do aluno {contador} (0 a 10) "))

        #Acumulamos a nota válida e passamos para o próximo aluno
            soma_notas = soma_notas + nota
            contador = contador + 1

    #Cálculo da média geral e classificação
        media = soma_notas / qtd_alunos

        if media >= 7:
            situacao = "Bem avaliada"
        elif media >= 5 and media < 7 :
            situacao = "Em situação de alerta"
        else:
            situacao = "Precisa de intervenção"

    #Relatório final
        print("\n RELATÓRIO DA TURMA: ")
        print(f"Nome da turma: {turma}")
        print(f"Disciplina: {disciplina}")
        print(f"Quantidade de alunos: {qtd_alunos}")
        print(f"Média geral da turma: {media:.2f}")
        print(f"Situação da turma: {situacao}")

    else:
        print("Digite um número!")
