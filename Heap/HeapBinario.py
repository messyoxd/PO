import random
import time


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
        while ((2*i)-1 <= self.ultima and self.vetor[i-1] < self.vetor[(2*i)-1]) or ((2*i)-1 < self.ultima and self.vetor[i-1] < self.vetor[2*i]):
            maior = (2*i)-1
            if (2*i)-1 < self.ultima and self.vetor[2*i] >= self.vetor[(2*i)-1]:
                maior += 1
            self.vetor[i-1], self.vetor[maior] = self.vetor[maior], self.vetor[i-1]
            i = maior
        self.vetor = self.vetor[:-1]
        return valor

    def heap_sort(self, lista, lista_size):
        for i in range(lista_size):
            self.insere(lista[i])
        for i in range(lista_size):
            lista[i] = self.remove_maior_elemento()
        return lista

def return_random_list(size):
    randomlist = []
    for i in range(size):
        n = random.randint(0,size-1)
        randomlist.append(n)
    return randomlist

if __name__ == "__main__":
    instance_size = 5000000
    # x = list(range(s))[::-1]
    # random.shuffle(x)
    list1 = return_random_list(instance_size)
    list2 = return_random_list(instance_size)
    heap=HeapBinarioDecrescente()
    start = time.time()
    result = max(list1)
    end = time.time()
    print(f"max -> {result} segundos: %.3f" %(end - start))
    for i in list2:
        heap.insere(i)
    start = time.time()
    result = heap.remove_maior_elemento()
    end = time.time()
    print(f"max -> {result} segundos: %.3f" %(end - start))
