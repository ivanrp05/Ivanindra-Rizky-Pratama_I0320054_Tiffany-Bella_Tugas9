#Mulai
print("")
print("Exercise 9.11")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
print("Jawab :")
#mendefinisikan fungsi untuk mengurutkan elemen array
def sort (A) :
    i = 0
    while i < len(A)-1 :
        j = len (A) - 1
        while J >= i+1:
            if A[j] < A[j-1] :
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
            j -= 1
        i += 1
def main():
    A = array.array ('i', [50,10,30,40,20])
    print("Sebelum diurutkan : ")
    for nilai in A :
        print("%d" % nilai, end ='')
    print("\n")

print("Alhamdulillah sudah selesai")
input("Klik enter untuk keluar.....")