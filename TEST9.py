print("Masukkan buah yang ingin dibeli apa saja")
isi = []
a = set()
while True:
    buah = input("Masukkan buah : ").lower()
    if buah == "stop".lower():
        print("Jadi ada",len(isi),"macam buah yang harus dibeli Andi, yaitu:")
        break
    else:
        isi.append(buah)  

isi = sorted(isi)
for i in isi :
    if i not in a:
        a.add(i)            
        v = isi.count(i)
        print("ada",i,"sebanyak",v,"buah")



# test 9 yang kumpul milka ku upload biar gak kosong aja
