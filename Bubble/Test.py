from TesteComParalelizacao import ParallelizedSortAlgorithmTester
from TesteSemParalelizacao import NotParallelizedSortAlgorithmTester
from Bubble import Bubble
import time
import sys

if __name__ == "__main__":

    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("the parameters are: 'threaded' or 'singlethreaded' ")
    else:
        
        if sys.argv[1] == "threaded":
            paralelizado = True
        elif sys.argv[1] == "singlethreaded":
            paralelizado = False
        else:
            raise Exception("parameter not identified!")
        if paralelizado:
            tester = ParallelizedSortAlgorithmTester()
            start = time.time()        
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
                "Comparacao Bubblesort MultiThreaded",
                "Tempo de computacao dos algoritmos",
                "Tamanho da instancia"
            )
            end = time.time()
            print(f"tempo decorrido desde o inicio do teste: %.3f" % (end - start))
        else:
            tester = NotParallelizedSortAlgorithmTester()
            start = time.time()  
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
                "Comparacao Bubblesort Single Thread",
                "Tempo de computacao (segundos)",
                "Tamanho da instancia"
            )
            end = time.time()
            print(f"tempo decorrido desde o inicio do teste: %.3f" % (end - start))
