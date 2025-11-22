# file dari obeInvers.py

import numpy as np

# fungsi
def cheksDets(M):
    D = np.linalg.det(M)
    return D

def printMatrix(M):
    for row in M:
        formatted = ["{:.2f}".format(x) for x in row]
        print("   [" + ", ".join(formatted) + "]")
    print()

def gaussStep(matrix4, B):
    n = len(matrix4)
    A = [row[:] for row in matrix4]   # salin matriks
    step = 1

    print("Proses Eliminasi Gauss-Jordan:\n")
    
    for i in range(n):
        pivot = A[i][i]

        # Jika pivot = 0, cari baris lain untuk swap
        if pivot == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    print(f"Iterasi-{step}: Tukar R{i+1} <-> R{k+1}")
                    A[i], A[k] = A[k], A[i]
                    B[i], B[k] = B[k], B[i]
                    print("Matriks A menjadi:")
                    printMatrix(A)
                    print("Matriks invers A menjadi:")
                    printMatrix(B)
                    step += 1
                    pivot = A[i][i]
                    break

        # Jika tetap 0 maka lanjut (tidak bisa normalisasi)
        if pivot == 0:
            continue

        # Normalisasi pivot: jadikan 1
        print(f"Iterasi-{step}: Normalisasi R{i+1} (bagi {pivot:.2f})")
        for c in range(len(A[0])):
            A[i][c] /= pivot
            B[i][c] /= pivot
        print("Matriks A menjadi:")
        printMatrix(A)
        print("Matriks invers A menjadi:")
        printMatrix(B)
        step += 1

        # Eliminasi ke semua baris lain (Gauss-Jordan)
        for r in range(n):
            if r == i:
                continue
            if A[r][i] == 0:
                continue

            factor = A[r][i]
            print(f"Iterasi-{step}: R{r+1} = R{r+1} - ({factor:.2f}) * R{i+1}")

            for c in range(len(A[0])):
                A[r][c] -= factor * A[i][c]
                B[r][c] -= factor * B[i][c]
            print("Matriks A menjadi:")
            printMatrix(A)
            print("Matriks invers A menjadi:")
            printMatrix(B)
            step += 1

    return A, B

def showStep(matrix4):
    print("Matriks A:")
    printMatrix(matrix4)
    row = len(matrix4)  
    col = len(matrix4)

    if row != col:  # determinan tidak berlaku
        print("Matriks A tidak memiliki invers")
        return

    checkDet = cheksDets(matrix4)
    if checkDet == 0:  # determinan harus != 0
        print("Matriks A tidak memiliki invers")
        return 
    else:
        B = []
        for i in range (row):
            B.append([])  # buat matriks identitas
            for j in range (col):
                if i == j:
                    B[i].append(1)
                else:
                    B[i].append(0)
    
    matrix4, B = gaussStep(matrix4, B)

    print("Matriks A akhir:")
    printMatrix(matrix4)
    print("Matriks invers A adalah:")
    printMatrix(B)

# Pemanggilan fungsi

A1 = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3],
]

A = [
    [2, 3, 1, 4],
    [1, 0, -1, 2],
    [3, 1, 2, 0],
    [2, 4, 1, 3]
]

B = [
    [2,  3,  1],
    [4, -1,  2],
    [5,  0,  3]
]

C = [
    [2, 1],
    [5, 3]
]

# Matriks tidak persegi
D = [
    [1, 3, 2],
    [4, 6, 5]
]

print("=== Matriks Invers A dengan Gauss-Jordan OBE ===\n")
showStep(C)
