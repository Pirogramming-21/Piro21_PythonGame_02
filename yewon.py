import random

class Player:
    def __init__(self, name, capacity, is_user=False):
        self.name = name
        self.capacity = capacity
        self.current_drinks = 0
        self.is_user = is_user

    def drink(self):
        self.current_drinks += 1

    def drinks_left(self):
        return self.capacity - self.current_drinks

    def is_intoxicated(self):
        return self.current_drinks >= self.capacity

    def make_move(self, number):
        if self.is_user:
            return input(f"{self.name}: ").strip()
        else:
            return self.auto_move(number)

    def auto_move(self, number):
        if '3' in str(number) or '6' in str(number) or '9' in str(number):
            clap_count = str(number).count('3') + str(number).count('6') + str(number).count('9')
            return '짝' * clap_count
        else:
            return str(number)

def intro():
    print("게임을 진행할까요? (y/n)")
    choice = input().strip().lower()
    if choice == 'y':
        return True
    else:
        print("게임이 종료되었습니다.")
        return False

def get_user_info():
    name = input("오늘 첫 차 탈 당신의 이름은? ").strip()
    while True:
        print("소주 기준 당신의 주량은? 1. 2잔, 2. 4잔, 3. 6잔, 4. 8잔, 5. 9잔")
        try:
            capacity_choice = int(input().strip())
            if capacity_choice in [1, 2, 3, 4, 5]:
                capacities = [2, 4, 6, 8, 9]
                return name, capacities[capacity_choice - 1]
            else:
                print("올바른 선택을 해주세요.")
        except ValueError:
            print("올바른 선택을 해주세요.")

def invite_players():
    player_names = ["은서", "하연", "연서", "예진", "헌도"]
    players = []
    print("몇 명을 초대하시겠습니까? (최대 3명)")
    while True:
        try:
            num_players = int(input().strip())
            if 0 <= num_players <= 3:
                break
            else:
                print("0에서 3사이의 숫자를 입력하세요.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")
    
    random.shuffle(player_names)
    for i in range(num_players):
        name = player_names[i]
        capacity = random.choice([2, 4, 6, 8, 9])
        player = Player(name, capacity)
        players.append(player)
        print(f"{name}의 주량은 {capacity}잔입니다.")

    return players

def display_players(players):
    for player in players:
        print(f"{player.name} 지금까지 마신 잔 수 {player.current_drinks} / 치사량까지 {player.drinks_left()}")

def show_game_list():
    print("게임 리스트")
    print("1. 게임1")
    print("2. 369 게임")
    print("3. 게임3")
    print("4. 게임4")

def play_369(players):
    number = 1
    while True:
        for player in players:
            print(f"{player.name}님의 차례입니다.")
            expected = player.auto_move(number) if not player.is_user else None
            response = player.make_move(number)
            
            # 출력
            if not player.is_user:
                print(f"{player.name}: {response}")
            
            # 응답 확인
            if expected is None:
                if ('3' in str(number) or '6' in str(number) or '9' in str(number)) and response != '짝' * (str(number).count('3') + str(number).count('6') + str(number).count('9')):
                    print(f"{player.name}님이 졌습니다!")
                    player.drink()
                    display_players(players)
                    if player.is_intoxicated():
                        return
                    return
                elif not ('3' in str(number) or '6' in str(number) or '9' in str(number)) and response != str(number):
                    print(f"{player.name}님이 졌습니다!")
                    player.drink()
                    display_players(players)
                    if player.is_intoxicated():
                        return
                    return
            else:
                if response != expected:
                    print(f"{player.name}님이 졌습니다!")
                    player.drink()
                    display_players(players)
                    if player.is_intoxicated():
                        return
                    return
            
            number += 1

def play_game(players):
    while True:
        display_players(players)
        show_game_list()
        try:
            game_choice = int(input("게임을 선택하세요: ").strip())
            if game_choice == 2:
                play_369(players)
                break
            else:
                print("해당 게임은 아직 구현되지 않았습니다.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

def random_game_choice():
    return random.choice([1, 2, 3, 4])

def main():
    if not intro():
        return

    user_name, user_capacity = get_user_info()
    user = Player(user_name, user_capacity, is_user=True)
    players = [user] + invite_players()

    while True:
        play_game(players)
        for player in players:
            if player.is_intoxicated():
                print(f"{player.name}님이 치사량에 도달했습니다!")
                display_players(players)
                print("게임이 종료되었습니다.")
                return

        non_user_players = [player for player in players if player != user]
        random.shuffle(non_user_players)
        for player in non_user_players:
            print(f"{player.name}님의 차례입니다. 게임을 랜덤으로 선택합니다.")
            random_game = random_game_choice()
            print(f"선택된 게임: {random_game}")
            if random_game == 2:
                play_369(players)
            else:
                print("해당 게임은 아직 구현되지 않았습니다.")
            if any(p.is_intoxicated() for p in players):
                break

        if any(p.is_intoxicated() for p in players):
            print("게임이 종료되었습니다.")
            break

if __name__ == "__main__":
    main()