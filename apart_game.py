import random

def play_apart(players):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("       __       ______      __      ______   __________     ")
    print("      /  \     |   __ \    /  \    |   __ \  |__    __|     ")
    print("     / /\ \    |  |__| |  / /\ \   |  |__| |    |  |        ")
    print("    /  __  \   |  ____/  /  __  \  |  __  /     |  |        ")
    print("   /  /  \  \  |  |     /  /  \  \ |  | \  \    |  |       ")
    print("  /__/    \__\ |__|    /__/    \__\|__|  \__\   |__|        ")
    print("                                                            ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~아파트! 아파트! 아파트! 아파트!~~~~~~~~~~~~~~~")
    
    num_players = len(players)
    num_turns = num_players * 2
    random_floor = random.randint(1, 30) 
    print(f"{random_floor} 층!")

    turns = players * 2
    random.shuffle(turns)
    
    turn_names = [player.name for player in turns]
    print(f"플레이어 순서: {turn_names}")

    current_floor = 1
    
    while True:
        for player in turns:
            while True:
                if player.is_user:
                    user_input = input(f"{player.name}, 몇 층?: ").strip()
                    if user_input.lower() == "종료":
                        print("게임을 종료합니다.")
                        return
                    try:
                        floor = int(user_input)
                        if floor != current_floor:
                            print(f"잘못된 층수입니다. {current_floor}층을 외쳐야 합니다.")
                            continue
                    except ValueError:
                        print(f"숫자를 입력하세요. {current_floor}층을 외쳐야 합니다.")
                        continue
                else:
                    floor = current_floor
                    print(f"{player.name}, 몇 층?: {floor}")
                
                if floor == random_floor:
                    print(f"{player.name} 벌칙 당첨!")
                    player.drink(1)
                    return
                
                current_floor += 1
                break

