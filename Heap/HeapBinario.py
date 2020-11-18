import random


class HeapBinarioCrescente:
    def __init__(self):
        self.vetor = []
        self.ultima = 0

    def insere(self, dado):
        self.ultima = self.ultima + 1
        i = self.ultima
        while i > 1 and self.vetor[(i//2)-1] > dado:
            if len(self.vetor) > i:
                self.vetor[i-1] = self.vetor[(i//2)-1]
            else:
                self.vetor.append(self.vetor[(i//2)-1])
            i = (i//2)
        if len(self.vetor) > i:
            self.vetor[i-1] = dado
        else:
            self.vetor.append(dado)

    def remove_menor_elemento(self):
        if len(self.vetor) < 1:
            raise Exception("Heap underflow!")
        valor = self.vetor[0]
        self.vetor[0] = self.vetor[self.ultima-1]
        self.ultima -= 1
        i = 1
        while ((2*i)-1 <= self.ultima and self.vetor[i-1] > self.vetor[(2*i)-1]) or ((2*i)-1 < self.ultima and self.vetor[i-1] > self.vetor[2*i]):
            menor = (2*i)-1
            if (2*i)-1 < self.ultima and self.vetor[2*i] <= self.vetor[(2*i)-1]:
                menor += 1
            self.vetor[i-1], self.vetor[menor] = self.vetor[menor], self.vetor[i-1]
            i = menor
        self.vetor = self.vetor[:-1]
        return valor

    def heap_sort(self, lista, lista_size):
        for i in range(lista_size):
            self.insere(lista[i])
        for i in range(lista_size):
            lista[i] = self.remove_menor_elemento()
        return lista


if __name__ == "__main__":
    s = 5
    # x = list(range(s))[::-1]
    # random.shuffle(x)
    x = [3, 0, 1, 2, 4]
    print(x)
    heap = HeapBinarioCrescente()
    print(heap.heap_sort(x, s))
    # print(heap.vetor)
    # print(heap.remove_menor_elemento())
    # print(heap.vetor)
