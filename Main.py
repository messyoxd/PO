import sys
import random
import time
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

from Bubble.Bubble import Bubble
from Selection.Selection import Selection
from Insertion.Insertion import Insertion
from Shell.Shell import Shell
from Quick.Quick import Quick
from Merge.Merge import Merge
from Heap.HeapBinario import HeapBinarioCrescente
from Counting.CountingSort import CountingSort


class SortAlgorithmTester:

    def create_random_list(self, size) -> list:
        randomlist = []
        for i in range(size):
            n = random.randint(0,size-1)
            randomlist.append(n)
        return randomlist

    def time_it(self, algorithm, algorithm_name, random_list, instance_size, label=None) -> dict:
        if algorithm_name in ["Quick", "Merge"]:
            start = time.time()
            algorithm(random_list, 0, instance_size-1)
            end = time.time()
        elif algorithm_name == "CountingSort":
            maior_elemento = max(random_list)
            start = time.time()
            algorithm(random_list, instance_size-1, maior_elemento)
            end = time.time()
        elif algorithm == "Heap":
            heap = HeapBinarioCrescente()
            start = time.time()
            heap.heap_sort(random_list, instance_size)
            end = time.time()
        else:
            start = time.time()
            algorithm(random_list, instance_size)
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

    def algorithm_comparation_random_list_single_thread(self, algorithms, algorithms_names, instance_sizes):
        result_tuple_list = []
        for i in range(len(algorithms)):
            result_tuple_list.append((self.random_test(
                [
                    algorithms[i]
                ]*len(instance_sizes),
                [
                    algorithms_names[i]
                ]*len(instance_sizes),
                instance_sizes,
            ), algorithms_names[i]))
        self.plot_data(
            result_tuple_list,
            "Comparacao Algoritmos Lista Embaralhada Single Thread",
            "Tempo de computacao (segundos)",
            "Tamanho da instancia",
            "ComparacaoListaEmbaralhadaSingleThread"
        )

    def algorithm_comparation_random_list_multi_thread(self, algorithms, algorithms_names, instance_sizes, max_workers=None):
        result_tuple_list = []
        for i in range(len(algorithms)):
            result_tuple_list.append((self.random_test_threaded(
                [
                    algorithms[i]
                ]*len(instance_sizes),
                [
                    algorithms_names[i]
                ]*len(instance_sizes),
                instance_sizes,
                workers
            ), algorithms_names[i]))
        if workers:
            filename = f"ComparacaoListaEmbaralhada{workers}Thread(s)"
        else:
            filename = "ComparacaoListaEmbaralhada1Thread"
        self.plot_data(
            result_tuple_list,
            f"Comparacao Algoritmos Lista Embaralhada {workers} Thread(s)",
            "Tempo de computacao (segundos)",
            "Tamanho da instancia",
            filename,
            workers
        )

    def algorithm_comparation_worst_case_single_thread(self, algorithms, algorithms_names, instance_sizes, worst_case_generators):
        result_tuple_list = []
        for i in range(len(algorithms)):
            result_tuple_list.append((self.worst_case_test(
                [
                    algorithms[i]
                ]*len(instance_sizes),
                [
                    algorithms_names[i]
                ]*len(instance_sizes),
                instance_sizes,
                worst_case_generators[i]
            ), algorithms_names[i]))
        self.plot_data(
            result_tuple_list,
            "Comparacao Algoritmos Pior Caso Single Thread",
            "Tempo de computacao (segundos)",
            "Tamanho da instancia",
            "ComparacaoPiorCasoSingleThread"
        )

    def algorithm_comparation_worst_case_multi_thread(self, algorithms, algorithms_names, instance_sizes, worst_case_generators, max_workers=None):
        result_tuple_list = []
        for i in range(len(algorithms)):
            result_tuple_list.append((self.worst_case_test(
                [
                    algorithms[i]
                ]*len(instance_sizes),
                [
                    algorithms_names[i]
                ]*len(instance_sizes),
                instance_sizes,
                worst_case_generators[i]
            ), algorithms_names[i]))
        if workers:
            filename = f"ComparacaoPiorCaso{workers}Thread(s)"
        else:
            filename = "ComparacaoPiorCaso1Thread"
        self.plot_data(
            result_tuple_list,
            f"Comparacao Algoritmos Pior Caso {workers} Thread(s)",
            "Tempo de computacao (segundos)",
            "Tamanho da instancia",
            filename,
            workers
        )

    def worst_case_test(self, algorithms, algorithms_names, instance_sizes, worst_case_generator) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        for i in range(len(algorithms)):
            worst_case_list = worst_case_generator(instance_sizes[i])
            futures.append(
                self.time_it(
                    algorithms[i], algorithms_names[i], worst_case_list, instance_sizes[i], algorithms_names[i])
            )
        return futures
        ######################################

    def worst_case_test_threaded(self, algorithms, algorithms_names, instance_sizes, worst_case_generator, max_workers=None) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        pool = ProcessPoolExecutor(max_workers=max_workers)
        for i in range(len(algorithms)):
            worst_case_list = worst_case_generator(
                instance_sizes[i])
            futures.append(pool.submit(
                self.time_it, algorithms[i], algorithms_names[i], worst_case_list, instance_sizes[i]))
        return futures
        ######################################

    def random_test_threaded(self, algorithms, algorithms_names, instance_sizes, max_workers=None) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        pool = ProcessPoolExecutor(max_workers=max_workers)
        for i in range(len(algorithms)):
            random_list = self.create_random_list(instance_sizes[i])
            futures.append(pool.submit(
                self.time_it, algorithms[i], algorithms_names[i], random_list, instance_sizes[i]))
        return futures
        ######################################

    def random_test(self, algorithms, algorithms_names, instance_sizes) -> list:
        ##### Cronometrar os algoritmos ######
        futures = []
        for i in range(len(algorithms)):
            random_list = self.create_random_list(instance_sizes[i])
            futures.append(
                self.time_it(
                    algorithms[i], algorithms_names[i], random_list, instance_sizes[i], algorithms_names[i])
            )
        return futures
        ######################################

    def plot_data(self, data_list, title, ylabel, xlabel, filename, workers=None) -> None:
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
        else:
            for i in range(len(data_list)):
                self.plot_in_lines(data_list[i][0], ax, data_list[i][1])
        ax.legend()
        fig.savefig(f'{filename}.png')
        ######################################


