#Mulai
print("")
print("Exercise 9.8")
print("Nama : Ivanindra Rizky P")
print("NIM : I0320054")
print("")
print("===========================")
print("")
print("Jawab :")
>>> #mengonversi list ke dalam array.array
>>> li = [10,20,30,40,50]
>>> C = array.array('i')
>>> C.fromlist (li)
>>> type(C)
<type 'array.array'>
>>> for nilai in C:
    print("%d " % nilai, end ='')
    
10 20 30 40 50
>>>