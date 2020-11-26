class NodeLista:
    def __init__(self, dado=0, proximo_node=None):
        self.dado = dado
        self.proximo = proximo_node
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:

    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    @staticmethod
    def from_list(lista):
        listEncad = ListaEncadeada()
        for i in lista:
            ListaEncadeada.insere_no_inicio(listEncad, i)
        return listEncad
    
    @staticmethod
    def insere_no_inicio(lista, novo_dado):
        novo_nodo = NodeLista(novo_dado)

        novo_nodo.proximo = lista.cabeca

        lista.cabeca = novo_nodo
        lista.tamanho += 1

    @staticmethod
    def insere_em_posicao(lista, posicao, node):
        i = 0
        p = lista.cabeca
        if posicao == 0:
            ListaEncadeada.insere_no_inicio(lista, node)
        else:
            while p != None or i < posicao+1:
                if i == posicao-1:
                    anterior = p
                    alvo = p.proximo

                    anterior.proximo = node
                    node.proximo = alvo

                    lista.tamanho += 1
                    i = posicao
                else:
                    i+=1
                    p = p.proximo

    @staticmethod
    def edit_em_posicao(lista, posicao, dado):
        i = 0
        p = lista.cabeca
        while p != None or i < posicao+1:
            if i == posicao:
                p.dado = dado
                i = posicao+1
            else:
                i+=1
                p = p.proximo

    @staticmethod
    def get_posicao(lista, posicao):
        i = 0
        p = lista.cabeca
        while p != None or i < posicao:
            if i == posicao:
                return p
            i+=1            
            p = p.proximo

    def printAll(self):
        p = self.cabeca
        while p != None:
            print(p.dado)
            p = p.proximo

    @staticmethod
    def crescent_sort(lista):
        # insertion sort adaptado para listas encadeadas
        if lista is not None:
            size = lista.tamanho
            for i in range(1, size):
                pivo = ListaEncadeada.get_posicao(lista, i).dado
                j = i - 1
                while j >= 0 and ListaEncadeada.get_posicao(lista, j).dado > pivo:
                    ListaEncadeada.edit_em_posicao(lista, j+1, ListaEncadeada.get_posicao(lista, j).dado)
                    j -= 1
                ListaEncadeada.edit_em_posicao(lista, j+1, pivo)
        return lista

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

class ListaDeListasEncadeadas:

    def __init__(self):
        self.lista = []

class BucketSort:

    @staticmethod
    def sort(vetor, buckets, maior_num):
        if buckets > 0:
            b = ListaDeListasEncadeadas()
            for i in range(buckets):
                b.lista.append(None)
            for i in range(len(vetor)-1,-1,-1):
                # inserir vetor[i] na primeira posicao da 
                # lista na posicao (vetor[i]*tamanho)//(maior_num+1) de B
                if b.lista[(vetor[i]*buckets)//(maior_num+1)] is None:
                    b.lista[(vetor[i]*buckets)//(maior_num+1)] = ListaEncadeada()
                ListaEncadeada.insere_no_inicio(b.lista[(vetor[i]*buckets)//(maior_num+1)], vetor[i])
            j = 0
            for i in range(buckets):
                ListaEncadeada.crescent_sort(b.lista[i])
                if b.lista[i] is not None:
                    p = b.lista[i].cabeca
                else:
                    p = None
                while p != None:
                    vetor[j] = p.dado
                    p = p.proximo
                    j += 1
                b.lista[i] = None
            return vetor
        raise Exception("Buckets deve ser maior que 0")

class Radix:

    @staticmethod
    def radix(vetor):
        maior_num = max(vetor)
        casas = 0
        exp = 1
        while maior_num//exp > 0:
            casas+=1
            Radix.sort(vetor, 10, casas, maior_num)
            exp*=10
        return vetor

    @staticmethod
    def sort(vetor, buckets, casa, maior_num):
        b = ListaDeListasEncadeadas()
        for i in range(buckets):
            b.lista.append(None)
        for i in range(len(vetor)-1,-1,-1):
            # inserir vetor[i] na primeira posicao da 
            # lista na posicao (vetor[i]*tamanho)//(maior_num+1) de B
            if vetor[i]*10//10**casa < 1:
                indice = 0
            else:
                indice = int(str(vetor[i])[casa*-1])
            if b.lista[indice] is None:
                b.lista[indice] = ListaEncadeada()
            ListaEncadeada.insere_no_inicio(b.lista[indice], vetor[i])
        j = 0
        for i in range(buckets):
            # ListaEncadeada.crescent_sort(b.lista[i])
            if b.lista[i] is not None:
                p = b.lista[i].cabeca
            else:
                p = None
            while p != None:
                vetor[j] = p.dado
                p = p.proximo
                j += 1
            b.lista[i] = None
        return vetor

if __name__ == "__main__":
    x = [32, 500, 431, 248, 9, 32, 63, 48]
    Radix.radix(x)