"""
Grupo:
- Daniela dos Santos Lima
- Pedro Lucas Ghezzi Bittencourt
- Isabela Navarro Benedetti
- Larissa Raimee Gomes
- João Vitor Zambão
"""

# DOCUMENTAÇÃO PYTHON (https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods)
# fala sobre .split() .lower() .isdigit() .isalpha() etc.

while True:
    palavra_secreta = str(input("Digite a palavra: "))
    palavra_completa = acertou = False  # Deixa-se falso para que o programa não conte como acerto (Linha 68, 88 e 113)
    lista_letras = [ ]  # Lista das letras escolhidas
    letras_certas = [ ]  # Lista das letras certas
    lista_palavra_secreta = [ ]  # Lista em que a palavra secreta será separada (letra por letra sem se repetir)

    # Isso pega a palavra secreta e a separa por caractere
    for caractere in palavra_secreta:  #
        if caractere not in lista_palavra_secreta and caractere != " ":  # Isso verifica se a letra não está repetida E se não é um espaço
            lista_palavra_secreta.append(caractere)

    while True:  # Verifica se o input será um número inteiro E maior que zero
        max_tentativa = input("Digite o número máximo de tentativas: ")
        if not max_tentativa.isdigit():  # Se a quantidade de tentativa é um digito
            print("Digite apenas números inteiros e maiores que zero!")
        elif int(max_tentativa) <= 0:  # Se é maior que zero
            print("O número de tentativas precisa ser superior a zero!")
        else:
            max_tentativa = int(max_tentativa)  # Transforma o input pra inteiro (não usei int(input())
            break  # porque senão, caso o usuário digitasse uma letra, o programa iria crashar
            # e não seria possível fazer essa verificação)

    print(100 * "\n")  # Dá um monte de espaço em branco para que a palavra secreta não apareça na tela

    while True:
        while True:  # Verifica se o que está sendo digitado é apenas X OU O
            temp_palavra_secreta = [ ]  # Lista temporária em que a palavra secreta ficará resetando conforme o usuário acerta a letra
            escolha = input("[O] Digitar uma letra | [X] Sugerir uma palavra: ")
            if not escolha.isalpha() or escolha not in "xXoO" or len(escolha.strip()) > 1:
                print("Digite apenas X ou O!")
            else:
                escolha.lower()
                break

        if escolha == "o":  # Digitar uma letra
            while True:  # Verifica se o usuário está digitando uma letra e não outra coisa
                usuario_in = str(input(f"Digite uma letra: "))
                if not usuario_in.isalpha() or len(usuario_in.strip()) > 1:
                    print("Digite apenas uma letra!")
                if usuario_in in lista_letras:
                    print("Esta letra ja foi escolhida! Escolha outra.")
                else:
                    break

            if not usuario_in in lista_letras:  # Se a letra não foi citada, então ela entra na lista das letras escolhidas
                lista_letras.append(usuario_in)
            # Se a letra escolhida pelo usuário estiver certa E não estiver na lista das letras certas, então ela entra nessa lista
            if usuario_in in lista_palavra_secreta and usuario_in not in letras_certas:
                letras_certas.append(usuario_in)
            else:  # Se o usuário errou, desconta uma tentativa
                max_tentativa -= 1
                print(f"Você ERROU! A palavra não possui a letra {usuario_in.upper()}.")

            # Exibe a palavra secreta
            for letra in palavra_secreta:
                if not letra in letras_certas and not letra.isspace():  # Se cada letra da palavra secreta não estiver na
                    letra = "*"  # lista das acertadas (não foi acertada)
                temp_palavra_secreta.append(letra)  # E se ela não é espaço, então ela aparecerá como *

            # Se a quantidade de letras certas já ditas for igual a da palavra secreta, então a palavra vai estar completa.
            if len(lista_palavra_secreta) == len(letras_certas):
                print(palavra_completa)
                print(lista_palavra_secreta)
                palavra_completa = True  # Valida que a palavra foi completada, logo, o usuário ganhou (Pula pra Linha 113)
            else:  # Então, se a palavra ainda não estiver conpleta, continua...
                print(f"\nLetras escolhidas: {lista_letras}.\nRestam {max_tentativa} tentativas")
                for i in temp_palavra_secreta:  # Exibe a palavra secreta temporária (BO* DIA)
                    print(i.upper(), end="")
                print()

        if escolha == "x":  # Digitar uma palavra
            while True:  # Verifica que seja apenas palavras
                usuario_in = str(input(f"Digite uma palavra: "))
                if usuario_in in "1234567890!@#$%&*()`{´[}]:;.,<>^~\"\'\\|":  # Seria mais fácil usar RegEx (expressões regulares)
                    print("Digite apenas palavras!")  # para filtrar mas a gente ainda não aprendeu isso e também
                else:  # não é permitido usar
                    break

            if usuario_in.lower().split() == palavra_secreta.lower().split():  # Se a palavra dita pelo usuário for igual a palavra secreta
                print(usuario_in.lower().split())  # então, ele acertou (Pula pra Linha 113)
                print(palavra_secreta.lower().split())
                acertou = True
            else:  # Se ele errou a palavra
                max_tentativa -= 1
                print(f"Você ERROU! Restam {max_tentativa} tentativas.\nLetras escolhidas: {lista_letras}.")
                for i in temp_palavra_secreta:
                    print(i.upper(), end="")
                print()

        # Monitorar comportamento | (selec. tudo, Ctrl + / para descomentar)

        #         print(f"""
        # ----------------------------------------------------
        # Letras Escolhidas: {lista_letras}
        # Letras Certas: {letras_certas}
        # Lista Palavra Secreta: {lista_palavra_secreta}
        # Temp: {temp_palavra_secreta}
        # ----------------------------------------------------""")

        if max_tentativa == 0:  # Verifica se as tentativas acabaram
            print("Que pena, você perdeu.")
            break
        elif palavra_completa or acertou:  # Verifica se o usuario completou ou acertou a palavra
            print("Parabéns, você acertou!")
            break

    while True:  # Jogar novamente | Verifica se o que está sendo digitado é apenas X OU O
        repetir = str(input("Jogar novamente?\n[O] Sim | [X] Sair: "))
        if not repetir.isalpha() or repetir not in "xXoO" or len(repetir.strip()) > 1:
            print("Digite apenas X ou O!")
        else:
            break
    if repetir == "x":
        break
