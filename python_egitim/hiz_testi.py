# eğer modüldeki belli kısımlar(def/class sınıf ve fonskiyonlar) kullanılacksa
# from modül_adi import fonk1,fonk2,class1,class2.....

# import selection_sort
# import quick_sort

# dizim =[5,7,2]

# sirali = selection_sort.selection_sort(dizim)
# print(sirali)
from selection_sort import selection_sort
from quick_sort import quick_sort
from random import randint
from datetime import datetime

if __name__ == '__main__':
    # test verileri oluştur
    listem = [randint(1, 1_000_000_000) for _ in range(20_000)]
    ssl = listem.copy()  # selection sort listesi
    hsl = listem.copy()
    psl = listem.copy()
    print(f"test {len(listem)} uzuznluktaki dizi ile başladı: ")
    # selection sort hız testi
    # ssBaslangic = datetime.now()
    # sirali = selection_sort(ssl)
    # ssBitis = datetime.now()
    # print("selection sort çalışma süresi:\t", ssBitis-ssBaslangic)
    # quick sort hız testi
    qsBaslangic = datetime.now()
    sirali = quick_sort(hsl)
    qsBitis = datetime.now()
    print("quick sort çalışma süresi:\t", qsBitis-qsBaslangic)

    # python built-in fonksiyon
    psBas = datetime.now()
    psl.sort()
    psBts= datetime.now()
    print("Built-in sort öalışöa süresi:\t",psBts-psBas)



