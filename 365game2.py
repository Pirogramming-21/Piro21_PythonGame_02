# import random

# class Player:
#     def __init__(self, name, is_user=False):
#         self.name = name
#         self.is_user = is_user

#     def make_move(self, number):
#         if self.is_user:
#             return input(f"{self.name}: ").strip()
#         else:
#             return self.auto_move(number)
    
#     def auto_move(self, number):
#         if random.random() < 0.3:  # 30% chance of providing an incorrect response
#             return self.generate_incorrect_response(number)
#         else:
#             if '3' in str(number) or '6' in str(number) or '9' in str(number):
#                 clap_count = str(number).count('3') + str(number).count('6') + str(number).count('9')
#                 return '짝' * clap_count
#             else:
#                 return str(number)
    
#     def generate_incorrect_response(self, number):
#         incorrect_number = random.randint(1, number + 10)  # Generate a random incorrect number
#         return str(incorrect_number)

# def play_369(players):
#     number = 1
#     while True:
#         for player in players:
#             expected = player.auto_move(number) if not player.is_user else None
#             response = player.make_move(number)
            
#             # Output the response
#             if not player.is_user:
#                 print(f"{player.name}: {response}")
            
#             # Check for incorrect responses
#             if not player.is_user and expected is not None and response != expected:
#                 print(f"{player.name}님이 졌습니다!")
#                 return
            
#             number += 1

# if __name__ == "__main__":
#     user_name = input("당신의 이름을 입력하세요: ").strip()
#     user = Player(user_name, is_user=True)
#     other_names = ["참가자 2", "참가자 3"]
#     random.shuffle(other_names)
#     other_players = [Player(name) for name in other_names]
#     players = [user] + other_players
#     random.shuffle(players)
    
#     play_369(players)
    
#     input("게임이 종료되었습니다. 엔터 키를 누르면 프로그램이 종료됩니다.")


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

    def random_incorrect_move(self, number):
        if '3' in str(number) or '6' in str(number) or '9' in str(number):
            return str(number)
        else:
            return '짝'

def intro():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                    □□□□□■■□□□□□□□□□□□□■■□■□□□■■■■■□□■■ ")
    print("                    □□□□■■■■□□□□□■■■■■□■■□■□□■■■■■■■□■■ ")
    print("                    □□■■■■■■■■□□□□□□■■□■■□■□□■■□□□■■□■■")
    print("                    □■■■■□□■■■■□□□□□■■□■■□■□□■■□□□■■□■■")
    print("                    □□□□□□□□□□□□□□□□■■■■■□■□□■■■■■■■□■■")
    print("                    ■■■■■■■■■■■■□□□■■■□■■□■□□□■■■■■□□■■")
    print("                    □□□□□■■□□□□□□□■■■□□■■□■□□□□□□□□□□□□")
    print("                    □□■■■■■■■■□□□■■■□□□■■□■□□□□■■■■■■■■")
    print("                    □□□□□□□□□■□□■■■□□□□■■□■□□□□■□□□□□■■")
    print("                    □□■■■■■■■■■□□□□□□□□□■■□■□□□□■□□□□□■■")
    print("                    □□■■□□□□□□□□□□□□□□□■■□■□□□□■□□□□□■■")
    print("                    □□■■■■■■■■■□□□□□□□□■■□■□□□□■■■■■■■■")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("        🍤안주🍤 먹을 시간이 없어요~❌ 마시면서 배우는 🍻 술❗게❗임❗🍻")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("🍻🎼소주 한 잔 할래요~~🎼🍻(y/n)")
    choice = input().strip().lower()
    if choice == 'y':
        return True
    else:
        print("게임이 종료되었습니다.")
        return False

