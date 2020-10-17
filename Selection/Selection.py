import random


class Selection:

    @staticmethod
    def crescent_selection(sortable_list, size) -> list:
        """
        Parameter: A list "sortable_list" with elements that have the same type
            and a int "size" with the number of elements of the list
        Return: A crescent sorted list 
        Brief: 
                o algoritmo imagina a lista à ser ordenada como dividida
                em duas partes: A esquerda, com elementos em ordem crescente
                e de tamanho p; A direita, com os elementos em ordem diversa
                e de tamanho q. O algoritmo usa um pivo para que à cada iteração 
                do loop interno descubra-se o index do menor numero da parte direita. 
                Após descobri-lo, considera-se que a parte esquerda será aumentada em 1
                e a parte direita será diminuida em 1 e faz-se um swap da posição p com
                a posição do pivo, assim a parte esquerda fica com numeros em ordem crescente.
        """
        for i in range(size-1):
            pivo = i
            for j in range(pivo+1, size):
                if sortable_list[j] < sortable_list[pivo]:
                    pivo = j
            sortable_list[i], sortable_list[pivo] = sortable_list[pivo], sortable_list[i]
        return sortable_list

    @staticmethod
    def worst_case(size):
        """
            There's no worst case for selection sort. 
            It will always be Θ(n2)
        """
        return random.shuffle(list(range(size)))


if __name__ == "__main__":
    s = 20
    x = list(range(s))
    random.shuffle(x)
    print(x)
    print(Selection.crescent_selection(x, s))
