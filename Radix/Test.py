
from RadixSort import *
import matplotlib.pyplot as plt
import time
import random
import matplotlib as mpl
mpl.use('Agg')


class SortAlgorithmTester:

    def create_random_list(self, size) -> list:
        randomlist = []
        for i in range(size):
            n = random.randint(0,size-1)
            randomlist.append(n)
        return randomlist

    def time_it(self, algorithm, algorithm_name, random_list, instance_size, label=None) -> dict:
        start = time.time()
        algorithm(random_list)
        end = time.time()
        if label:
            print(f"{label} -> elementos: {instance_size} | segundos: %.3f" %(end - start))
        return {algorithm_name: [instance_size, end - start]}

    def plot_in_lines(self, data, cv, label) -> None:
        x = []
        y = []
        for i in range(len(data)):
            result = data[i]
            x.append(list(result.values())[0][0])
            y.append(list(result.values())[0][1])
        cv.plot(x, y, label=label)

    def random_test(self, algorithms, algorithms_names, instance_sizes) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        for i in range(len(algorithms)):
            random_list = self.create_random_list(instance_sizes[i])
            futures.append(
                self.time_it(
                    algorithms[i], algorithms_names[i], random_list, instance_sizes[i], "Aleatorio")
            )
        return futures
        ######################################

    def plot_data(self, data_list, title, ylabel, xlabel) -> None:
        ###### Plotar os dados ###############
        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(formater)
        ax.xaxis.set_major_formatter(formater)
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)
        ax.set_title(title)
        for i in range(len(data_list)):
            self.plot_in_lines(data_list[i][0], ax, data_list[i][1])
        ax.legend()
        fig.savefig(f'{title}.png')
        ######################################


def formater(x, pos):
    return '{:1.0f}'.format(x*1)


if __name__ == "__main__":
    tester = SortAlgorithmTester()
    start = time.time()
    random_test_results = tester.random_test(
        [
            Radix.radix
        ]*6,
        [
            "RadixSort"
        ]*6,
        [10000, 20000, 40000, 70000, 100000, 500000]
    )

    tester.plot_data(
        [
            (random_test_results, "Aleatorio"),
        ],
        "Comparacao RadixSort Single Thread",
        "Tempo de computacao (segundos)",
        "Tamanho da instancia"
    )