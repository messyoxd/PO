
from BucketSort import *
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

    def time_it(self, algorithm, algorithm_name, random_list, instance_size, parameters, label=None) -> dict:
        maior_elemento = max(random_list)
        start = time.time()
        algorithm(random_list, parameters[0], maior_elemento)
        end = time.time()
        if label:
            print(f"{label} -> elementos: {instance_size}| buckets => {parameters[0]} | maior elemento -> {maior_elemento} | segundos: %.3f" %
                  (end - start))
        return {algorithm_name: [instance_size, end - start, parameters[0]]}

    def plot_in_lines(self, data, cv, label, buckets=False) -> None:
        x = []
        y = []
        for i in range(len(data)):
            result = data[i]
            if buckets:
                x.append(list(result.values())[0][2])
                y.append(list(result.values())[0][1])
            else:
                x.append(list(result.values())[0][0])
                y.append(list(result.values())[0][1])
        cv.plot(x, y, label=label)

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

    def plot_data(self, data_list, title, ylabel, xlabel, buckets=False, workers=None) -> None:
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
            fig.savefig(f'BucketSort{workers}Threads.png')
        else:
            for i in range(len(data_list)):
                self.plot_in_lines(data_list[i][0], ax, data_list[i][1], buckets)
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
            BucketSort.sort
        ]*6,
        [
            "BucketSort"
        ]*6,
        [10000, 20000, 40000, 70000, 100000, 500000],
        [
            [10000],
            [20000],
            [40000],
            [70000],
            [100000],
            [500000],
        ],
    )

    tester.plot_data(
        [
            (random_test_results, "Aleatorio"),
        ],
        "Comparacao BucketSort Single Thread",
        "Tempo de computacao (segundos)",
        "Tamanho da instancia"
    )

    print("-> Testando o BucketSort alterando a quantidade de Buckets")
    tamanho_instancia = 100000
    quantidade_buckets_max = tamanho_instancia*2
    quantidade_testes = 20
    quantidade_buckets_list = [ (quantidade_buckets_max//quantidade_testes)*x for x in range(1,quantidade_testes+1)]
    # quantidade_buckets_list = quantidade_buckets_list[::-1]
    testes = tester.random_test(
        [
            BucketSort.sort
        ]*quantidade_testes,
        [
            "BucketSort"
        ]*quantidade_testes,
        [
            100000
        ]*quantidade_testes,
        [
            [i] for i in quantidade_buckets_list
        ],
    )
    tester.plot_data(
        [
            (testes, "Alterando Buckets"),
        ],
        "Comparacao BucketSort Single Thread com quantidade variada de buckets",
        "Tempo de computacao (segundos)",
        "Quantidade de buckets",
        buckets=True
    )
    end = time.time()
    print(f"tempo decorrido desde o inicio do teste: %.3f" %
          (end - start))