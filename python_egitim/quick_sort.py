def quick_sort(dizi:list):
    if len(dizi)<2:# özyineleme bitiş
        return dizi
    else:
        pivot=dizi[0]
        sol = [i for i in dizi[1:] if i<=pivot]
        sag = [i for i in dizi[1:] if i>pivot]
        return quick_sort(sol) + [pivot] + quick_sort(sag)

if __name__ == '__main__':
    dizi = [16,10,20,8,30,54,70,7,4,58]

    sirali=quick_sort(dizi)

    print(sirali,"quick sort")
