import numpy as np
'''
numpy yang sudah / akan digunakan:
1. np.linalg.det()
2. np.sqrt()
3. np.dot()
4. np.asin()
5. np.acos()
'''

# helper function

def hitungDet(matrix):
    det = np.linalg.det(matrix)
    return det

def tampilkanMatrix(matrix): # menampilkan matrix yang ingin ditampilkan
    for row in matrix:
        atur = ["{:.2f}".format(x) for x in row]
        print("    [" + ", ".join(atur) + "]")

def tampilkanMatrix1D(v):
    print("[", end = '')
    print(", ".join(f"{x:.2f}" for x in v), end = '')
    print(']')

def displayInput(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    V{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def displayInput6(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    U{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def displayInput7(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    W{i+1} =")
        tampilkanMatrix(v)
        print()

def radToDeg(res):
    ans = res * (180 / np.pi)
    return ans

# spesific function
def displayInput3(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    P{i+1} =", end=' ')
        tampilkanMatrix1D(v)
        print()

def displayInput8(vectors):
    # tampilkan semua matrix
    for i, v in enumerate(vectors):
        print(f"    T{i+1} =", end = ' ')
        tampilkanMatrix1D(v)
        print()

def crossProductDeterminant(Uvectors, Vvectors):
    print("\n=== Kamu memilih operasi cross product ===\n")
    print("Vektor input:\n")

    displayInput6(Uvectors)
    displayInput(Vvectors)

    # error message kalo ukuran tidak 3
    # if len(Uvectors) != 3 or len(Vvectors):
    #     print(f"Tidak dapat menghitung cross product karena salah satu ukuran tidak 3\n")
    #     return

    print("=== Hasil cross product menggunakan determinan ===\n")
    for i, Uvec in enumerate(Uvectors):
        for j, Vvec in enumerate(Vvectors):
            U = Uvec
            V = Vvec

            if len(U) != len(V) or len(U) > 3 or len(V) > 3:
                print(f"Panjang dari vektor U berbeda dengan vektor V. Len(U) = {len(U)} sedangkan len(V) = {len(V)}")
                print("U x V terdefinisi hanya pada vektor dimensi 3 saja")

            W1 = []
            for k in range(2):
                W1.append([])
                AppendA = U[1] if k == 0 else V[1]
                AppendB = U[2] if k == 0 else V[2]
                W1[k].append(AppendA)
                W1[k].append(AppendB)

            W2 = []
            for k in range(2):
                W2.append([])
                AppendA = U[0] if k == 0 else V[0]
                AppendB = U[2] if k == 0 else V[2]
                W2[k].append(AppendA)
                W2[k].append(AppendB)

            W3 = []
            for k in range(2):
                W3.append([])
                AppendA = U[0] if k == 0 else V[0]
                AppendB = U[1] if k == 0 else V[1]
                W3[k].append(AppendA)
                W3[k].append(AppendB)

            W = [W1, W2, W3]

            print(f"-----------------------------------------------------------------------")
            print(f"|========================== Operasi U{i+1} X V{j+1} ==========================|")
            print(f"-----------------------------------------------------------------------\n")

            print(f"====| Rumus1 U{i+1} X V{j+1} = [det(W1), -det(W2), det(W3)] |====\n")
            print("    Vektor W yang terbentuk adalah:\n")
            displayInput7(W)

            kalkulasi = []
            kalkulasi.append([])

            # detW1 = 0
            # detW2 = 0
            # detW3 = 0
            detW = [0, 0, 0]

            for k in range(3):
                detW[k] += hitungDet(W[k])
                kalkulasi[0].append(f"[({W[k][0][0]:.2f}) * ({W[k][1][1]:.2f})] - [({W[k][1][0]:.2f}) * ({W[k][0][1]:.2f})]")

            detW[1] *= -1

            # print(f"    Determinan W1 = " + " + ".join(kalkulasi[0][0]))
            # print(f"    Determinan W1 = {detW[0]}")
            # print(f"    Determinan W1 = " + " + ".join(kalkulasi[0][1]))
            # print(f"    Determinan W2 = {detW[1]}")
            # print(f"    Determinan W1 = " + " + ".join(kalkulasi[0][2]))
            # print(f"    Determinan W3 = {detW[2]}\n")

            for k, detK in enumerate(detW):
                print(f"    Determinan W{k+1} = {kalkulasi[0][k]}")
                print(f"    Determinan W{k+1} = {detK:.2f}")
                print()

            print(f"    Sehingga hasil U{i+1} X V{j+1} =", end = ' ')
            tampilkanMatrix1D(detW)
            print()
            print(f"==== Rumus2 ||U{i+1} X V{j+1}|| = sqrt(W1^2 + W2^2 + W3^2) ====\n")

            kalkulasi.append([])
            ans = 0
            for k, w in enumerate(detW):
                kalkulasi[0].append(f"({w:.2f})^2")
                ans += pow(w, 2)
            
            ans = np.sqrt(ans)

            print(f"    Hasil ||U{i+1} X V{j+1}|| = sqrt[" + " + ".join(kalkulasi[1]) + "]")
            print(f"    Hasil ||U{i+1} X V{j+1}|| = {ans:.2f}\n")

            print(f"==== Rumus3 menentukan theta dari ||U{i+1} X V{j+1}|| = ||U|| dot ||V|| * sin(theta) ====\n")

            res = 0.00
            lengU = 0.00
            lengV = 0.00
            
            for k in U:
                lengU += pow(k, 2)

            lengU = np.sqrt(lengU)

            for k in V:
                lengV += pow(k, 2)

            lengV = np.sqrt(lengV)

            resRad = np.asin(ans / (lengU * lengV))

            resDeg = radToDeg(resRad)

            kalkulasi.append([])
            kalkulasi[1].append(f"({lengU:.2f}) * ({lengV:.2f}) * sin(theta)")
            kalkulasi[1].append(f"asin[{ans:.2f} / (({lengU:.2f}) * ({lengV:.2f}))]")

            print(f"    Hasil ||U{i+1} X V{j+1}|| = {kalkulasi[1][0]}")
            print(f"    Hasil theta = {kalkulasi[1][1]}\n")
            print(f"    Theta = {resRad:.2f} Rad")
            print(f"    Theta = {resDeg:.2f} Deg\n")

def hitungLSegitiga(vectorsP):
    print("\n=== Kamu memilih operasi hitung luas segitiga Product ===\n")
    print("Vektor input:\n")

    displayInput3(vectorsP)
    
    leng = len(vectorsP)
    for i in range(leng):
        pusat = vectorsP[i]

        print(f"=== Luas segitiga dengan pusat P{i+1} ===\n")

        P1 = vectorsP[(i+1) % leng]
        P2 = vectorsP[(i+2) % leng]

        PP1 = np.array(P1) - np.array(pusat)
        PP2 = np.array(P2) - np.array(pusat)
        
        crossP = np.cross(PP1, PP2)
        lengPP = np.linalg.norm(crossP)

        lengPP = np.sqrt(lengPP)

        luas = 0.5 * (lengPP)

        idxP1 = (i+1) % leng
        idxP2 = (i+2) % leng
        print(f"    Rumus luas segitiga = 0.5 * ||P{i+1}P{idxP1+1} X P{i+1}P{idxP2+1}||")
        print(f"    Hasil luas segitiga = {luas:.2f}\n")

def persBdgMll1Ttk(titik, nVal):
    print("\n=== Kamu memilih operasi hitung persamaan bidang melalui 1 titik ===\n")
    print("Vektor input:\n")

    print(f"    Titik =", end = ' ')
    tampilkanMatrix1D(titik)
    print(f"    Tegak lurus terhadap n =", end = ' ')
    tampilkanMatrix1D(nVal)
    print()

    constanta = 0.00
    for i in range(3):
        constanta += ((titik[i] * -1) * nVal[i])

    print(f"Rumus: P0P * n = 0")
    print(f"Persamaannya: ({nVal[0]:.2f})X + ({nVal[1]:.2f})Y + ({nVal[2]:.2f})Z + ({constanta:.2f}) = 0\n")

def persBdgMll3Ttk(Tvec):
    print("\n=== Kamu memilih operasi hitung persamaan bidang melalui 3 titik ===\n")
    print("Vektor input:\n")

    displayInput8(Tvec)

    leng = len(Tvec)
    for i, pusat in enumerate(Tvec):
        P1 = Tvec[(i+1) % leng]
        P2 = Tvec[(i+2) % leng]

        PP1 = np.array(P1) - np.array(pusat)
        PP2 = np.array(P2) - np.array(pusat)

        crossPP = np.cross(PP1, PP2)

        constanta = 0.00
        for j in range(3):
            constanta += ((pusat[j] * -1) * crossPP[j])

        print(f"Persamaan bidang dengan P0 = P{i+j}:\n")
        print(f"    Rumus: P0P * n")
        print(f"    Persamaan: ({crossPP[0]:.2f})X + ({crossPP[1]:.2f})Y + ({crossPP[2]:.2f})Z + ({constanta:.2f}) = 0\n")


# main driver 
def main():
    opsi = 4

    U1 = [1, 2, 3]
    U2 = [73, 63, 9]
    U3 = [-7, -9, 10]

    V1 = [4, 5, 6]
    V2 = [2, -7, 9]
    V3 = [102, -87, -90]

    vectorsU = [U1, U2, U3]
    vectorsV = [V1, V2, V3]

    P1 = [9, 201, -29]
    P2 = [2, -8, -13]
    P3 = [1, 2, 3]

    vectorsP = [P1, P2, P3]

    titik = [3, -1, 7]
    nVal = [4, 2, -5]

    T1 = [-3, 2, 0]
    T2 = [0, -1, 2]
    T3 = [5, 1, 3]

    Tvec = [T1, T2, T3]

    match opsi:
        case 1:
            # exit kalo ukuran tidak sama dengan 3
            if len(Uvectors) != 3 or len(Vvectors):
                print(f"Tidak dapat menghitung cross product karena salah satu ukuran tidak 3\n")
                return

            crossProductDeterminant(vectorsU, vectorsV)
        case 2:
            # exit kalo ukuran tidak sama dengan 3
            if len(vectorsP[0]) != 3 or len(vectorsP[1]) != 3 or len(vectorsP[2]) != 3:
                print(f"Tidak dapat menghitung luas segitiga karena salah satu ukuran tidak 3\n")
                return
            
            hitungLSegitiga(vectorsP)
        case 3:
            # exit kalo ukuran tidak sama dengan 3
            if len(titik) != 3 or len(nVal) != 3:
                print(f"Tidak dapat menghitung persamaan karena salah satu ukuran tidak 3\n")
                return
            
            persBdgMll1Ttk(titik, nVal)

        case 4:
            # exit kalo ukuran tidak sama dengan 3
            if len(Tvec[0]) != 3 or len(Tvec[1]) != 3 or len(Tvec[2]) != 3 or len(Tvec) != 3:
                print(f"Tidak dapat menghitung persamaan karena salah satu ukuran tidak 3\n")
                return
            
            persBdgMll3Ttk(Tvec)

"""
int main(int argv, char **argv) {
    return 0;
}
"""

if __name__ == "__main__":
    main()
    