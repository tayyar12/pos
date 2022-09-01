import time
baslangicparasi =5000
print(f"bankanızdaki para : {baslangicparasi}  ")
time.sleep(3)


cekilecek= int(input("çekilecek tutar: "))

def cekmeislem (baslangicparasi , cekilecek):
        print("isleminiz basarılı")
        time.sleep(2)
        kalan = baslangicparasi - cekilecek
        print(f"kalan paranız {kalan} lira")
        time.sleep(2)
        print("iyi günler...")

    

if baslangicparasi > cekilecek:
    cekmeislem(baslangicparasi,cekilecek)
else:
    time.sleep(3)
    print("yetersiz bakiye")


