import random

def play_imground(players):
    solo = next(player for player in players if player.is_user)
    solo_name = solo.name

    def print_players():
        names = [player.name for player in players]
        print("참가자들: " + ", ".join(names))

    def get_next_player(target_name):
        for index, player in enumerate(players):
            if player.name == target_name:
                return index, player
        return -1, None

    def check_name_repetition(name, count, input_sequence):
        expected_sequence = " ".join(["짝"] * (4 - count) + [name] * count)
        return expected_sequence == input_sequence.strip()

    def random_name_and_count(exclude_name):
        target = random.choice([player for player in players if player.name != exclude_name])
        count = random.randint(1, 4)
        return target.name, count

    def random_clap_name(name, count):
        return " ".join(["짝"] * (4 - count) + [name] * count)

    def random_clap_name_incorrect(name, count):
        incorrect_sequence = ["짝"] * 4
        for _ in range(count):
            incorrect_sequence[random.randint(0, 3)] = name
        return " ".join(incorrect_sequence)

    # 아스키 아트 출력
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("             _____       ___   __  __       ____   ____     _____  __   __   __   __   _____                ")
    print("            |_   _|     / _ \ |  \/  |    / ____| |  __ \  / __  \ | |  | | |  \  | | |  __  \              ")
    print("              | |      / /_\ \| .  . |    | |     |  |_\ | | | | | | |  | | |   \ | | |  | | |              ")
    print("              | |      |  _  || |\/| |    | |  _  |  _  /  | | | | | |  | | |    \| | |  | | |              ")
    print("             _| |_     | | | || |  | |    | |_| | | | \ \  | |_|   | |__| | |  |\   | |  |_| |              ")
    print("            |_____|    \_/  \_|_|  \_|     \____| |_|  \_\  \___/  \_____/  |__| \__| |_____/               ")
    print("                                                                                                            ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("아이엠~그라운드~ 지금부터 시작!")
    print_players()

    current = 0

    while True:
        current_name = players[current].name
        print(f"\n지목 순서: {current_name}")

        if current_name == solo_name:
            input_line = input("지목할 사람의 이름과 횟수를 입력하세요(예: 이름 2): ").strip()
            if input_line == "종료" or input_line == "":
                print("게임을 종료합니다.")
                return

            try:
                target_name, count = input_line.split()
                count = int(count)
                if count < 1 or count > 4:
                    print("1에서 4 사이의 숫자를 입력하세요.")
                    print(f"{current_name}가 잘못된 숫자를 입력했습니다. {current_name} 벌칙 당첨!")
                    players[current].drink(1)
                    return
            except ValueError:
                print("이름과 횟수를 입력하세요. (예: 화현 2)")
                print(f"{current_name}가 잘못된 형식을 입력했습니다. {current_name} 벌칙 당첨!")
                players[current].drink(1)
                return

            if target_name not in [player.name for player in players]:
                print("참가자가 아닙니다.")
                print(f"{current_name}가 참가자 목록에 없는 이름을 선택했습니다. {current_name} 벌칙 당첨!")
                players[current].drink(1)
                return

            if target_name == current_name:
                print(f"{current_name}가 본인을 지목했습니다. {current_name} 벌칙 당첨!")
                players[current].drink(1)
                return
        else:
            target_name, count = random_name_and_count(current_name)
            print(f"지목할 사람의 이름과 횟수를 입력하세요(예: 이름 2): {target_name} {count}")

        print(f"이름을 4박자에 맞춰 외쳐야 합니다.")

        if target_name != solo_name:
            if random.randint(1, 10) <= 7:
                input_sequence = random_clap_name(target_name, count)
            else:
                input_sequence = random_clap_name_incorrect(target_name, count)
            print(f"현재 순서: {input_sequence}")
        else:
            print(f"4박자에 맞춰 이름을 외쳐주세요 (예: 짝 짝 이름 이름):")
            input_sequence = input().strip()

        if not check_name_repetition(target_name, count, input_sequence):
            print(f"박자는 생명~ 박자는 생명~ {target_name} 벌칙 당첨!")
            target_player_index, _ = get_next_player(target_name)
            players[target_player_index].drink(1)
            return

        print(f"{target_name}가 올바르게 이름을 외쳤습니다.")
        current, _ = get_next_player(target_name)
        
        if current == -1:
            print("게임에서 탈락한 사람이 있습니다. 게임을 종료합니다.")
            return

        if players[current].is_intoxicated():
            print(f"{players[current].name}가 술을 너무 많이 마셔서 게임을 계속할 수 없습니다.")
            return

