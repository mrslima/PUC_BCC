"""
Daniela dos Santos Lima

Este programa tem por objetivo realizar operações de união, interseção, diferença e produto cartesiano, a partir da leitura de um arquivo de entrada.
"""

file = open('../arquivo_01.txt', 'r')
lines = file.readlines()


def display(op_name, line_x, line_y, result):
    line_x = "{" + "".join(map(str, line_x)).strip() + "}"
    line_y = "{" + "".join(map(str, line_y)).strip() + "}"
    result = "{" + ", ".join(map(str, result)).strip() + "}"
    print(f"{op_name}: conjunto 1 {line_x}, conjunto 2 {line_y}. Resultado: {result}\n")


def f_filter(f_line):
    temp = str(f_line.replace(", ", "-")).strip()
    temp_listed = temp.split("-")
    return temp_listed


def f_union(line_x, line_y):
    op_name = "União"
    result = f_filter(line_x) + f_filter(line_y)

    for i, v in enumerate(result):  # remove elementos repetidos
        if result.count(v) > 1:
            result.pop(i)

    display(op_name, line_x, line_y, result)


def f_intersection(line_x, line_y):
    op_name = "Interseção"
    x = f_filter(line_x)
    y = f_filter(line_y)
    result = x + y

    for i, v in reversed(list(enumerate(result))):
        if not (v in x and v in y):
            result.pop(i)
        if result.count(v) > 1:
            result.pop(i)

    display(op_name, line_x, line_y, result)


def f_difference(line_x, line_y):
    op_name = "Diferença"
    x = f_filter(line_x)
    y = f_filter(line_y)
    result = []

    for i in x:  # deepcopy() manual
        result.append(i)

    for i in y:
        if i in result:
            result.remove(i)

    display(op_name, line_x, line_y, result)


def f_cartesian_product(line_x, line_y):
    op_name = "Produto cartesiano"
    x = f_filter(line_x)
    y = f_filter(line_y)
    result = []

    # remove elementos repetidos
    for i, v in reversed(list(enumerate(x))):
        if x.count(v) > 1:
            x.pop(i)

    for i, v in reversed(list(enumerate(y))):
        if y.count(v) > 1:
            y.pop(i)
    #

    for i in y:
        for k in x:
            result.append([f"{k}, {i}"])

    display(op_name, line_x, line_y, result)


for line in range(1, len(lines), 3):
    lines[line] = str(lines[line]).strip()

    if lines[line].upper() == "U":
        f_union(lines[line + 1], lines[line + 2])

    elif lines[line].upper() == "I":
        f_intersection(lines[line + 1], lines[line + 2])

    elif lines[line].upper() == "D":
        f_difference(lines[line + 1], lines[line + 2])

    else:  # lines[line].upper() == "C"
        f_cartesian_product(lines[line + 1], lines[line + 2])
