import random

class Player:
    def __init__(self, name, capacity, is_user=False):
        self.name = name
        self.capacity = capacity
        self.current_drinks = 0
        self.is_user = is_user
        self.has_chosen_game = False

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
    print("                    □□■■■■■■■■□□□□□□□□□■■□■□□□□■□□□□□■■")
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
        print(f"🤗 안녕? 난 {name}(이)고, 내 주량은 🥃 {capacity}잔이야 🤗")

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
    print("4. 지하철 게임")
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
                elif not ('3' in str(number) or '6' in str(number) or '9') in str(number) and response != str(number):
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

# 서울 지하철 1호선 역 목록
line_1 = [
    "소요산", "동두천", "보산", "동두천중앙", "지행", "덕정", "덕계", "양주", "녹양", "가능", "의정부",
    "회룡", "망월사", "도봉산", "도봉", "방학", "창동", "녹천", "월계", "광운대", "석계", "신이문",
    "외대앞", "회기", "청량리", "제기동", "신설동", "동묘앞", "동대문", "종로5가", "종로3가", "종각",
    "시청", "서울역", "남영", "용산", "노량진", "대방", "신길", "영등포", "신도림", "구로", "구일",
    "개봉", "오류동", "온수", "역곡", "소사", "부천", "중동", "송내", "부개", "부평", "백운", "동암",
    "간석", "주안", "도화", "제물포", "도원", "동인천", "인천"
]

# 랜덤 역 선택
def random_station():
    return random.choice(line_1)

# 지하철 게임
def play_subway(players):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("      ________   __       __  __                             __      ")
    print("     /  _____/  |__| ____ |__|/  |_ __ __  ____    ____    _/  |_   ")
    print("    /   \  ___  |  |/    \|  \   __\  |  \/    \  / ___\   \   __\  ")
    print("    \    \_\  \ |  |   |  \  ||  | |  |  /   |  \/ /_/  >   |  |    ")
    print("     \______  / |__|___|  /__||__| |____/|___|  /\___  /    |__|    ")
    print("            \/          \/                    \//_____/             ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~🎼 이 다음 역은~ ♬지금까지~ ♪🎼~~~~~~~~~~~~~~~~~~~~")

    chosen_station = random_station()
    print(f"초기 역은 {chosen_station}입니다.")
    
    current_station = chosen_station
    
    while True:
        for player in players:
            print(f"{player.name}님의 차례입니다.")
            next_station = player.auto_move(current_station) if not player.is_user else None
            response = player.make_move(current_station)
            
            # 출력
            if not player.is_user:
                print(f"{player.name}: {response}")

            # 응답 확인
            if next_station is None:
                if response not in line_1 or response == current_station:
                    print(f"{player.name}님이 졌습니다!")
                    player.drink()
                    display_players(players)
                    if player.is_intoxicated():
                        return
                    current_station = random_station()
                    print(f"새로운 역은 {current_station}입니다.")
                    break
                else:
                    current_station = response
            else:
                if response != next_station:
                    print(f"{player.name}님이 졌습니다!")
                    player.drink()
                    display_players(players)
                    if player.is_intoxicated():
                        return
                    current_station = random_station()
                    print(f"새로운 역은 {current_station}입니다.")
                    break
                else:
                    current_station = next_station

def play_game(players):
    while True:
        show_game_list()
        print("게임을 선택하세요 (1~4, 종료하려면 q):")
        choice = input().strip()
        if choice == '1':
            print("게임1은 아직 준비 중입니다.")
        elif choice == '2':
            play_369(players)
        elif choice == '3':
            print("게임3은 아직 준비 중입니다.")
        elif choice == '4':
            play_subway(players)
        elif choice.lower() == 'q':
            print("게임이 종료되었습니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 선택하세요.")

if __name__ == "__main__":
    if intro():
        user_name, user_capacity = get_user_info()
        user = Player(user_name, user_capacity, is_user=True)
        players = [user] + invite_players()
        display_players(players)
        play_game(players)
