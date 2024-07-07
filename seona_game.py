#up and down 게임만 구현.
def play_updown(players):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("""
             _    _  _____      ___    _   _  _____     _____      _____    __        __  __   __
            | |  | ||  __ \    / _ \  | \ | ||  __ \   |  __ \    /  __  \  \ \      / /  | \ | |
            | |  | || |__) |  / /_\ \ |  \| || |  | |  | |  | |   | |  | |   \ \ /\ / /   |  \| |
            | |  | ||  ___/   |  _  | | . ` || |  | |  | |  | |   | |  | |    \ V  V /    | . ` |
            | |__| || |       | | | | | |\  || |__| |  | |__| |   | |__| |     \_/\_/     | |\  |
             \____/ |_|       \_| |_/ |_| \_||_____/   |_____/    \______/                |_| \_|
               
                """)

    print("                            Up & Down 게임을 시작합니다!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    target = random.randint(1, 100)
    used_numbers = set() #이미 입력된 숫자를 집합으로 처리
    lower_bound = 1 #최소 범위
    upper_bound = 100 #최대 범위

    while True:
        for player in players:
            print(f"{player.name}님의 차례입니다.")
            if player.is_user:
                print(f"가능한 숫자 범위: {lower_bound} ~ {upper_bound}")
                guess = input(f"{lower_bound}부터 {upper_bound} 사이의 숫자를 맞춰보세요: ")
            else:
                available_numbers = list(set(range(lower_bound, upper_bound + 1)) - used_numbers)
                if not available_numbers:
                    print(f"더 이상 선택할 수 있는 숫자가 없습니다. {player.name}님의 패배입니다!")
                    player.drink()
                    display_players(players)
                    if player.is_intoxicated():
                        return
                    return
                guess = str(random.choice(available_numbers))
                print(f"{player.name}: {guess}")
            #입력된 숫자가 범위 내에 있는지 확인하는 try-except 문
            try:
                guess = int(guess)
                if guess < lower_bound or guess > upper_bound or guess in used_numbers:
                    raise ValueError
            except ValueError:
                print(f"잘못된 입력입니다. {lower_bound}부터 {upper_bound} 사이의 사용되지 않은 숫자를 입력하세요.")
                continue

            used_numbers.add(guess)

            if guess == target:
                print(f"정답입니다! {player.name}님이 벌칙을 받습니다!")
                player.drink()
                display_players(players)
                if player.is_intoxicated():
                    return
                return
            elif guess < target:
                print("Up!")
                lower_bound = guess + 1
            else:
                print("Down!")
                upper_bound = guess - 1

        if lower_bound > upper_bound:
            print("더 이상 가능한 숫자가 없습니다. 게임을 종료합니다.")
            return