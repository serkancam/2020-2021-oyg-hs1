def enkb(dizi:list):
    enkyeri = 0 #indis yeri
    ekDeger = dizi[0]
    for i in range(1,len(dizi)):#n-1
        if dizi[i]<ekDeger:
            enkyeri=i
            ekDeger=dizi[i]
    return enkyeri

def selection_sort(dizi:list):
    sirali=[]
    for _ in range(len(dizi)):#n kere tekrar eder
        enkyeri = enkb(dizi)
        deger = dizi.pop(enkyeri)
        sirali.append(deger)
    return sirali    


if __name__=="__main__":
    dizi = [16,10,20,8,30,54,70,7,4,58]

    sirali=selection_sort(dizi)

    print(sirali)