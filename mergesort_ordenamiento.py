import time
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Algoritmo de ordenamiento por inserción
def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

# Algoritmo de ordenamiento por mezcla (merge sort)
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def medir_tiempo(n):
    arr = list(range(n))
    random.shuffle(arr)

    arr1 = arr.copy()

    inicio = time.time()
    insertion_sort(arr)
    fin = time.time()

    inicio2 = time.time()
    merge_sort(arr1)
    fin2 = time.time()

    print(f"Insertion Sort: {fin - inicio:.6f} segundos")
    print(f"Merge Sort: {fin2 - inicio2:.6f} segundos")
    return fin - inicio, fin2 - inicio2

if __name__ == "__main__":
    dc_times = []
    bf_times = []
    input_sizes = [10, 50, 100, 200, 500, 1000]

    for n in input_sizes:
        dc_elapsed, bf_elapsed = medir_tiempo(n)
        dc_times.append(dc_elapsed)
        bf_times.append(bf_elapsed)

    sns.lineplot(x=input_sizes, y=dc_times, label="Divide y conquista", marker="o")
    sns.lineplot(x=input_sizes, y=bf_times, label="Fuerza bruta", marker="o")

    plt.xlabel("Tamaño de la entrada (N)")
    plt.ylabel("Tiempo transcurrido (s)")
    plt.title("Análisis del ordenamiento por mezcla vs ordenamiento por inserción")
    plt.grid(True)
    plt.legend()
    plt.show()