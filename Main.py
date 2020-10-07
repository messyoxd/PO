
import random
import time

from Bubble.Bubble import Bubble


class SortAlgorithmTester:

    def create_random_list(self, size):
        x = list(range(size))
        random.shuffle(x)
        return x

    def test(self, algorithm):
        start = time.time()
        algorithm(self.create_random_list(10000), 10000)
        end = time.time()
        print(end - start)


if __name__ == "__main__":
    bubble = Bubble()
    tester = SortAlgorithmTester()
    tester.test(bubble.crescent_sort)
