"""
GRUPO:
- Camily Albres
- Daniela Lima
- Eduardo Lago
- Mateus Marcimiano

REQUISITOS:
- pygame | pip install pygame
- tabulate | pip install tabulate

!!!!!!!!!!!!!!!     Para tirar a animação de digitação
!!    OBS    !!     comente a linha 164 ou "sleep(choice(txt_fx_vel))"
!!!!!!!!!!!!!!!


{ ( p ∧ q ) , ( r ∨ s ) , ( x ∧ w ) , ( p → ¬s ) } ⊨  r
{ (( p ∨ q ) → r ) ,  ( s → p ) , ( t → q ) , v , ( s ∨ t ) } ⊨ r
"""

from random import choice
from time import sleep

from pygame import mixer
from tabulate import tabulate

# PYGAME MIXER
# Sfx
mixer.init()
mixer.music.load("sfx_enter.mp3")
mixer.music.load("sfx_soundtrack_menu.mp3")
mixer.music.load("sfx_typing.mp3")
sfx_enter = mixer.Sound("sfx_enter.mp3")
sfx_menu = mixer.Sound("sfx_soundtrack_menu.mp3")
sfx_typing = mixer.Sound("sfx_typing.mp3")
# Background Music
mixer.music.load("sfx_soundtrack_main.mp3")

# VARIÁVEIS GLOBAIS
contador_mordomo = 0
contador_jardineiro = 0
contador_faxineira = 0
txt_fx_vel = [0.02, 0.05, 0.08]

# ARRAYS
pistas = [
    ["o jardineiro estava podando o jardim sozinho"],
    ["a faxineira estava limpando a varanda sozinha"],
    ["a faxineira avistou o jardineiro com uma tesoura de poda no jardim"],
    ["o jardineiro viu a faxineira limpando vidro quebrado na varanda"],
    ["o mordomo foi ao mercado"],
    ["o mordomo acusa a faxineira de ter assassinado a Sra. Brown"],
    ["a faxineira diz que o mordomo nao saiu de casa"],
    ["o jardineiro diz que o mordomo nao saiu de casa"],
]

pistas_tab = [
    ["PISTAS"],
]

acoes = [
    ["Opções", "Ação"],
    ["1", "Interrogar"],
    ["2", "Acusar"],
    ["3", "Consultar pistas"],
]

suspeitos = [
    ["Opções", "Suspeitos"],
    ["1", "Faxineira"],
    ["2", "Jardineiro"],
    ["3", "Mordomo"],
]

# TEXTOS
main_txt_01 = """- Na tarde de uma quinta-feira, a polícia civil da região metropolitana
de Curitiba, foi chamada para investigar um caso de assassinato
ocorrido há poucos minutos, na casa de uma senhora muito influente
na cidade.

- Ao chegar na residência da Sra. Brown, o mordomo os recepcionou e disse foi ele 
quem ligou para a polícia.

- Disse também que na casa estavam presentes o jardineiro e a faxineira
durante o ocorrido.

- Os policiais, então, partiram para interrogar um por um, no local do crime.

A partir de agora, cabe a você descobrir quem é o assassino.
"""

txt_vazio_01 = "Não tenho nada a declarar no momento.\n"
txt_vazio_02 = "Não tenho mais nada a declarar.\n"

# Faxineira
txt_f00 = """- Você vai até a faxineira, na varanda, e pergunta onde ela estava no momento do ocorrido.

- Ela responde que estava limpando alguns cacos de vidro de um copo que havia sido
derrubado pela Sra. Brown, momentos antes do assassinato.

[Nova pista obtida! - a faxineira estava limpando a varanda sozinha.]
"""

txt_f01 = """- Você volta até a faxineira e pergunta se alguém havia saido da casa durante essa tarde.

- Ela responde que ninguém havia saido, mas que ela viu o jardineiro 
rodear a casa com uma tesoura bem grande.

[Nova pista obtida! - a faxineira avistou o jardineiro com uma tesoura de poda no jardim.]
"""

txt_f02 = """- Você decide, então, perguntar sobre o mordomo.

- Ela responde que não viu ninguém sair da resiência e que o mordomo provavelmente
estaria dentro da casa.

[Nova pista obtida! - a faxineira diz que o mordomo nao saiu de casa.]
"""

# Jardineiro
txt_j00 = """- Você vai até o jardineiro, no jardim, e pergunta onde ela estava no momento do ocorrido.

- Ele responde que estava aparando os arbustos na entrada da casa e que viu a faxineira limpando 
algo na varanda.

[Nova pista obtida! - o jardineiro estava podando o jardim sozinho.]
[Nova pista obtida! - o jardineiro viu a faxineira limpando vidro quebrado na varanda.]
"""

txt_j01 = """- Você decide, então, perguntar sobre o mordomo.

- Ela responde que não viu ninguém sair da resiência e que o mordomo provavelmente
estaria dentro da casa.

[Nova pista obtida! - o jardineiro diz que o mordomo nao saiu de casa.]
"""

# Mordomo
txt_m00 = """- Você vai até o mordomo e pergunta onde ela estava no momento do ocorrido.

- Ele responde que tinha ido ao mercado.

[Nova pista obtida! - o mordomo foi ao mercado.]
"""

