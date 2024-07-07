#up and down 함수만 구현되어있음.
def play_updown(players):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                    Up & Down 게임을 시작합니다!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    target = random.randint(1, 100)

    while True:
        for player in players:
            print(f"{player.name}님의 차례입니다.")
            if player.is_user:
                guess = input("1부터 100 사이의 숫자를 맞춰보세요: ")
            else:
                guess = str(random.randint(1, 100))
                print(f"{player.name}: {guess}")

            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    raise ValueError
            except ValueError:
                print("잘못된 입력입니다. 1부터 100 사이의 숫자를 입력하세요.")
                continue

            if guess == target:
                print(f"정답입니다! {player.name}님이 벌칙을 받습니다!")
                player.drink()
                display_players(players)
                if player.is_intoxicated():
                    return
                return  # 게임 종료 후 다른 게임으로 이동
            elif guess < target:
                print("Up!")
            else:
                print("Down!")