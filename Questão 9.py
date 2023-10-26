def merge_sort(array):
    if len(array) <= 1:
        return array

    meio = len(array) // 2
    esquerda = array[:meio]
    direita = array[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)

def merge(left, right):
    resultado = []
    esquerdaX, direitaX = 0, 0

    while esquerdaX < len(left) and direitaX < len(right):
        if left[esquerdaX] < right[direitaX]:
            resultado.append(left[esquerdaX])
            esquerdaX += 1
        else:
            resultado.append(right[direitaX])
            direitaX += 1

    resultado.extend(left[esquerdaX:])
    resultado.extend(right[direitaX:])
    return resultado

def par_com_soma(array, x):
    sortedArray = merge_sort(array)

    left, right = 0, len(sortedArray) - 1

    while left < right:
        soma = sortedArray[left] + sortedArray[right]

        if soma == x:
            return True
        elif soma < x:
            left += 1
        else:
            right -= 1

    return False

# Exemplo de uso:
S = [1, 3, 5, 7, 9]
x = 12
if par_com_soma(S, x):
    print("Existe um par cuja soma é igual a", x)
else:
    print("Não existe um par cuja soma seja igual a", x)
