#Mulai
print("Exercise 9.2")
#Nama file : array3.py
print("Nama file : array3.py")
print("")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
print("Jawab :")
#Import sys

# mendefinisikan array asosiatif

KAMUS = {'one': 'satu','two':'dua','three':'tiga', 'four':'empat','five':'lina','six':'enam','seven':'tujuh',
'eight':'delapan','nine':'sembilan','ten':'sepuluh'
#....
}

def main():

    # meminta user memasukkan kata dalam bahasa inggris

    kata = input("Masukkan kata dalan bahasa inggris: ")

if not (kata in KAMUS.keys()):

    print("'%s' tidak ditemukan di dalam kasus ini" % kata)
    sys.exit(1)

    print("Arti kata '%s' adalah 's'"% (kata, KAMUS ))
if__name__=="__main__":
    main()