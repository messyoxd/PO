import random
import time


class HeapBinarioCrescente:
    def __init__(self):
        self.vetor = []
        self.ultima = 0

    def insere(self, dado):
        self.ultima = self.ultima + 1
        i = self.ultima
        while i > 1 and self.vetor[(i//2)-1] >= dado:
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
        while ((2*i)-1 <= self.ultima-1 and self.vetor[i-1] > self.vetor[(2*i)-1]) or ((2*i)-1 < self.ultima-1 and self.vetor[i-1] > self.vetor[(2*i)]):
            menor = (2*i)-1
            if (2*i)-1 < self.ultima-1 and self.vetor[(2*i)] < self.vetor[(2*i)-1]:
                menor += 1
            self.vetor[i-1], self.vetor[menor] = self.vetor[menor], self.vetor[i-1]
            i = menor+1
        self.vetor = self.vetor[:-1]
        return valor

    @staticmethod
    def heap_sort(lista, lista_size):
        heap = HeapBinarioCrescente()
        for i in range(lista_size):
            heap.insere(lista[i])
        for i in range(lista_size):
            lista[i] = heap.remove_menor_elemento()
        return lista

class HeapBinarioDecrescente:
    def __init__(self):
        self.vetor = []
        self.ultima = 0

    def insere(self, dado):
        self.ultima = self.ultima + 1
        i = self.ultima
        while i > 1 and self.vetor[(i//2)-1] < dado:
            if len(self.vetor) > i:
                self.vetor[i-1] = self.vetor[(i//2)-1]
            else:
                self.vetor.append(self.vetor[(i//2)-1])
            i = (i//2)
        if len(self.vetor) > i:
            self.vetor[i-1] = dado
        else:
            self.vetor.append(dado)

    def remove_maior_elemento(self):
        if len(self.vetor) < 1:
            raise Exception("Heap underflow!")
        valor = self.vetor[0]
        self.vetor[0] = self.vetor[self.ultima-1]
        self.ultima -= 1
        i = 1
        while ((2*i)-1 <= self.ultima-1 and self.vetor[i-1] < self.vetor[(2*i)-1]) or ((2*i)-1 < self.ultima-1 and self.vetor[i-1] < self.vetor[2*i]):
            maior = (2*i)-1
            if (2*i)-1 < self.ultima-1 and self.vetor[(2*i)] > self.vetor[(2*i)-1]:
                maior += 1
            self.vetor[i-1], self.vetor[maior] = self.vetor[maior], self.vetor[i-1]
            i = maior+1
        self.vetor = self.vetor[:-1]
        return valor

    @staticmethod
    def heap_sort(lista, lista_size):
        heap = HeapBinarioDecrescente()
        for i in range(lista_size):
            heap.insere(lista[i])
        for i in range(lista_size):
            lista[i] = heap.remove_maior_elemento()
        return lista

def return_random_list(size):
    randomlist = []
    for i in range(size):
        n = random.randint(0,size-1)
        randomlist.append(n)
    return randomlist

if __name__ == "__main__":
    x = return_random_list(40)
    # x = [2, 4, 3, 9, 9, 7, 9, 3, 4, 5]
    min_heap = HeapBinarioCrescente()
    for i in x:
        min_heap.insere(i)
    print(f"array -> {x}")
    print(f"menor elemento -> {min_heap.remove_menor_elemento()}")
    max_heap = HeapBinarioDecrescente()
    for i in x:
        max_heap.insere(i)
    print(f"maior elemento -> {max_heap.remove_maior_elemento()}")
    print(f"ordem crescente -> {HeapBinarioCrescente.heap_sort(x, len(x))}")
    print(f"ordem decrescente -> {HeapBinarioDecrescente.heap_sort(x, len(x))}")
    
