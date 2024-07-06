import random

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
            return f"{self.name}이 치사량에 도달했습니다."
        else:
            return f"{self.name}이 현재 {self.current_drinks}잔 마셨습니다. 치사량까지 {self.max_alcohol - self.current_drinks}잔 남았습니다."

    def game_chosung(self):
        # 초성 게임 로직 구현
        print(f"{self.name}이 초성 게임을 하고 있습니다.")
        # 예시: 한 잔 마신 것으로 처리
        return self.drink(1)

    def game_369(self):
        # 369 게임 로직 구현
        print(f"{self.name}이 369 게임을 하고 있습니다.")
        return self.drink(1)

    def game_dubu(self):
        # 두부 게임 로직 구현
        print(f"{self.name}이 두부 게임을 하고 있습니다.")
        return self.drink(1)

    def game_joa(self):
        # 좋아 게임 로직 구현
        print(f"{self.name}이 좋아 게임을 하고 있습니다.")
        return self.drink(1)

    def game_love_shoot(self):
        # 사랑의 총알 게임 로직 구현
        print(f"{self.name}이 사랑의 총알 게임을 하고 있습니다.")
        return self.drink(1)

    def play_game(self, game_name):
        if game_name == "초성 게임":
            return self.game_chosung()
        elif game_name == "369 게임":
            return self.game_369()
        elif game_name == "두부 게임":
            return self.game_dubu()
        elif game_name == "좋아 게임":
            return self.game_joa()
        elif game_name == "사랑의 총알 게임":
            return self.game_love_shoot()
        else:
            return "알 수 없는 게임입니다."

# 메인 게임 로직
def main():
    # 사용자 정보 입력 받기
    player_name = input("이름을 입력하세요: ")
    player_alcohol = int(input("주량을 입력하세요: "))

    player = Person(player_name, player_alcohol)

    print(player.measure_drink())

    # 대결할 사람 초대
    opponents = []
    for i in range(random.randint(1, 3)):
        opponent_name = random.choice(["은서", "하연", "연서", "예진", "헌도"])
        opponent_alcohol = random.randint(3, 7)
        opponents.append(Person(opponent_name, opponent_alcohol))

    # 게임 리스트 출력
    game_list = ["초성 게임", "369 게임", "두부 게임", "좋아 게임", "사랑의 총알 게임"]
    print("게임 리스트:", game_list)

    # 게임 선택 및 실행
    while True:
        game_choice = input("게임을 선택하세요: ")
        result = player.play_game(game_choice)
        print(result)
        
        if player.current_drinks >= player.max_alcohol:
            print(f"{player.name}이 치사량에 도달했습니다. 게임 종료.")
            break

        for opponent in opponents:
            opponent_game_choice = random.choice(game_list)
            result = opponent.play_game(opponent_game_choice)
            print(result)
            
            if opponent.current_drinks >= opponent.max_alcohol:
                print(f"{opponent.name}이 치사량에 도달했습니다. 게임 종료.")
                return

if __name__ == "__main__":
    main()

