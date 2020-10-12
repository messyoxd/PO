
import random
import time
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

from Bubble import Bubble


class SortAlgorithmTester:

    def create_random_list(self, size):
        x = list(range(size))
        random.shuffle(x)
        return x

    def time_it(self, algorithm, algorithm_name, random_list, instance_size):
        start = time.time()
        algorithm(random_list, instance_size)
        end = time.time()
        return {algorithm_name: [instance_size, end - start]}

    def test(self, algorithms, algorithms_names, instance_sizes):
        futures = []
        pool = ProcessPoolExecutor()
        for i in range(len(algorithms)):
            random_list = self.create_random_list(instance_sizes[i])
            futures.append(pool.submit(
                self.time_it, algorithms[i], algorithms_names[i], random_list, instance_sizes[i]))

        width = 0.35

        fig, ax = plt.subplots()

        for i in range(len(futures)):
            result = futures[i].result()
            algorithm = list(result.keys())[0]
            inst_size = list(result.values())[0][0]
            time = list(result.values())[0][1]
            ax.bar(str(inst_size), time, width,
                   label=f"{algorithm} com %.3f segundo(s)" % time)

        ax.set_ylabel('Tempo de computacao(segundos)')
        ax.set_xlabel('Tamanho da instancia')
        ax.set_title('Tempo de computacao dos algoritmos')
        ax.legend()

        plt.show()


if __name__ == "__main__":
    tester = SortAlgorithmTester()
    tester.test(
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
