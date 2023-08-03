def bubble_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        check = False
        for i in range(0, n - j - 1):
            if compareNL(lista[i], lista[i + 1]) > 0:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                check = True
        if not check:
            break

    return lista
def compareNL(item1, item2):
    letter1, number1 = item1[0], int(item1[1:])
    letter2, number2 = item2[0], int(item2[1:])
    if letter1 == letter2:
        return number1 - number2
    else:
        return ord(letter1) - ord(letter2)

N = int(input())
participantes = input().split(' ')
sort_list = bubble_sort(participantes)
local = sort_list[N - 1]

if len(local) > 2:
    print(f'O vencedor está na fila {local[0]} poltrona {local[1]+local[2]}!')
else:
    print(f'O vencedor está na fila {local[0]} poltrona {local[1]}!')