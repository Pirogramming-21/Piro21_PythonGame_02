import random, sys
import up_and_down_game, imground_game, subway_game, _369_game, apart_game

# 사람 클래스 패키지
class Person:
    def __init__(self, name, max_alcohol, is_user=False):
        self.name = name
        self.max_alcohol = max_alcohol
        self.current_drinks = 0
        self.is_user = is_user

    def measure_drink(self):
        return f"{self.name}의 주량은 {self.max_alcohol}잔입니다."
    
    def drinks_left(self):
        return self.max_alcohol - self.current_drinks
    
    def drink(self, amount):
        self.current_drinks += amount
        return f"{self.name}은(는) 지금까지 {self.current_drinks}잔 마셨습니다! 치사량까지 {self.max_alcohol - self.current_drinks}잔 남았습니다."
    
    def is_intoxicated(self):
        return self.current_drinks >= self.max_alcohol
            
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

# 게임 클래스 패키지
class Game:
    def __init__(self, players:list):
        self.players = players

    def play_game(self):
        print(f'{self.players[0].name}이(가) 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? ', end = "")
        while True:
            if self.players[0].is_user:
                try:
                    game_choice = input().strip()
                    if not game_choice.isdigit():
                        raise ValueError
                    game_choice = int(game_choice)
                except ValueError:
                    print("올바른 숫자를 입력하세요.")
                    continue
            else:
                game_choice = random.randint(1, 4)
            try:
                if game_choice == 1:
                    self.play_subway()
                    return
                elif game_choice == 2:
                    self.play_369()
                    return
                elif game_choice == 3:
                    self.play_updown()
                    return
                elif game_choice == 4:
                    self.play_imground()
                    return
                elif game_choice == 5:
                    self.play_apart()
                    return
                else:
                    print("해당 게임은 아직 구현되지 않았습니다.")
            except ValueError:
                print("올바른 숫자를 입력하세요.")

    def play_subway(self):
        subway_game.play_subway(self.players)

    def play_369(self):
        _369_game.play_369(self.players)

    def play_updown(self):
        up_and_down_game.play_updown(self.players)

    def play_imground(self):
        imground_game.play_imground(self.players)

    def play_apart(self):
        apart_game.play_apart(self.players)

# 인트로 함수
def intro():
    print("게임을 진행할까요? (y/n)")
    choice = input().strip().lower()
    if choice == 'y':
        return False
    elif choice == 'n':
        print("게임이 종료되었습니다.")
        sys.exit()
        return True
    else:
        print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")
        return True

# 플레이어 수 결정 함수
def num_players():
    while True:
        try:
            num = int(input("함께 취할 친구들은 얼마나 필요하신가요? (최대 3명)  "))
            if 0 <= num <= 3:
                return num
            else:
                print("0에서 3사이의 숫자를 입력하세요.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

# 게임 리스트 보여주는 함수
def show_game_list():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~🎮 게임 리스트 🎮~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. 지하철 게임")
    print("2. 369 게임")
    print("3. Up & Down 게임")
    print("4. 아이엠그라운드 게임")
    print("5. 아파트 게임")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 메인 게임 로직
def main_game():

    # 1. 게임 할까말까 여부    
    while intro():
        print("")

    # 2. 사용자(주인공) 이름 받기
    player_name = input("😵오늘 첫 차 탈 당신의 이름은?😵   ")

    # 3. 사용자(주인공) 주량 선택하기
    choice_list = '~~~~~~~~~🥃소주 기준 당신의 주량은? ~~~~~~~~~~\n'\
    '🥃 1. 소주 반 병 (2잔)\n'\
    '🥃 2. 소주 반 병에서 한 병 (4잔)\n'\
    '🥃 3. 소주 한 병에서 한 병 반 (6잔)\n'\
    '🥃 4. 소주 한 병 반에서 두 병 (8잔)\n'\
    '🥃 5. 소주 두 병 이상 (10잔)'

    print(choice_list)

    player_alcohol = 2 * int(input("당신의 치사량(주량)은 얼마만큼인가요?(1~5를 선택해주세요): "))
    player = Person(player_name, player_alcohol, is_user=True)

    #4-1. 대결할 사람 초대
    capacity = [2, 4, 6, 8, 10]
    player1 = Person("지훈", random.choice(capacity))  # 주량 2, 4, 6, 8, 10 중 랜덤선택
    player2 = Person("예원", random.choice(capacity))
    player3 = Person("화현", random.choice(capacity))
    player4 = Person("선아", random.choice(capacity))

    players = [player1, player2, player3, player4]
    opponents = random.sample(players, k=num_players())

    #4-2. 게임 멤버들 소개
    for opponent in opponents:
        print(f"오늘 함께 취할 친구는 {opponent.name}입니다! (치사량 : {opponent.max_alcohol})")

    # 주인공 + 추가된 랜덤 플레이어들
    gamers = []
    gamers.append(player)
    gamers.extend(opponents)

    # 마신 잔 수 및 치사량 출력    
    for gamer in gamers:
        print(gamer.drink(0))

    #4-3. 게임 리스트 출력
    show_game_list()    
    
    #5. 게임 시작    
    # 게임 선택 및 실행
    while True:
        # 게이머들 지정
        starter = gamers[0]  # 게임 시작하는 사람

        # 게임 시작!
        game = Game(gamers)
        game.play_game()

        # 게임 후 플레이어들 마신 잔 수 및 남은 잔 수 출력
        for gamer in gamers:
            print(gamer.drink(0))

        # 죽은 사람 있는지 확인
        for gamer in gamers:
            if gamer.is_intoxicated():
                print("__________________________________________")
                print("______________GAME OVER____________________")
                print("__________________________________________")
                print(f"{gamer.name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
                sys.exit()
        # 한판 더 할건지 여부 물어보기
        show_game_list()
        print('술게임 진행중! 다른 사람의 턴입니다. 그만하고 싶으면 "exit"을, 계속하고 싶으면 아무키나 입력해 주세요!:  ', end="")
        end_yn = input().strip().lower()
        if end_yn == "exit":
            print("즐거운 게임이었습니다!!!!")
            sys.exit()
        else:
            # 다음 플레이어 설정
            next_player_index = random.randint(1, len(gamers) - 1)
            starter = gamers.pop(next_player_index)
            gamers.insert(0, starter)

if __name__ == "__main__":
    main_game()
