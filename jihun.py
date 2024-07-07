import random, sys

class Person:
    def __init__(self, name, max_alcohol, is_user=False):
        self.name = name
        self.max_alcohol = max_alcohol
        self.current_drinks = 0
        self.is_user = is_user

    def measure_drink(self):
        return f"{self.name}의 주량은 {self.max_alcohol}잔입니다."

    def drink(self, amount):
        self.current_drinks += amount
        if self.current_drinks >= self.max_alcohol:
            return f"{self.name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz"
        else:
            return f"{self.name}은(는) 지금까지 {self.current_drinks}잔 마셨습니다! 치사량까지 {self.max_alcohol - self.current_drinks}잔 남았습니다."

class Game:
    def play_game(self,players):
        while True:
            try:
                game_choice = int(input("게임을 선택하세요: ").strip())
                if game_choice == 2:
                    self.play_369(players)
                    break
                else:
                    print("해당 게임은 아직 구현되지 않았습니다.")
            except ValueError:
                print("올바른 숫자를 입력하세요.")

    def play_369(self, players):
        print("")

    def jh_game(self, players):
        print("")

    def hy_game(self, players):
        print("")

    def sunna_game(players):
        print("")





# 인트로 함수
def intro():
    print("게임을 진행할까요? (y/n)")
    choice = input().strip().lower()
    if choice == 'y':
        return True
    elif choice == 'n':
        print("게임이 종료되었습니다.")
        sys.exit()
        return
    else:
        print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

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
    print("게임 리스트")
    print("1. 게임1")
    print("2. 369 게임")
    print("3. 게임3")
    print("4. 게임4")

# 메인 게임 로직
def main_game():

    # 1. 게임 할까말까 여부    
    intro()

    # 2. 사용자(주인공) 이름 받기
    player_name = input("오늘 거하게 취해볼 당신의 이름은? : ")

    # 3. 사용자(주인공) 주량 선택하기
    choice_list = '~~~~~~~~~소주 기준 당신의 주량은? ~~~~~~~~~~\n'\
    '1. 소주 반 병 (2잔)\n'\
    '2. 소주 반 병에서 한 병 (4잔)\n'\
    '3. 소주 한 병에서 한 병 반 (6잔)\n'\
    '4. 소주 한 병 반에서 두 병 (8잔)\n'\
    '5. 소주 두 병 이상 (10잔)'

    print(choice_list)

    player_alcohol = 2* int(input("당신의 치사량(주량)은 얼마만큼인가요?(1~5를 선택해주세요): "))
    player = Person(player_name, player_alcohol, is_user=True)

    #4-1. 대결할 사람 초대
    capacity = [2,4,6,8,10]
    player1 = Person("지훈", random.choice(capacity)) #주량 2,4,6,8,10 중 랜덤선택
    player2 = Person("예원", random.choice(capacity))
    player3 = Person("화현", random.choice(capacity))
    player4 = Person("선아", random.choice(capacity))

    players = [player1, player2, player3, player4]
    opponents = random.sample(players, k = num_players())
    
    #4-2. 게임 멤버들 소개
    for opponent in opponents:
        print(f"오늘 함께 취할 친구는 {opponent.name}입니다! (치사량 : {opponent.max_alcohol})")

    #4-3. 게임 리스트 출력
    show_game_list()

    #5. 게임 시작
    
    # 게임 선택 및 실행
    while True:
        # 게이머들 지정
        gamers = [player].append(opponents)


        game_choice = input("00이가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? (번호를 입력하세요): ")
        result = play_game(player, game_choice)
        print(result)
        
        if player.current_drinks >= player.max_alcohol:
            print(f"{player.name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
            return

        for opponent in opponents:
            result = play_game(opponent, game_choice)
            print(result)
            
            if opponent.current_drinks >= opponent.max_alcohol:
                print(f"{opponent.name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
                return

if __name__ == "__main__":
    main_game()