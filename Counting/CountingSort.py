import random


class CountingSort:

    @staticmethod
    def crescent_sort(lista, lista_size, biggest_number):
        aux = []
        c = [0 for i in range(len(lista))]
        for i in range(biggest_number+1):
            aux.append(0)
        for i in range(lista_size):
            aux[lista[i]] = aux[lista[i]] + 1
        for i in range(1, biggest_number+1):
            aux[i] = aux[i] + aux[i-1]
        for i in range(lista_size-1, -1, -1):
            aux[lista[i]] = aux[lista[i]] - 1
            c[aux[lista[i]]] = lista[i]
        for i in range(lista_size):
            lista[i] = c[i]
        return lista


if __name__ == "__main__":
    s = 100
    x = list(range(s))[::-1]
    random.shuffle(x)
    # x = [8, 4, 5, 3, 8, 2]
    print(x)
    print(CountingSort.crescent_sort(x, len(x), len(x)-1))
    # print(heap.vetor)
    # print(heap.remove_menor_elemento())
    # print(heap.vetor)
