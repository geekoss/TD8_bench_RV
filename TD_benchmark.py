from random import randint
from time import time
from sys import setrecursionlimit
setrecursionlimit(500_000)


# def bubble_sort(table):
#     pass


# def quick_sort(table):
#     pass


# def merge_sort(table):
#     pass


def generate_random_table(table_size):
    '''
    - FUNCTION
        -this function generate a random table of length = n
    - INPUT
        -table_size<int> : the size of the table to generate
    - OUTPUT
        - table<list> : the table generated
    '''
    table = []
    for _ in range(table_size):
        table.append(randint(0, 32))
    return table


def bubble_sort(table):
    '''
    - FUNCTION
        -this function sorts a given table using the Bubble sort
    - INPUT
        -table<list> : the table to sort
    - OUTPUT
        -table<list> : the table sorted
    '''
    for cpt_a in range(len(table), 0, -1):
        for cpt_b in range(cpt_a-1):
            if table[cpt_b] > table[cpt_b+1]:
                temp = table[cpt_b]
                table[cpt_b] = table[cpt_b+1]
                table[cpt_b+1] = temp
    return table


def quick_sort(table):
    '''
    - FUNCTION
        -this function sorts a given table using the quick_sort
    - INPUT
        -table<list> : the table to sort
    - OUTPUT
        -table<list> : the table sorted
    '''
    if len(table) <= 1:
        return table
    else:
        table_a = []
        table_b = []
        pivot = table[0]
        for varI in range(1, len(table)):
            if (table[varI] > pivot):
                table_b.append(table[varI])
            else:
                table_a.append(table[varI])

        table_a = quick_sort(table_a)
        table_b = quick_sort(table_b)
        table = table_a + [pivot] + table_b
        return table


def merge(table_a, table_b):
    '''
    - FUNCTION
        -this function merges 2 tables
    - INPUT
        -table_a<list> : the first table to merge
        -table_b<list> : the second table to merge
    - OUTPUT
        -table<list> : the 2 tables merged
    '''
    if len(table_a) == 0:
        return table_b
    if len(table_b) == 0:
        return table_a
    if table_a[0] <= table_b[0]:
        return [table_a[0]] + merge(table_a[1:], table_b)
    else:
        return [table_b[0]] + merge(table_a, table_b[1:])


def merge_sort(table):
    '''
    - FUNCTION
        -this function sorts a given table using the merge_sort
    - INPUT
        -table<list> : the table to sort
    - OUTPUT
        -table<list> : the table sorted
    '''
    n = len(table)
    if n <= 1:
        return table
    return merge(merge_sort(table[0:int(n/2)]), merge_sort(table[int(n/2):n]))


def get_time(function, table_size):
    '''
    - FUNCTION
        -this function returns the time taken to execute a sort function
    - INPUT
        -function<string> : the name of the function to execute (must be in a dict)
        -table_size<int> : the size of the table to sort
    - OUTPUT
        -time_used<int> : the number of nanosecond taken to execute the function
    '''
    table = generate_random_table(table_size)
    time_used = time()
    function_dict[function](table)
    time_used = time() - time_used
    return time_used


def time_in_file(list_time_used, function, table_size):
    '''
    - FUNCTION
        -this function writes the time taken by a function in a file
    - INPUT
        -list_time_used<int> : time taken by the function to be executed
        -function<string> : the name of the function executed
        -table_size<int> : the size of the table to sort
    '''
    file_name = "benchmark_RV_"+str(function)+"_"+str(table_size)+".txt"
    with open(file_name, "w") as file:
        for cpt in list_time_used:
            file.write(str(cpt)+"\n")


def benchmark(function, table_size):
    '''
    - FUNCTION
        -this function writes the time taken by a function in a file
    - INPUT
        -time_used<int> : time taken by the function to be executed
        -function<string> : the name of the function executed
        -table_size<int> : the size of the table to sort
    '''
    list_time_used = []
    for _ in range(100):
        list_time_used.append(get_time(function, table_size))
    time_in_file(list_time_used, function, table_size)


function_dict = {
  "bubble_sort": bubble_sort,
  "quick_sort": quick_sort,
  "merge_sort": merge_sort
}
index_dict = {
  0: "bubble_sort",
  1: "quick_sort",
  2: "merge_sort"
}


def main():
    '''
    - FUNCTION
        -this function writes the time taken by a function in a file
    - INPUT
        -time_used<int> : time taken by the function to be executed
        -function<string> : the name of the function executed
        -table_size<int> : the size of the table to sort
    '''
    table_size = int(input("rentrez la taille du tableau à trier:"))
    for cpt in range(3):
        benchmark(index_dict[cpt], table_size)


if __name__ == '__main__':
    main()
