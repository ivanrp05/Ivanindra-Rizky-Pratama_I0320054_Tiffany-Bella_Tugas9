#Mulai
print("Exercise 9.1")
#Nama file : array2.py
print("Nama file : array2.py")
print("")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
print("Jawab :")
import sys
#mendefinisikan array konstan
HARI : ('Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu')

def main():

# meminta user memasukkan nomor hari
nohari = int(input("Masukkan nomor hari [1..7]: "))

if (nohari < 1) or (nohari > 7):
    print("Tidak ada hari ke-%s" % nohari)

sys.exit(1)

print("Hari ke-%d adalah %s" % (nohari, HARI[nohari-1]))

if __name__== "__main__":
    main()