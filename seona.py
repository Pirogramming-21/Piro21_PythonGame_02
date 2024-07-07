#main은 예원님의 코드 + 1번에 updown 게임 넣어놓음, 컴퓨터 플레이어 우리 이름으로 수정
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
    player_names = ["선아", "지훈", "예원", "화현"]
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
    print("1. up&down게임")
    print("2. 게임2")
    print("3. 게임3")
    print("4. 게임4")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    
def play_updown(players):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                    Up & Down 게임을 시작합니다!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    target = random.randint(1, 100)

    while True:
        for player in players:
            print(f"{player.name}님의 차례입니다.")
            if player.is_user:
                guess = input("1부터 100 사이의 숫자를 맞춰보세요: ")
            else:
                guess = str(random.randint(1, 100))
                print(f"{player.name}: {guess}")

            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    raise ValueError
            except ValueError:
                print("잘못된 입력입니다. 1부터 100 사이의 숫자를 입력하세요.")
                continue

            if guess == target:
                print(f"정답입니다! {player.name}님이 벌칙을 받습니다!")
                player.drink()
                display_players(players)
                if player.is_intoxicated():
                    return
                return  # 게임 종료 후 다른 게임으로 이동
            elif guess < target:
                print("Up!")
            else:
                print("Down!")



def play_game(players):
    while True:
        display_players(players)
        show_game_list()
        try:
            game_choice = int(input("게임을 선택하세요: ").strip())
            if game_choice == 1:
                play_updown(players)
                break
            else:
                print("해당 게임은 아직 구현되지 않았습니다.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

def random_game_choice():
    return random.choice([1, 2, 3, 4])  # 1: Up & Down(선아 구현), 나머지 2, 3, 4

def main():
    if not intro():
        return

    user_name, user_capacity = get_user_info()
    user = Player(user_name, user_capacity, is_user=True)
    players = [user] + invite_players()
    
    while True:
        display_players(players)
        
        current_player = random.choice(players)
        
        print(f"\n{current_player.name}님의 차례입니다.")
        
        if current_player.is_user:
            show_game_list()
            try:
                game_choice = int(input("게임을 선택하세요: ").strip())
                if game_choice in [1, 2, 3, 4]:
                    if game_choice == 1:
                        play_updown(players)
                    else:
                        print("해당 게임은 아직 구현되지 않았습니다.")
                else:
                    print("1에서 4 사이의 숫자를 입력하세요.")
                    continue
            except ValueError:
                print("올바른 숫자를 입력하세요.")
                continue
        else:
            print(f"{current_player.name}님이 게임을 랜덤으로 선택합니다.")
            random_game = random_game_choice()
            print(f"선택된 게임: {random_game}")
            if random_game == 1:
                play_updown(players)
            else:
                print("해당 게임은 아직 구현되지 않았습니다.")

        # 게임 종료 조건 확인
        intoxicated_players = [p for p in players if p.is_intoxicated()]
        if intoxicated_players:
            print("\n게임이 종료되었습니다!")
            print("최종 결과:")
            display_players(players)
            for p in intoxicated_players:
                print(f"{p.name}이(가) 전사했습니다...꿈나라에서는 편히 쉬시길...zzzz")
            return
        
        #처음부터 플레이어가 랜덤으로 선택되는 오류, 중복 선택 오류가 있음... 해결해주실 수 있는 천사 구해요
        # 현재 플레이어를 제외한 나머지 플레이어들 중에서 다음 플레이어 선택(이 부분이 문제가 있는 것 같음)
        remaining_players = [p for p in players if p != current_player]
        if not remaining_players:  # 만약 모든 플레이어가 차례를 가졌다면 다시 전체 플레이어로 초기화
            remaining_players = players

        print("\n다음 플레이어를 선택합니다.")
        
if __name__ == "__main__":
    main()




