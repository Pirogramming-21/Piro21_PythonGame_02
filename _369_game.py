import random

class Player:
    def __init__(self, name, is_user=False):
        self.name = name
        self.is_user = is_user

    def make_move(self, number):
        if self.is_user:
            return input(f"{self.name}: ").strip()
        else:
            return self.auto_move(number)
    
    def auto_move(self, number):
        if random.random() < 0.5:  # 10% chance of providing an incorrect response
            return self.generate_incorrect_response(number)
        else:
            if '3' in str(number) or '6' in str(number) or '9' in str(number):
                clap_count = str(number).count('3') + str(number).count('6') + str(number).count('9')
                return '짝' * clap_count
            else:
                return str(number)
    
    def generate_incorrect_response(self, number):
        if '3' in str(number) or '6' in str(number) or '9' in str(number):
            return str(number)  # Wrong response should be a number instead of "짝"
        else:
            return '짝'  # Wrong response should be "짝" instead of the number

def play_369(players):
    number = 1
    while True:
        for player in players:
            expected = player.auto_move(number) if not player.is_user else None
            response = player.make_move(number)
            
            # Output the response
            if not player.is_user:
                print(f"{player.name}: {response}")
            
            # Check for incorrect responses
            if (('3' in str(number) or '6' in str(number) or '9' in str(number)) and response != '짝' * (str(number).count('3') + str(number).count('6') + str(number).count('9'))) or \
               (not ('3' in str(number) or '6' in str(number) or '9' in str(number)) and response != str(number)):
                print(f"{player.name}님이 졌습니다!")
                return
            
            number += 1

if __name__ == "__main__":
    user_name = input("당신의 이름을 입력하세요: ").strip()
    user = Player(user_name, is_user=True)
    other_names = ["참가자 2", "참가자 3"]
    random.shuffle(other_names)
    other_players = [Player(name) for name in other_names]
    players = [user] + other_players
    random.shuffle(players)
    
    play_369(players)
    
    input("게임이 종료되었습니다. 엔터 키를 누르면 프로그램이 종료됩니다.")