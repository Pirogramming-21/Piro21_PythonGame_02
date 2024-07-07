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
