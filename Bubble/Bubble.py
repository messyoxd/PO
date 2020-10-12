class Bubble:

    @staticmethod
    def crescent_sort(sortable_list, size) -> list:
        """
        Parameter: A list "sortable_list" with elements that have the same type
            and a int "size" with the number of elements of the list
        Return: A crescent sorted list 
        Brief: 
            the list will be sorted by comparing each element from
            the beginning with it's successor, which if the successor
            is smaller the elements will swap their positions
        """
        for i in range(size - 1):
            for j in range(size - 1 - i):
                if sortable_list[j] > sortable_list[j+1]:
                    sortable_list[j], sortable_list[j +
                                                    1] = sortable_list[j+1], sortable_list[j]
        return sortable_list

    @staticmethod
    def crescent_sort_with_flag(sortable_list, size) -> list:
        """
        Parameter: A list "sortable_list" with elements that have the same type
            and a int "size" with the number of elements of the list
        Return: A crescent sorted list 
        Brief: 
                Funciona como o bubble sort crescente, mas com um 
            acréscimo de uma flag. A flag faz com que Caso nenhum 
            swap tenha ocorrido a lista já estará ordenada e o 
            algoritmo poderá parar. 
        """
        i = 0
        flag = True
        while flag:
            flag = False
            for j in range(size - 1 - i):
                if sortable_list[j] > sortable_list[j + 1]:
                    sortable_list[j], sortable_list[j +
                                                    1] = sortable_list[j+1], sortable_list[j]
                    flag = True
            i += 1
        return sortable_list


if __name__ == "__main__":
    bubble = Bubble()
    print(bubble.crescent_sort_with_flag([5, 4, 3, 2, 1], 5))
