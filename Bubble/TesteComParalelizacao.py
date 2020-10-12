
import random
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

from Bubble import Bubble


class ParallelizedSortAlgorithmTester:

    def create_random_list(self, size) -> list:
        x = list(range(size))
        random.shuffle(x)
        return x

    def create_crescent_bubble_worst_case(self, size) -> list:
        """
        Retorna uma lista decrescente de tamanho "size"
        """
        return list(range(size))[::-1]

    def time_it(self, algorithm, algorithm_name, random_list, instance_size) -> dict:
        start = time.time()
        algorithm(random_list, instance_size)
        end = time.time()
        return {algorithm_name: [instance_size, end - start]}

    def plot_in_lines(self, data, cv, label) -> None:
        x = []
        y = []
        for i in range(len(data)):
            result = data[i].result()
            x.append(list(result.values())[0][0])
            y.append(list(result.values())[0][1])
            print(f"{label} -> elementos: {x[i]} segundos: %.3f" % y[i])
        cv.plot(x, y, label=label)

    def worst_case_test(self, algorithms, algorithms_names, instance_sizes) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        pool = ProcessPoolExecutor()
        for i in range(len(algorithms)):
            random_list = self.create_crescent_bubble_worst_case(
                instance_sizes[i])
            futures.append(pool.submit(
                self.time_it, algorithms[i], algorithms_names[i], random_list, instance_sizes[i]))
        return futures
        ######################################

    def random_test(self, algorithms, algorithms_names, instance_sizes) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        pool = ProcessPoolExecutor()
        for i in range(len(algorithms)):
            random_list = self.create_random_list(instance_sizes[i])
            futures.append(pool.submit(
                self.time_it, algorithms[i], algorithms_names[i], random_list, instance_sizes[i]))
        return futures
        ######################################

    def plot_data(self, data_list, title, ylabel, xlabel) -> None:
        ###### Plotar os dados ###############
        fig, ax = plt.subplots()
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)
        ax.set_title(title)
        for i in range(len(data_list)):
          self.plot_in_lines(data_list[i][0], ax, data_list[i][1])
        ax.legend()
        fig.savefig('BubbleSortParalelizado.png')
        ######################################

if __name__ == "__main__":
    tester = ParallelizedSortAlgorithmTester()
    random_test_results = tester.random_test(
        [
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort
        ],
        [
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
        ],
        [
            1000,
            2000,
            3000,
            4000,
            5000,
            8000,
            11000,
            15000
        ]
    )
    worst_case_test_results = tester.worst_case_test(
        [
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort,
            Bubble.crescent_sort
        ],
        [
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
            "Bubble",
        ],
        [
            1000,
            2000,
            3000,
            4000,
            5000,
            8000,
            11000,
            15000
        ]
    )
    tester.plot_data(
        [
            (random_test_results, "Aleatorio"),
            (worst_case_test_results, "Pior Caso")
        ],
        "Comparacao Bubblesort",
        "Tempo de computacao dos algoritmos",
        "Tamanho da instancia"
    )
