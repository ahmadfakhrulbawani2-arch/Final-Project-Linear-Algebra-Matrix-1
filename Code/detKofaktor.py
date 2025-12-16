# file dari detKofaktor.py
import numpy as np

def calcDet(A):
    D = np.linalg.det(A)
    return D


def printMatrix(M):
    for row in M:
        formatted = ["{:.2f}".format(x) for x in row]
        print("   [" + ", ".join(formatted) + "]")
    print()


def minor(matrix, row, col):
    m = []
    
    for i in range(len(matrix)):
        if i == row:
            continue  

        new_row = []  

        for j in range(len(matrix)):
            if j == col:
                continue  

            new_row.append(matrix[i][j])

        m.append(new_row)

    return m


def showStep(matrix):
    n = len(matrix)
    c = len(matrix[0])

    # Cetak matriks awal
    print("Matriks A:")
    printMatrix(matrix)

    if n == c:
        print(f"Ekspansi kofaktor untuk matriks A {n}x{n}:\n")

        print("Ekspansi baris pertama (baris 0):\n")

        terms = []
        det = 0

        for j in range(n):
            sign = pow(-1, (0 + j))
            a = matrix[0][j]

            print(f"Elemen A[0][{j}] = {a}")
            if sign > 0:
                print("Tanda: positif")
            else:
                print("Tanda: negatif")

            # Minor
            M = minor(matrix, 0, j)
            print(f"Minor M_0{j}:")
            printMatrix(M)

            terms.append(f"({sign} * {a} * det(M_0{j}))")
            detTmp = sign * a * calcDet(M)
            det += detTmp

        print("Ekspansi lengkap determinan:\n")
        print("det(A) = " + " + ".join(terms))
        print()
        print(f"Determinannya = {det:.2f}")
        print()
    else:
        print(f"Maaf, determinan tidak berlaku untuk matriks {n} x {c}")
        print("Silakan masukkan matriks persegi (n x n) untuk menghitung determinan.\n")


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

E = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72],
    [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83 ,84],
    [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96],
    [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108],
    [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
    [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132],
    [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144],
]

F = [
    [7, 0, 9]
]

print("\n=== Determinan dengan Ekspansi Kofaktor ===\n")
showStep(E)
# showStep(B)
