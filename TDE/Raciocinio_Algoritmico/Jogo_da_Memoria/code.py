"""
GRUPO 25
- Daniela Lima
- Guilherme Henrique Peres
- Rafael Galo
- Izabelly Mucholowski
"""

from random import randint

from time import sleep

nivel_dificuldade = 0
contador_exibir_resposta = 2

user_in = user_in_temp = x = user_in_row = user_in_col = ''


# FUNÇÕES
# Selecionar/Controles
def opt_select(what: int):
    """
    :param what:
        0 - Selecionar dificuldade |
        1 - Selecionar posições das cartas |
        2 - Interação com o menu
    :return:
        user_in or user_in_row and user_in_col
    """
    global x

    def my_strip(self):  # gambiarra do .strip()  |  :p
        global user_in
        user_in = ''
        for i in self:
            if i != ' ':
                user_in += i
        return user_in

    def formatar_dificuldade():

        global user_in_row, user_in_col
        if nivel_dificuldade == 1:
            # row
            while True:
                user_in_row = str(input('Selecione uma linha: '))
                if len(user_in_row) == 1 and user_in_row in x and int(user_in_row) <= 4:
                    user_in_row = int(user_in_row) - 1
                    break

                print('--> Digite apenas um número entre 1 e 4!')

            # col
            while True:
                user_in_col = str(input('Selecione uma coluna: '))
                if len(user_in_col) == 1 and user_in_col in x and int(user_in_col) <= 4:
                    user_in_col = int(user_in_col) - 1
                    break

                print('--> Digite apenas um número entre 1 e 4!')

        if nivel_dificuldade == 2:
            # row
            while True:
                user_in_row = str(input('Selecione uma linha: '))
                if len(user_in_row) == 1 and user_in_row in x and int(user_in_row) <= 8:
                    user_in_row = int(user_in_row) - 1
                    break

                print('--> Digite apenas um número entre 1 e 8!')

            # col
            while True:
                user_in_col = str(input('Selecione uma coluna: '))
                if len(user_in_col) == 1 and user_in_col in x and int(user_in_col) <= 8:
                    user_in_col = int(user_in_col) - 1
                    break
                print('--> Digite apenas um número entre 1 e 8!')

        if nivel_dificuldade == 3:
            # row
            while True:
                user_in_row = str(input('Selecione uma linha: '))
                if 1 <= len(user_in_row) <= 2 and user_in_row in x and int(user_in_row) <= 10:
                    user_in_row = int(user_in_row) - 1
                    break

                print('--> Digite apenas um número entre 1 e 10')

            # col
            while True:
                user_in_col = str(input('Selecione uma coluna: '))
                if 1 <= len(user_in_col) <= 2 and user_in_col in x and int(user_in_col) <= 10:
                    user_in_col = int(user_in_col) - 1
                    break
                print('--> Digite apenas um número entre 1 e 10')

        return user_in_row, user_in_col

    if what == 0:  # Selecionar dificuldade
        x = '123'
        while True:
            print("""
+-------+-----------------+
| Opção |   Dificuldade   |
+-------+-----------------+
|     1 | Fácil (4x4)     |
|     2 | Médio (8x8)     |
|     3 | Difícil (10x10) |
+-------+-----------------+
""")
            user_in = str(input('Selecione uma opção: '))
            my_strip(user_in)

            if len(user_in) == 1 and user_in in x:
                user_in = int(user_in)
                break
            print('--> Digite apenas um número entre 1 e 3!')
        return user_in

    elif what == 1:  # Selecionar indices das 'cartas'
        if nivel_dificuldade == 1:
            x = '1234'
        elif nivel_dificuldade == 2:
            x = '12345678'
        elif nivel_dificuldade == 3:
            x = '1098765432'

        return formatar_dificuldade()

    elif what == 2:  # Seleção no menu
        x = '012'
        while True:
            print("""
+-------+---------------------------+
| Opção |           Menu            |
+-------+---------------------------+
|     0 | Desistir                  |
|     1 | Escolher carta            |
|     2 | Ajuda (mostar respostas   |
|       |        por 3 segundos).   |
+-------+---------------------------+
""")
            user_in = str(input('Selecione uma opção: '))
            my_strip(user_in)

            if len(user_in) == 1 and user_in in x:
                user_in = int(user_in)
                break
            print('--> Digite apenas um número entre 0 e 2!')
        return user_in


# Formatação Matriz
def formatar_mat(mat):
    print()
    for row in range(len(mat)):
        for col in range(len(mat)):
            print(f'[{mat[row][col]:^7}]', end='')
        print()


# Matrix secreta
def matrix_exibicao(mat):
    matrix_temp = []
    for row in range(len(mat)):
        matrix_temp.append([])
        for col in range((len(mat[row]))):
            matrix_temp[row].insert(col, '#')
    return matrix_temp


