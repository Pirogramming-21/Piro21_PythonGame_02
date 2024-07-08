import random

def make_move(player, number):
    if player.is_user:
        return input(f"{player.name}: ").strip()
    else:
        return auto_move(player,number)
    
def auto_move(player, number):
    if random.random() < 0.1:  # 10% chance of providing an incorrect response
        return generate_incorrect_response(player, number)
    else:
        if '3' in str(number) or '6' in str(number) or '9' in str(number):
            clap_count = str(number).count('3') + str(number).count('6') + str(number).count('9')
            return '짝' * clap_count
        else:
            return str(number)

def generate_incorrect_response(player, number):
    if '3' in str(number) or '6' in str(number) or '9' in str(number):
        return str(number)  # Wrong response should be a number instead of "짝"
    else:
        return '짝'  # Wrong response should be "짝" instead of the number



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
            expected = auto_move(player,number) if not player.is_user else None
            response = make_move(player,number)
            
            # Output the response
            if not player.is_user:
                print(f"{player.name}: {response}")
            
            # Check for incorrect responses
            if (('3' in str(number) or '6' in str(number) or '9' in str(number)) and response != '짝' * (str(number).count('3') + str(number).count('6') + str(number).count('9'))) or \
               (not ('3' in str(number) or '6' in str(number) or '9' in str(number)) and response != str(number)):
                print(f"{player.name}님이 졌습니다!")
                player.drink(1)
                return
            
            number += 1
