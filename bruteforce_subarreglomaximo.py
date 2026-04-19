import random
import time
import matplotlib.pyplot as plt
import seaborn as sns

def max_crossing_subarray(arr, low, mid, high):
    left_sum = float("-inf")
    suma = 0
    max_left = mid

    for i in range(mid, low-1, -1):
        suma = suma + arr[i]
        if suma > left_sum:
            left_sum = suma
            max_left = i
    
    right_sum = float("-inf")
    suma = 0
    max_right = mid + 1

    for j in range(mid+1, high+1):
        suma = suma + arr[j]
        if suma > right_sum:
            right_sum = suma
            max_right = j
    
    return max_left, max_right, left_sum + right_sum


def max_subarray_divide_conquer(arr, low, high):
    # Caso base
    if low == high:
        return low, high, arr[low]

    mid = (low + high ) // 2 

    # 1. La mitad izquierda -> Recursiva
    left_low, left_high, left_sum = max_subarray_divide_conquer(arr, low, mid)
    # 2. La mitad derecha -> Recursiva
    right_low, righ_high, right_sum = max_subarray_divide_conquer(arr, mid+1, high)
    # 3. Un subarreglo que atraviesa la mitad -> Lineal
    cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, righ_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

def max_subarray_bruteforce(arr):
    max_sum = float("-inf")
    inicio = 0
    fin = 0

    for i in range(len(arr)):
        suma_actual = 0
        for j in range(i, len(arr)):
            suma_actual = suma_actual + arr[j]

            if suma_actual > max_sum:
                max_sum = suma_actual
                inicio = i
                fin = j
    return inicio, fin, max_sum

def medir_tiempo(n):
    arr = list(range(-n,n))
    random.shuffle(arr)

    arr1 = arr.copy()

    inicio_t1 = time.time()
    inicio, fin, max_sum = max_subarray_divide_conquer(arr, 0, len(arr)-1)
    print(f"El subarreglo con la suma máxima por el metodo de divide-conquista es: {arr[inicio:fin+1]} con suma {max_sum}")
    fin_t1 = time.time()

    inicio_t2 = time.time()
    inicio2, fin2, max_sum2 = max_subarray_bruteforce(arr1)
    print(f"El subarreglo con la suma máxima por el metodo de fuerza bruta es: {arr[inicio2:fin2+1]} con suma {max_sum2}")
    fin_t2 = time.time()

    print(f"Divide y conquista: {fin_t1 - inicio_t1:.2f} segundos")
    print(f"Fuerza bruta: {fin_t2 - inicio_t2:.2f} segundos")
    return fin_t1 - inicio_t1, fin_t2 - inicio_t2

if __name__ == "__main__":
    tiempos_divide_conquista = []
    tiempos_fuerza_bruta = []
    datos = [10,50,100,200,500,1000]

    for i,n in enumerate(datos):
        tiempo_divide_conquista, tiempo_fuerza_bruta  = medir_tiempo(n)
        tiempos_divide_conquista.append(tiempo_divide_conquista)
        tiempos_fuerza_bruta.append(tiempo_fuerza_bruta)
    
    sns.lineplot(x=datos, y=tiempos_divide_conquista, label="Divide y conquista", markers="o")
    sns.lineplot(x=datos, y=tiempos_fuerza_bruta, label="Fuerza bruta", markers="o")
    plt.xlabel("Cantidad de datos (N)")
    plt.ylabel("Complejidad temporal (s)")
    plt.title("Analisis de la complejidad temporal del problema de maximo subarreglo")
    plt.grid(True)
    plt.legend()
    plt.show()