def formater(x, pos):
    return '{:1.0f}'.format(x*1)


if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("the parameters are: ('threaded', int and 'random' or 'worst') or ('singlethreaded' and 'random' or 'worst') ")
    else:
        if sys.argv[1] == "threaded":
            try:
                if int(sys.argv[2]) > 0:
                    workers = int(sys.argv[2])
            except Exception as e:
                raise Exception("second parameter is not int!")
            try:
                if sys.argv[3] == "random":
                    instance_type = "random"
                elif sys.argv[3] == "worst":
                    instance_type = "worst"
                else:
                    raise Exception(
                        "third parameter is not 'random' or 'worst'!")
            except Exception as e:
                print(e)
                raise Exception("Problem with the third parameter!")
            paralelizado = True

        elif sys.argv[1] == "singlethreaded":
            try:
                if sys.argv[2] == "random":
                    instance_type = "random"
                elif sys.argv[2] == "worst":
                    instance_type = "worst"
                else:
                    raise Exception(
                        "second parameter is not 'random' or 'worst'!")
            except Exception as e:
                print(e)
                raise Exception("Problem with the second parameter!")
            paralelizado = False
        else:
            raise Exception("parameter not identified!")

        tester = SortAlgorithmTester()
        if paralelizado:
            if instance_type == "random":
                start = time.time()
                tester.algorithm_comparation_random_list_multi_thread(
                    [
                        # Bubble.crescent_sort,
                        # Selection.crescent_selection,
                        # Insertion.direct_crescent_insertion,
                        Shell.crescent_shell,
                        Quick.crescent_quick,
                        Merge.crescent_sort,
                        HeapBinarioCrescente.heap_sort,
                        CountingSort.crescent_sort
                    ],
                    [
                        # "Bubble",
                        # "Selection",
                        # "Insertion",
                        "Shell",
                        "Quick",
                        "Merge",
                        "Heap",
                        "CountingSort"
                    ],
                    [
                        50000,
                        100000,
                        500000,
                        1000000,
                        5000000,
                    ]
                )
            else:
                start = time.time()
                tester.algorithm_comparation_worst_case_multi_thread(
                    [
                        Bubble.crescent_sort,
                        Selection.crescent_selection,
                        Insertion.direct_crescent_insertion,
                        Shell.crescent_shell
                    ],
                    [
                        "Bubble",
                        "Selection",
                        "Insertion",
                        "Shell"
                    ],
                    [
                        1000,
                        2000,
                        3000,
                        4000,
                        5000,
                        8000,
                        11000,
                        15000,
                        50000,
                        100000,
                    ],
                    [
                        Bubble.worst_case,
                        Selection.worst_case,
                        Insertion.worst_case
                    ]
                )
            end = time.time()
            print(f"tempo decorrido desde o inicio do teste: %.3f" %
                  (end - start))

        else:
            if instance_type == "random":
                heap = HeapBinarioCrescente()
                start = time.time()
                tester.algorithm_comparation_random_list_single_thread(
                    [
                        # Bubble.crescent_sort,
                        # Selection.crescent_selection,
                        # Insertion.direct_crescent_insertion,
                        # Shell.crescent_shell,
                        Quick.crescent_quick,
                        Merge.crescent_sort,
                        heap.heap_sort,
                        CountingSort.crescent_sort
                    ],
                    [
                        # "Bubble",
                        # "Selection",
                        # "Insertion",
                        # "Shell",
                        "Quick",
                        "Merge",
                        "Heap",
                        "CountingSort"
                    ],
                    [
                        50000,
                        100000,
                        500000,
                        1000000,
                        5000000,
                    ]
                )
            else:
                start = time.time()
                tester.algorithm_comparation_worst_case_single_thread(
                    [
                        Bubble.crescent_sort,
                        Selection.crescent_selection,
                        Insertion.direct_crescent_insertion,
                        Shell.crescent_shell
                    ],
                    [
                        "Bubble",
                        "Selection",
                        "Insertion",
                        "Shell"
                    ],
                    [
                        1000,
                        2000,
                        3000,
                        4000,
                        5000,
                        8000,
                        11000,
                        15000,
                        50000,
                        100000,
                    ],
                    [
                        Bubble.worst_case,
                        Selection.worst_case,
                        Insertion.worst_case,
                        Shell.worst_case
                    ]
                )
            end = time.time()
            print(f"tempo decorrido desde o inicio do teste: %.3f" %
                  (end - start))