def get_user_info():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    name = input("😵오늘 첫 차 탈 당신의 이름은?😵").strip()
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~🥃소주 기준 당신의 주량(치사량)은?🥃~~~~~~~~~~~~~~~~~~~~~~~~")
        print("                                🥃 1. 2잔")
        print("                                🥃 2. 4잔")
        print("                                🥃 3. 1병")
        print("                                🥃 4. 1병 반")
        print("                                🥃 5. 2병")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("위의 선택지에서 숫자를 선택하세요")
        try:
            capacity_choice = int(input().strip())
            if capacity_choice in [1, 2, 3, 4, 5]:
                capacities = [2, 4, 6, 8, 9]
                return name, capacities[capacity_choice - 1]
            else:
                print("1~5 중 하나를 선택해주세요.")
        except ValueError:
            print("1~5 중 하나를 선택해주세요.")

def invite_players():
    player_names = ["은서", "하연", "연서", "예진", "헌도"]
    players = []
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("👨‍👩‍👧 몇 명을 초대하시겠습니까? (최대 3명) 👨‍👩‍👧")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        try:
            num_players = int(input().strip())
            if 0 <= num_players <= 3:
                break
            else:
                print("0에서 3 사이의 숫자를 입력하세요.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")
    
    random.shuffle(player_names)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(num_players):
        name = player_names[i]
        capacity = random.choice([2, 4, 6, 8, 9])
        player = Player(name, capacity)
        players.append(player)
        print(f"🤗 안녕? 난 {name}(이)고, 내 주량은 🥃 {capacity}잔이야 🤗)")

    return players

def display_players(players):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for player in players:
        print(f"🥃{player.name} 지금까지 마신 잔 수: 🥃 {player.current_drinks}잔 🥃 / 치사량까지 남은 잔 수: 🥃 {player.drinks_left()}잔 🥃")

def show_game_list():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🎮 게임 리스트 🎮~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. 게임1")
    print("2. 369 게임")
    print("3. 게임3")
    print("4. 게임4")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def play_369(players):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("    __       ____       __                                               ")
    print("  /'__`\    /'___\    /'_ `\                                             ")  
    print(" /\_\L\ \  /\ \__/   /\ \L\ \      __        __       ___ ___       __   ")
    print(" \/_/_\_<_ \ \  _``\ \ \___, \   /'_ `\    /'__`\   /' __` __`\   /'__`\ ")                                              
    print("   /\ \L\ \ \ \ \L\ \ \/__,/\ \ /\ \L\ \  /\ \L\.\_ /\ \/\ \/\ \ /\  __/ ")
    print("   \ \____/  \ \____/      \ \_\\ \____ \ \ \__/\_\_\ \_\ \_\ \ \\ \____\ ")
    print("    \/___/    \/___/        \/_/ \/___L\ \ \/__/\/_/ \/_/\/_/\/_/ \/____/")
    print("                                   /\____/                               ")
    print("                                   \_/__/       ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~🎼 369~369~369 🎼~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    number = 1
    while True:
        for player in players:
            print(f"{player.name}님의 차례입니다.")
            expected = player.auto_move(number) if not player.is_user else None
            
            if not player.is_user and random.random() < 0.3:
                response = player.random_incorrect_move(number)
            else:
                response = player.make_move(number)
            
            # 출력
            if not player.is_user:
                print(f"{player.name}: {response}")
            
            # 응답 확인
            if expected is None:
                if ('3' in str(number) or '6' in str(number) or '9') and response != '짝' * (str(number).count('3') + str(number).count('6') + str(number).count('9')):
                    print(f"{player.name}님이 졌습니다!")
                    player.drink(1)
                    display_players(players)
                    if player.is_intoxicated():
                        return
                elif not ('3' in str(number) or '6' in str(number) or '9') and response != str(number):
                    print(f"{player.name}님이 졌습니다!")
                    player.drink(1)
                    display_players(players)
                    if player.is_intoxicated():
                        return
            else:
                if response != expected:
                    print(f"{player.name}님이 졌습니다!")
                    player.drink(1)
                    display_players(players)
                    if player.is_intoxicated():
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
