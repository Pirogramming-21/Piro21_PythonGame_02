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
        if '3' in str(number) or '6' in str(number) or '9' in str(number):
            clap_count = str(number).count('3') + str(number).count('6') + str(number).count('9')
            return '짝' * clap_count
        else:
            return str(number)

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
            if expected is None:
                if ('3' in str(number) or '6' in str(number) or '9' in str(number)) and response != '짝' * (str(number).count('3') + str(number).count('6') + str(number).count('9')):
                    print(f"{player.name}님이 졌습니다!")
                    return
                elif not ('3' in str(number) or '6' in str(number) or '9' in str(number)) and response != str(number):
                    print(f"{player.name}님이 졌습니다!")
                    return
            else:
                if response != expected:
                    print(f"{player.name}님이 졌습니다!")
                    return
            
            number += 1

def main():
    user_name = input("당신의 이름을 입력하세요: ").strip()
    user = Player(user_name, is_user=True)
    other_names = ["참가자 2", "참가자 3"]
    random.shuffle(other_names)
    other_players = [Player(name) for name in other_names]
    players = [user] + other_players
    random.shuffle(players)
    
    play_369(players)

if __name__ == "__main__":
    main()