def kelime_zinciri_oyunu():
    print("Kelime Zinciri Oyununa Hoş Geldiniz!")
    print("Kurallar: Bir kelime söyleyin, bir sonraki oyuncu önceki kelimenin son harfiyle başlayan bir kelime söylemeli. 'bitir' yazarak oyunu bitirebilirsiniz.")

    oyuncu_sira = 1
    son_kelime = ""
    
    while True:
        if oyuncu_sira % 2 != 0:
            oyuncu = "1. Oyuncu"
        else:
            oyuncu = "2. Oyuncu"
        
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

kelime_zinciri_oyunu()
