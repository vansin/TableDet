import time
from concurrent import futures


def cpu_bound(number):
    return sum(i * i for i in range(number))


def calculate_sums(numbers):
    for number in numbers:
        print(cpu_bound(number))


def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))


def main_process():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    with futures.ProcessPoolExecutor() as pe:
        result = pe.map(cpu_bound, numbers)
        print(f"result: {list(result)}")
    end_time = time.perf_counter()
    print('multiprocessing Calculation takes {} seconds'.format(
        end_time - start_time))


if __name__ == '__main__':
    main()
    main_process()
