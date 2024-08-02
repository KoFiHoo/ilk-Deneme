def kelime_zinciri_oyunu():
    print("Kelime Zinciri Oyununa Hoş Geldiniz!")
    print("Kurallar: Bir kelime söyleyin, bir sonraki oyuncu önceki kelimenin son harfiyle başlayan bir kelime söylemeli. 'bitir' yazarak oyunu bitirebilirsiniz.")

    oyuncu_sira = 1
    oyuncu1_puan = 0
    oyuncu2_puan = 0
    son_kelime = ""
    
    while True:
        if oyuncu_sira % 2 != 0:
            oyuncu = "1. Oyuncu"
            oyuncu_puan = oyuncu1_puan
        else:
            oyuncu = "2. Oyuncu"
            oyuncu_puan = oyuncu2_puan
        
        kelime = input(f"{oyuncu}, kelimenizi girin: ").lower()
        
        if kelime == "bitir":
            print("Oyun bitti!")
            break
        
        if oyuncu_sira > 1:
            if kelime[0] != son_kelime[-1]:
                print(f"Hatalı giriş! {kelime} kelimesi, {son_kelime[-1]} harfiyle başlamalı.")
                continue
        
        son_kelime = kelime
        oyuncu_sira += 1
        
        if oyuncu == "1. Oyuncu":
            oyuncu1_puan += 1
        else:
            oyuncu2_puan += 1
    
    print("Oyun Sonu! Puanlar:")
    print(f"1. Oyuncu: {oyuncu1_puan} puan")
    print(f"2. Oyuncu: {oyuncu2_puan} puan")

kelime_zinciri_oyunu()
