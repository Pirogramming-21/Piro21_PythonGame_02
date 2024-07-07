import random, sys

class Person:
    def __init__(self, name, max_alcohol):
        self.name = name
        self.max_alcohol = max_alcohol
        self.current_drinks = 0

    def measure_drink(self):
        return f"{self.name}의 주량은 {self.max_alcohol}잔입니다."

    def drink(self, amount):
        self.current_drinks += amount
        if self.current_drinks >= self.max_alcohol:
            return f"{self.name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz"
        else:
            return f"{self.name}은(는) 지금까지 {self.current_drinks}잔 마셨습니다! 치사량까지 {self.max_alcohol - self.current_drinks}잔 남았습니다."

# 각 게임별 함수 정의
# def game_jh(person):
#     print(f"{person.name}이 지훈 게임을 하고 있습니다.")
#     return person.drink(1)

# def game_yw(person):
#     print(f"{person.name}이 예원 게임을 하고 있습니다.")
#     return person.drink(1)

# def game_hh(person):
#     print(f"{person.name}이 화현 게임을 하고 있습니다.")
#     return person.drink(1)

# def game_sa(person):
#     print(f"{person.name}이 선아 게임을 하고 있습니다.")
#     return person.drink(1)


# 게임 선택 함수
# def play_game(person, game_name):
#     if game_name == "1": # 1 == 지훈 게임
#         return game_jh(person)
#     elif game_name == "2": # 2 == 예원 게임
#         return game_yw(person)
#     elif game_name == "3": # 3 == 화현 게임
#         return game_hh(person)
#     elif game_name == "4": # 4 == 선아 게임
#         return game_sa(person)
#     else:
#         return "알 수 없는 게임입니다."
def game_ground(opponents, current_player):
    def print_participants():
        names = [opponent.name for opponent in opponents]
        print("참가자들: " + ", ".join(names))

    def get_next_participant(current):
        return (current + 1) % len(opponents)

    def check_name_repetition(name, count, input_sequence):
        expected_sequence = " ".join(["짝"] * (4 - count) + [name] * count)
        return expected_sequence == input_sequence.strip()

    # 아스키 아트 출력
    print("""
...
    """)
    print("아이엠그라운드 게임 시작!")
    print_participants()

    current = 0
    while True:
        current_name = opponents[current].name
        print(f"\n현재 순서: {current_name}")
        input_line = input("지목할 사람의 이름과 횟수를 입력하세요 (종료하려면 '종료' 입력): ").strip()
        if input_line == "종료":
            print("게임을 종료합니다.")
            break

        try:
            target_name, count = input_line.split()
            count = int(count)
            if count < 1 or count > 4:
                print("1에서 4 사이의 숫자를 입력하세요.")
                continue
        except ValueError:
            print("올바른 형식으로 입력하세요 (예: 지수 2)")
            continue

        if target_name not in [opponent.name for opponent in opponents]:
            print("참가자 목록에 없는 이름입니다. 다시 입력하세요.")
            continue

        if target_name == current_name:
            print(f"{current_name}가 본인을 지목했습니다. {current_name}가 게임에서 패배했습니다.")
            return f"{current_name}가 게임에서 패배했습니다."

        print(f"{target_name}가 자신의 이름을 4박자에 맞춰 {count}번 외쳐야 합니다.")
        print(f"4박자에 맞춰 이름을 외쳐주세요 (예: 짝 짝 {target_name} {target_name}):")
        input_sequence = " ".join(input().split())

        if check_name_repetition(target_name, count, input_sequence):
            print(f"{target_name}가 올바르게 이름을 외쳤습니다.")
        else:
            print(f"{target_name}가 이름을 잘못 외쳤습니다. 게임에서 패배했습니다.")
            return f"{target_name}가 게임에서 패배했습니다."

        current = get_next_participant(current)

def play_game(person, game_name,opponents):
    if game_name == "3":
        result = game_ground(opponents, person)
        return result
    else:
        return f"알 수 없는 게임입니다: {game_name}"
    
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
    player = Person(player_name, player_alcohol)
    
    # 친구 수 입력 예외 처리
    # while True:
    #     try:
    #         player_friends = int(input("함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기로 인해 최대 3명까지 초대할 수 있어요!) : "))
    #         if 1 <= player_friends <= 3:
    #             break
    #         else:
    #             print("잘못된 입력입니다. 1부터 3 사이의 숫자를 입력해주세요.")
    #     except ValueError:
    #         print("숫자를 입력해주세요.")
    
    # print(player.measure_drink())

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
    game_list = ["1", "2", "3", "4"]
    print("게임 리스트: 1. 지훈 게임, 2. 예원 게임, 3. 화현 게임, 4. 선아 게임")

    # 게임 선택 및 실행
    while True:
        game_choice = input("00이가 좋아하는 랜덤 게임~ 랜덤 게임~ 무슨 게임? (번호를 입력하세요): ")
        result = play_game(player, game_choice,opponents)
        print(result)
        
        if player.current_drinks >= player.max_alcohol:
            print(f"{player.name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
            return

        for opponent in opponents:
            result = play_game(opponent, game_choice,opponents)
            print(result)
            
            if opponent.current_drinks >= opponent.max_alcohol:
                print(f"{opponent.name}이(가) 전사했습니다... 꿈나라에서는 편히 쉬시길..zzz")
                return

# 1) 게임 시작 여부를 묻는 코드 -> y를 누르면 main_game()으로 감
# game_start = input("게임을 진행할까요? (y/n) : ")
# if game_start.lower() == 'y': # 답변 대소문자 구분하지 않고 처리(lower)
#     print("게임을 시작합니다!")
#     main_game()
# elif game_start.lower() == 'n':
#     print("게임을 종료합니다.")
# else:
#     print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

if __name__ == "__main__":
    main_game()