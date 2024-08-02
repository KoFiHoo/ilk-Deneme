import random

# Oyuncular ve roller listelerini oluştur
oyuncular = []
roller = []

# Oyunun başına kaç kişi oynayacak?
oyuncu_sayisi = int(input("Kaç kişi oynayacak? "))

# Oyuncuların isimlerini al
for i in range(oyuncu_sayisi):
    isim = input(f"{i+1}. oyuncunun ismi: ")
    oyuncular.append(isim)

# Rol dağılımını al
roller_dict = {"köylü": 0, "doktor": 0, "gözcü": 0, "katil": 0}
for rol in roller_dict.keys():
    sayi = int(input(f"Kaç tane {rol} olacak? "))
    roller_dict[rol] = sayi

# Roller listesini oluştur
roller = (
    ["köylü"] * roller_dict["köylü"]
    + ["doktor"] * roller_dict["doktor"]
    + ["gözcü"] * roller_dict["gözcü"]
    + ["katil"] * roller_dict["katil"]
)
random.shuffle(roller)  # Roller rastgele dağıt

# Oyunculara rollerini ata
oyuncu_roller = list(zip(oyuncular, roller))

# Oyun döngüsü
while True:
    oylama_listesi = []
    oldurulen = None
    iyilestirilen = None
    katil = None

    print("\nTur başlıyor...")

    # Her oyuncunun sırası
    for i, (oyuncu, rol) in enumerate(oyuncu_roller):
        print(f"\n{oyuncu} ({rol}) sırada...")

        if rol == "köylü":
            print(f"{oyuncu} bir şey yapmıyor.")
        elif rol == "katil":
            hedef = input(f"{oyuncu}, kimi öldürmek istiyorsun? ")
            katil = oyuncu
            oldurulen = hedef
        elif rol == "doktor":
            hedef = input(f"{oyuncu}, kimi iyileştirmek istiyorsun? ")
            iyilestirilen = hedef
        elif rol == "gözcü":
            hedef = input(f"{oyuncu}, kimin rolünü görmek istiyorsun? ")
            for oyuncu_ad, oyuncu_rol in oyuncu_roller:
                if oyuncu_ad == hedef:
                    print(f"{hedef}'in rolü: {oyuncu_rol}")
                    break

    # Tur sonunda değerlendirme
    if oldurulen and oldurulen != iyilestirilen:
        print(f"{oldurulen} öldürüldü.")
        oyuncu_roller = [p for p in oyuncu_roller if p[0] != oldurulen]
    else:
        print("Kimse ölmedi.")

    # Oylama
    print("\nOylama zamanı...")
    for oyuncu in oyuncular:
        oy = input(f"{oyuncu}, kime oy veriyorsun? ")
        oylama_listesi.append(oy)

    # En çok oy alanı bul
    oy_sayilari = {oyuncu: oylama_listesi.count(oyuncu) for oyuncu in oyuncular}
    asilan = max(oy_sayilari, key=oy_sayilari.get)
    print(f"{asilan} asıldı.")
    oyuncu_roller = [p for p in oyuncu_roller if p[0] != asilan]

    # Oyun bitim koşulları
    katil_sayisi = sum(1 for p in oyuncu_roller if p[1] == "katil")
    diger_roller = len(oyuncu_roller) - katil_sayisi

    if katil_sayisi >= diger_roller:
        print("Katiller kazandı!")
        break
    elif katil_sayisi == 0:
        print("Köylüler kazandı!")
        break
