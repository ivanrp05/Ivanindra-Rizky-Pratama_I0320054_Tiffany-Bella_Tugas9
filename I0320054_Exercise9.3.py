#Mulai
print("Exercise 9.3")
#Nama file : array4.py
print("Nama file : array4.py")
print("")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
print("Jawab :")
A = [
    [23,11,54,38,76],
    [14,12,20,22,21],
    [10,13,18,17,24],
    [35,33,39,32,29]
]
BARIS = 4
KOLOM = 4
def main () :
    print("isi array A :")
    #menampilkan elemen array dua dimensi
    i = 0 ;
    while i < BARIS:
        j = 0
        while j < KOLOM :
            print("%d"%A[i][j], end = '')
            j += 1
        i += 1
        print() # ganti baris
if __name__ == "__main__":
    main()
print("Selesai, mohon maaf apabila terdapat kesalahan")
input("Klik enter untuk keluar...")

