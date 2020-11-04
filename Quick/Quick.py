import random


class Quick:

    @staticmethod
    def partition(sortable_list, start, end) -> int:
        pivo = sortable_list[start]
        i = start + 1
        j = end
        while i <= j:
            while i <= j and sortable_list[i] <= pivo:
                i += 1
            while sortable_list[j] > pivo:
                j -= 1
            if i <= j:
                sortable_list[i], sortable_list[j] = sortable_list[j], sortable_list[i]
                i += 1
                j -= 1
        sortable_list[start], sortable_list[j] = sortable_list[j], sortable_list[start]
        return j

    @staticmethod
    def crescent_quick(sortable_list, start, end) -> list:
        if start < end:
            j = Quick.partition(sortable_list, start, end)
            if start < j - 1:
                Quick.crescent_quick(sortable_list, start, j - 1)
            if j + 1 < end:
                Quick.crescent_quick(sortable_list, j+1, end)
        return sortable_list


if __name__ == "__main__":
    s = 1000
    x = list(range(s))[::-1]
    random.shuffle(x)
    # print(x)
    print(Quick.crescent_quick(x, 0, len(x) - 1))
