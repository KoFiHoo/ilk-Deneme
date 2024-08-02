import random

class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.is_alive = True

    def __str__(self):
        return f"{self.name}"

def get_player_count():
    while True:
        try:
            count = int(input("Kaç oyuncu var? "))
            if count < 4:
                print("Oyuncu sayısı en az 4 olmalıdır.")
            else:
                return count
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

def get_role_counts(player_count):
    roles = ['Köylü', 'Doktor', 'Gözcü', 'Vampir']
    role_counts = {}
    remaining = player_count

    for role in roles:
        while True:
            try:
                count = int(input(f"Kaç tane {role} olacak? (Kalan oyuncu: {remaining}) "))
                if count < 0 or count > remaining:
                    print("Geçersiz sayı. Kalan oyuncu sayısına uygun bir sayı girin.")
                else:
                    role_counts[role] = count
                    remaining -= count
                    break
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
    
    if remaining > 0:
        role_counts['Köylü'] += remaining

    return role_counts

def assign_roles(player_count, role_counts):
    players = []
    names = [input(f"{i + 1}. oyuncunun adını girin: ") for i in range(player_count)]
    roles = []

    for role, count in role_counts.items():
        roles.extend([role] * count)

    random.shuffle(roles)

    for i in range(player_count):
        players.append(Player(names[i], roles[i]))

    return players

def main():
    player_count = get_player_count()
    role_counts = get_role_counts(player_count)
    players = assign_roles(player_count, role_counts)

    print("\nOyuncular belirlendi. Oyun başlıyor...")

    game_over = False
    while not game_over:
        vampire_target = None
        doctor_target = None
        seer_target = None

        for player in players:
            if not player.is_alive:
                continue
            
            print(f"\n{player.name}'nin sırası ({player.role})")
            if player.role == 'Vampir':
                target_name = input("Öldürmek istediğiniz oyuncunun adını girin: ")
                vampire_target = target_name
            elif player.role == 'Doktor':
                target_name = input("İyileştirmek istediğiniz oyuncunun adını girin: ")
                doctor_target = target_name
            elif player.role == 'Gözcü':
                target_name = input("Rolüne bakmak istediğiniz oyuncunun adını girin: ")
                seer_target = target_name

        if vampire_target == doctor_target:
            print(f"\nDoktor, {vampire_target}'i iyileştirdi. Bu turda kimse ölmedi.")
        else:
            for player in players:
                if player.name == vampire_target:
                    player.is_alive = False
                    print(f"\n{vampire_target} öldü.")

        if seer_target:
            for player in players:
                if player.name == seer_target:
                    print(f"\n{seer_target} rolü: {player.role}")

        alive_vampires = [p for p in players if p.role == 'Vampir' and p.is_alive]
        alive_villagers = [p for p in players if p.role != 'Vampir' and p.is_alive]

        if not alive_vampires:
            print("Köylüler kazandı!")
            game_over = True
        elif len(alive_vampires) >= len(alive_villagers):
            print("Vampirler kazandı!")
            game_over = True

if __name__ == "__main__":
    main()
