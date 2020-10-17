import random


class Insertion:

    @staticmethod
    def naive_direct_crescent_insertion(sortable_list, size) -> list:
        if size < 2:
            return sortable_list
        else:
            pivo = 1
            while pivo < size:
                for k in range(0, pivo):
                    if sortable_list[pivo - k] < sortable_list[pivo - (k + 1)]:
                        sortable_list[pivo - (k + 1)], sortable_list[pivo -
                                                                     k] = sortable_list[pivo - k], sortable_list[pivo - (k + 1)]
                pivo += 1
            return sortable_list

    @staticmethod
    def direct_crescent_insertion(sortable_list, size) -> list:
        for i in range(1, size):
            pivo = sortable_list[i]
            j = i - 1
            while j >= 0 and sortable_list[j] > pivo:
                sortable_list[j+1] = sortable_list[j]
                j -= 1
            sortable_list[j+1] = pivo
        return sortable_list

    @staticmethod
    def worst_case(size):
        return list(range(size))[::-1]


if __name__ == "__main__":
    s = 20
    x = list(range(s))[::-1]
    random.shuffle(x)
    print(x)
    print(Insertion.direct_crescent_insertion(x, s))