# Gerar Matrx
def gen_matrix(self=nivel_dificuldade):
    """Gera uma matriz baseada no nível de dificuldade"""

    matrix_values = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],  # 4X4
        ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF'],  # 8X8
        ['GG', 'HH', 'II', 'JJ', 'KK', 'LL', 'MM', 'NN',
         'OO', 'PP', 'QQ', 'RR', 'SS', 'TT', 'UU', 'VV',
         'WW', 'XX', 'YY', 'ZZ', 'AAA', 'BBB', 'CCC', 'DDD',
         'EEE', 'FFF', 'GGG', 'HHH', 'III', 'JJJ', 'KKK', 'LLL', ],  # 10X10
    ]

    matrix = []

    def verificar_repetencia(carta):
        contador_carta_repetida = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if carta == matrix[row][col]:
                    contador_carta_repetida += 1
        return contador_carta_repetida

    def escolhe_carta():
        matrix_temp = []
        if nivel_dificuldade == 1:
            carta = matrix_values[0][randint(0, len(matrix_values[0]) - 1)]
        elif nivel_dificuldade == 2:
            matrix_temp = matrix_values[0] + matrix_values[1]
            carta = matrix_temp[randint(0, len(matrix_temp) - 1)]
        else:
            matrix_temp = matrix_values[0] + matrix_values[1] + matrix_values[2]
            carta = matrix_temp[randint(0, len(matrix_temp) - 1)]
        return carta

    def gerador(lvl):
        for row in range(lvl):
            matrix.append([])
            for col in range(lvl):
                while True:
                    carta = escolhe_carta()
                    if verificar_repetencia(carta) < 2:
                        matrix[row].append(carta)
                        break

    if nivel_dificuldade == 1:
        lvl = 4
    elif nivel_dificuldade == 2:
        lvl = 8
    else:
        lvl = 10

    gerador(lvl)
    return matrix


# Selecionar carta
def escolher_carta(mat, exibir):
    formatar_mat(exibir)
    while True:
        carta_1_row, carta_1_col = opt_select(1)
        carta_2_row, carta_2_col = opt_select(1)
        if mat[carta_1_row][carta_1_col] in exibir_temp[carta_1_row][carta_1_col] or mat[carta_2_row][carta_2_col] in \
                exibir_temp[carta_2_row][carta_2_col]:
            print('Carta(s) já exibida(s)! Tente outra.')
        else:
            if carta_1_row != carta_2_row or carta_1_col != carta_2_col:
                break
            else:
                print("Você não pode selecionar a mesma carta!")

    if mat[carta_1_row][carta_1_col] == mat[carta_2_row][carta_2_col]:
        exibir_temp[carta_1_row][carta_1_col] = mat[carta_1_row][carta_1_col]
        exibir_temp[carta_2_row][carta_2_col] = mat[carta_2_row][carta_2_col]
        print()
        formatar_mat(exibir_temp)
    else:
        print("\nERROU")


nivel_dificuldade = opt_select(0)
mat = gen_matrix(nivel_dificuldade)
exibir = matrix_exibicao(mat)
exibir_temp = exibir
formatar_mat(exibir)

while True:
    print(f"\n[Ajuda = {contador_exibir_resposta} restantes]")
    menu = opt_select(2)
    if menu == 1:
#         print(mat)
        escolher_carta(mat, exibir_temp)

        if exibir_temp == mat:
            print("""

__   _____   ___ ___  __   _____ _  _  ___ ___ _   _ _ 
\ \ / / _ \ / __| __| \ \ / / __| \| |/ __| __| | | | |
 \ V / (_) | (__| _|   \ V /| _|| .` | (__| _|| |_| |_|
  \_/ \___/ \___|___|   \_/ |___|_|\_|\___|___|\___/(_)


                    RESPOSTA:
                """)
            formatar_mat(mat)
            break

    elif menu == 2:
        if contador_exibir_resposta > 0:
            print('\n' * 50)
            formatar_mat(mat)
            sleep(3)
            print('\n' * 50)
            contador_exibir_resposta -= 1
        else:
            print('Você não pode mais usar Ajuda!')

    elif menu == 0:
        print("""

__   _____   ___ ___   ___  ___ ___ ___ ___ _____ ___ _   _ _ 
\ \ / / _ \ / __| __| |   \| __/ __|_ _/ __|_   _|_ _| | | | |
 \ V / (_) | (__| _|  | |) | _|\__ \| |\__ \ | |  | || |_| |_|
  \_/ \___/ \___|___| |___/|___|___/___|___/ |_| |___|\___/(_)


            RESPOSTA:
        """)
        formatar_mat(mat)
        break
