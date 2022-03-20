while True:
    palavra_secreta = str(input("Digite a palavra: "))
    palavra_completa = acertou = False
    lista_letras = [ ]
    letras_certas = [ ]
    lista_palavra_secreta = [ ]

    for caractere in palavra_secreta:
        if caractere not in lista_palavra_secreta and caractere != " ":
            lista_palavra_secreta.append(caractere)

    while True:
        max_tentativa = input("Digite o número máximo de tentativas: ")
        if not max_tentativa.isdigit():
            print("Digite apenas números inteiros e maiores que zero!")
        elif int(max_tentativa) <= 0:
            print("O número de tentativas precisa ser superior a zero!")
        else:
            max_tentativa = int(max_tentativa)
            break

    print(100 * "\n")

    while True:
        while True:
            temp_palavra_secreta = [ ]
            escolha = input("[O] Digitar uma letra | [X] Sugerir uma palavra: ")
            if not escolha.isalpha() or escolha not in "xXoO" or len(escolha.strip()) > 1:
                print("Digite apenas X ou O!")
            else:
                escolha.lower()
                break

        if escolha == "o":
            while True:
                usuario_in = str(input(f"Digite uma letra: "))
                if not usuario_in.isalpha() or len(usuario_in.strip()) > 1:
                    print("Digite apenas uma letra!")
                if usuario_in in lista_letras:
                    print("Esta letra ja foi escolhida! Escolha outra.")
                else:
                    break

            if not usuario_in in lista_letras:
                lista_letras.append(usuario_in)
            if usuario_in in lista_palavra_secreta and usuario_in not in letras_certas:
                letras_certas.append(usuario_in)
            else:
                max_tentativa -= 1
                print(f"Você ERROU! A palavra não possui a letra {usuario_in.upper()}.")

            for letra in palavra_secreta:
                if not letra in letras_certas and not letra.isspace():
                    letra = "*"
                temp_palavra_secreta.append(letra)

            if len(lista_palavra_secreta) == len(letras_certas):
                print(palavra_completa)
                print(lista_palavra_secreta)
                palavra_completa = True
            else:
                print(f"\nLetras escolhidas: {lista_letras}.\nRestam {max_tentativa} tentativas")
                for i in temp_palavra_secreta:
                    print(i.upper(), end="")
                print()

        if escolha == "x":
            while True:
                usuario_in = str(input(f"Digite uma palavra: "))
                if usuario_in in "1234567890!@#$%&*()`{´[}]:;.,<>^~\"\'\\|":
                    print("Digite apenas palavras!")
                else:
                    break

            if usuario_in.lower().split() == palavra_secreta.lower().split():
                print(usuario_in.lower().split())
                print(palavra_secreta.lower().split())
                acertou = True
            else:
                max_tentativa -= 1
                print(f"Você ERROU! Restam {max_tentativa} tentativas.\nLetras escolhidas: {lista_letras}.")
                for i in temp_palavra_secreta:
                    print(i.upper(), end="")
                print()

        if max_tentativa == 0:
            print("Que pena, você perdeu.")
            break
        elif palavra_completa or acertou:
            print("Parabéns, você acertou!")
            break

    while True:
        repetir = str(input("Jogar novamente?\n[O] Sim | [X] Sair: "))
        if not repetir.isalpha() or repetir not in "xXoO" or len(repetir.strip()) > 1:
            print("Digite apenas X ou O!")
        else:
            break
    if repetir == "x":
        break