txt_m01 = """- Você vai novamente até o mordomo e conta que a faxineira falou que ele não
saiu para ir ao mercado naquela tarde.

- Ele responde que a faxineira está mentindo pois, quando ele voltou, se deparou 
com ela limpando uma bagunça que parecia ser um monte de vidro quebrado, indicando
sinais de luta.

[Nova pista obtida! - o mordomo acusa a faxineira de ter assassinado a Sra. Brown.]
"""


# FUNÇÕES
# Typing FX
def typing_fx(text):
    while True:
        sfx_typing.play()
        for i in range(len(text)):
            print(text[i], end="")
            sleep(choice(txt_fx_vel))
        sleep(0.03)
        sfx_typing.stop()
        break


# Gerar Tabela
def gen_tab(tabela):
    x = None
    if not tabela == "pistas_tab":
        x = "firstrow"
    print(tabulate(tabela, headers=x, tablefmt="fancy_grid"))


# Selecionar
def opt_select(add=1):
    global user_in
    x = '123'
    if add == 0:
        x = '0123'
    while True:
        user_in = str(input("Selecione uma opção: ")).strip()
        sfx_enter.play()
        if len(user_in) == 1 and user_in in x:
            user_in = int(user_in)
            break
        print("--> Digite apenas um número entre 1 e 3!")
    return user_in


# INÍCIO

# Regras
sfx_menu.play()

print("""
   ______________________________
 / \                             \.
|   |           𝗥𝗘𝗚𝗥𝗔𝗦           |.
 \_ |                            |.
    |  1. Você será o investiga- |.
    |     dor chefe da operação. |.
    |                            |.
    |  2. Você deve descobrir    |.
    |     quem é o assassino     |.
    |     com base nas pistas.   |.
    |                            |.
    |  3. Não há tempo limite.   |.
    |                            |.
    |  4. O jogo acaba quando    |.
    |     alguém for preso.      |.
    |                            |.
    |  5. Você ganha o jogo se   |.
    |     acertar quem era o     |.
    |     assassino, caso con-   |.
    |     trário, você perde.    |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.
    """)

while True:
    user_in = str(input("Pressione [Enter] para iniciar:"))
    if user_in == "":
        sfx_menu.stop()
        sfx_enter.play()
        break
    print("--> Pressione apenas [Enter] para iniciar!")

print("\n" * 100)  # faz sumir as regras da dela
sleep(2)

# Jogo
mixer.music.play()

typing_fx(main_txt_01)

while True:
    gen_tab(acoes)
    user_in = opt_select()
    if user_in == 1:  # Investigar
        gen_tab(suspeitos)
        user_in = opt_select()

        if user_in == 1:  # Faxineira
            if contador_faxineira == 0:
                typing_fx(txt_f00)
                pistas_tab.append(pistas[1])
            elif contador_faxineira == 1:
                typing_fx(txt_f01)
                pistas_tab.append(pistas[2])
            elif contador_faxineira == 2:
                typing_fx(txt_f02)
                pistas_tab.append(pistas[6])
            else:
                typing_fx(txt_vazio_02)
            contador_faxineira += 1
        elif user_in == 2:  # Jardineiro
            if contador_jardineiro == 0:
                typing_fx(txt_j00)
                pistas_tab.append(pistas[0])
                pistas_tab.append(pistas[3])

            elif contador_jardineiro == 1:
                typing_fx(txt_j01)
                pistas_tab.append(pistas[7])
            else:
                typing_fx(txt_vazio_02)
            contador_jardineiro += 1
        else:  # Mordomo
            if contador_mordomo == 0:
                typing_fx(txt_m00)
                pistas_tab.append(pistas[4])

            elif contador_mordomo >= 1:
                if contador_faxineira < 2:
                    typing_fx(txt_vazio_01)
                elif contador_faxineira >= 2 and not pistas[5] in pistas_tab:
                    typing_fx(txt_m01)
                    pistas_tab.append(pistas[5])
                elif pistas[5] in pistas_tab:
                    typing_fx(txt_vazio_02)
            contador_mordomo += 1

    elif user_in == 2:  # Acusar
        if not len(pistas_tab) >= 5:
            print("--> Ainda está muito cedo para prender alguém. Obtenha mais pistas!")
            continue
        gen_tab(suspeitos)
        print("Digite 0 para voltar.")
        user_in = opt_select(add=0)
        if user_in == 0:
            continue
        elif user_in == 1 or user_in == 2:  # Acusou o jardineiro ou a faxineira
            print("""
        ██████╗ ███████╗██████╗ ██████╗  ██████╗ ████████╗ █████╗
        ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗
        ██║  ██║█████╗  ██████╔╝██████╔╝██║   ██║   ██║   ███████║
        ██║  ██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══██║
        ██████╔╝███████╗██║  ██║██║  ██║╚██████╔╝   ██║   ██║  ██║
        ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝

        É uma pena. Você deixou o assassino impune.
            """)
        else:  # Acusou o mordomo
            print("""
                                  █
        ██╗   ██╗██╗████████╗ ██████╗ ██████╗ ██╗ █████╗
        ██║   ██║██║╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗
        ██║   ██║██║   ██║   ██║   ██║██████╔╝██║███████║
        ╚██╗ ██╔╝██║   ██║   ██║   ██║██╔══██╗██║██╔══██║
         ╚████╔╝ ██║   ██║   ╚██████╔╝██║  ██║██║██║  ██║
          ╚═══╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝

        Parabéns, você acertou!
            """)
        break
    else:  # Mostrar pistas
        gen_tab(pistas_tab)

print("FIM.")
