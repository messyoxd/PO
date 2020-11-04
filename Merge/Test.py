
from Merge import Merge
from concurrent.futures import ProcessPoolExecutor
import matplotlib.pyplot as plt
import time
import sys
import random
import matplotlib as mpl
mpl.use('Agg')


class SortAlgorithmTester:

    def create_random_list(self, size) -> list:
        x = list(range(size))
        random.shuffle(x)
        return x

    def worst_case_instance(self, size) -> list:
        """
        Retorna uma lista decrescente de tamanho "size"
        """
        return list(range(size))[::-1]

    def time_it(self, algorithm, algorithm_name, random_list, instance_size, parameters, label=None) -> dict:
        if len(parameters) == 1:
            start = time.time()
            algorithm(random_list, parameters[0])
            end = time.time()
        elif len(parameters) == 2:
            start = time.time()
            algorithm(random_list, parameters[0], parameters[1])
            end = time.time()
        else:
            start = time.time()
            algorithm(random_list, parameters[0])
            end = time.time()
        if label:
            print(f"{label} -> elementos: {instance_size} segundos: %.3f" %
                  (end - start))
        return {algorithm_name: [instance_size, end - start]}

    def plot_in_lines_threaded(self, data, cv, label) -> None:
        x = []
        y = []
        for i in range(len(data)):
            result = data[i].result()
            x.append(list(result.values())[0][0])
            y.append(list(result.values())[0][1])
            print(f"{label} -> elementos: {x[i]} segundos: %.3f" % y[i])
        cv.plot(x, y, label=label)

    def plot_in_lines(self, data, cv, label) -> None:
        x = []
        y = []
        for i in range(len(data)):
            result = data[i]
            x.append(list(result.values())[0][0])
            y.append(list(result.values())[0][1])
        cv.plot(x, y, label=label)

    def worst_case_test_threaded(self, algorithms, algorithms_names, instance_sizes, parameters, max_workers=None) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        pool = ProcessPoolExecutor(max_workers=max_workers)
        for i in range(len(algorithms)):
            random_list = self.worst_case_instance(
                instance_sizes[i])
            futures.append(pool.submit(
                self.time_it, algorithms[i], algorithms_names[i], random_list, instance_sizes[i], parameters[i]))
        return futures
        ######################################

    def worst_case_test(self, algorithms, algorithms_names, instance_sizes, parameters) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        for i in range(len(algorithms)):
            worst = self.worst_case_instance(
                instance_sizes[i])
            futures.append(
                self.time_it(
                    algorithms[i], algorithms_names[i], worst, instance_sizes[i], parameters[i], "Pior Caso")
            )
        return futures
        ######################################

    def random_test_threaded(self, algorithms, algorithms_names, instance_sizes, parameters, max_workers=None) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        pool = ProcessPoolExecutor(max_workers=max_workers)
        for i in range(len(algorithms)):
            random_list = self.create_random_list(instance_sizes[i])
            futures.append(pool.submit(
                self.time_it, algorithms[i], algorithms_names[i], random_list, instance_sizes[i], parameters[i]))
        return futures
        ######################################

    def random_test(self, algorithms, algorithms_names, instance_sizes, parameters) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        for i in range(len(algorithms)):
            random_list = self.create_random_list(instance_sizes[i])
            futures.append(
                self.time_it(
                    algorithms[i], algorithms_names[i], random_list, instance_sizes[i], parameters[i], "Aleatorio")
            )
        return futures
        ######################################

    

    def plot_data(self, data_list, title, ylabel, xlabel, workers=None) -> None:
        ###### Plotar os dados ###############
        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(formater)
        ax.xaxis.set_major_formatter(formater)
        ax.set_ylabel(ylabel)
        ax.set_xlabel(xlabel)
        ax.set_title(title)
        if workers:
            for i in range(len(data_list)):
                self.plot_in_lines_threaded(
                    data_list[i][0], ax, data_list[i][1])
            ax.legend()
            fig.savefig(f'MergeSort{workers}Threads.png')
        else:
            for i in range(len(data_list)):
                self.plot_in_lines(data_list[i][0], ax, data_list[i][1])
            ax.legend()
            fig.savefig(f'MergeSortSingleThread.png')
        ######################################

def formater(x, pos):
        return '{:1.0f}'.format(x*1)

if __name__ == "__main__":
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print("the parameters are: ('threaded' and int) or 'singlethreaded' ")
    else:
        if sys.argv[1] == "threaded":
            try:
                if int(sys.argv[2]) > 0:
                    workers = int(sys.argv[2])
            except Exception as e:
                raise Exception("second parameter is not int!")
            paralelizado = True
        elif sys.argv[1] == "singlethreaded":
            paralelizado = False
        else:
            raise Exception("parameter not identified!")
        if paralelizado:
            tester = SortAlgorithmTester()
            start = time.time()
            random_test_results = tester.random_test_threaded(
                [
                    Merge.crescent_sort
                ]*6,
                [
                    "Merge"
                ]*6,
                [100000, 200000, 400000, 700000, 1000000, 5000000],
                [
                    [0, 100000-1],
                    [0, 200000-1],
                    [0, 400000-1],
                    [0, 700000-1],
                    [0, 1000000-1],
                    [0, 5000000-1],
                ],
                workers
            )

            tester.plot_data(
                [
                    (random_test_results, "Aleatorio"),
                ],
                f"Comparacao MergeSort MultiThreaded ({workers} threads)",
                "Tempo de computacao(segundos)",
                "Tamanho da instancia",
                workers
            )
            end = time.time()
            print(f"tempo decorrido desde o inicio do teste: %.3f" %
                  (end - start))
        else:
            tester = SortAlgorithmTester()
            start = time.time()
            random_test_results = tester.random_test(
                [
                    Merge.crescent_sort
                ]*6,
                [
                    "Merge"
                ]*6,
                [100000, 200000, 400000, 700000, 1000000, 5000000],
                [
                    [0, 100000-1],
                    [0, 200000-1],
                    [0, 400000-1],
                    [0, 700000-1],
                    [0, 1000000-1],
                    [0, 5000000-1],
                ],
            )

            tester.plot_data(
                [
                    (random_test_results, "Aleatorio"),
                ],
                "Comparacao MergeSort Single Thread",
                "Tempo de computacao (segundos)",
                "Tamanho da instancia"
            )
            end = time.time()
            print(f"tempo decorrido desde o inicio do teste: %.3f" %
                  (end - start))
