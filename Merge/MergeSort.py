import random


class Merge():

    @staticmethod
    def crescent_sort(sortable_list, start, end) -> list:
        """
        Parameter: A list "sortable_list" with elements that have the same type
            and the start and end positions of "sortable_list"
        Return: A crescent sorted list 
        Brief: 

        """
        if start < end:
            if (start+end)%2 == 1:
                if end - start == 1:
                    middle = start
                else:
                    middle = ((start+end + 1)//2)
            else:
                middle = (start+end)//2
            if start < middle:
                sortable_list = Merge.crescent_sort(
                    sortable_list, start, middle)
            if middle + 1 < end:
                sortable_list = Merge.crescent_sort(
                    sortable_list, middle+1, end)
            sortable_list = Merge.merge(sortable_list, start, middle, end)
        return sortable_list

    @staticmethod
    def merge(sortable_list, start, middle, end) -> list:
        """
        Parameter: A list "sortable_list" with elements that have the same type
            and ints "start", "middle" and "end" as positions of "sortable_list".
            "sortable_list" must be sorted between "start" and "middle" and
            between "middle+1" and "end" in crescent 
        Return: A crescent sorted list from "start" to "end" positions
        Brief: 

        """
        i, j, aux = start, middle+1, []
        while i <= middle and j <= end:
            if sortable_list[i] <= sortable_list[j]:
                aux.append(sortable_list[i])
                i += 1
            else:
                aux.append(sortable_list[j])
                j += 1
        if i <= middle:
            for j in range(middle, i-1, -1):
                sortable_list[end - middle + j] = sortable_list[j]
            for i in range(len(aux)):
                sortable_list[i+start] = aux[i]
        return sortable_list


if __name__ == "__main__":
    s = 20
    x = list(range(s))[::-1]
    random.shuffle(x)
    print(x)
    print(Merge.crescent_sort(x, 0, len(x)-1))
