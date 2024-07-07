# 서울 지하철 1호선 역 목록
line_1 = [
    "소요산", "동두천", "보산", "동두천중앙", "지행", "덕정", "덕계", "양주", "녹양", "가능", "의정부",
    "회룡", "망월사", "도봉산", "도봉", "방학", "창동", "녹천", "월계", "광운대", "석계", "신이문",
    "외대앞", "회기", "청량리", "제기동", "신설동", "동묘앞", "동대문", "종로5가", "종로3가", "종각",
    "시청", "서울역", "남영", "용산", "노량진", "대방", "신길", "영등포", "신도림", "구로", "구일",
    "개봉", "오류동", "온수", "역곡", "소사", "부천", "중동", "송내", "부개", "부평", "백운", "동암",
    "간석", "주안", "도화", "제물포", "도원", "동인천", "인천"
]

# 서울 지하철 2호선 역 목록
line_2 = [
    "시청", "을지로입구", "을지로3가", "을지로4가", "동대문역사문화공원", "신당", "상왕십리", "왕십리",
    "한양대", "뚝섬", "성수", "건대입구", "구의", "강변", "잠실나루", "잠실", "잠실새내", "종합운동장",
    "삼성", "선릉", "역삼", "강남", "교대", "서초", "방배", "사당", "낙성대", "서울대입구", "봉천",
    "신림", "신대방", "구로디지털단지", "대림", "신도림", "문래", "영등포구청", "당산", "합정", "홍대입구",
    "신촌", "이대", "아현", "충정로"
]

# 서울 지하철 3호선 역 목록
line_3 = [
    "대화", "주엽", "정발산", "마두", "백석", "대곡", "화정", "원당", "원흥", "삼송", "지축", "구파발",
    "연신내", "불광", "녹번", "홍제", "무악재", "독립문", "경복궁", "안국", "종로3가", "을지로3가",
    "충무로", "동대입구", "약수", "금호", "옥수", "압구정", "신사", "잠원", "고속터미널", "교대",
    "남부터미널", "양재", "매봉", "도곡", "대치", "학여울", "대청", "일원", "수서", "가락시장", "경찰병원",
    "오금"
]

# 서울 지하철 4호선 역 목록
line_4 = [
    "당고개", "상계", "노원", "창동", "쌍문", "수유", "미아", "미아사거리", "길음", "성신여대입구",
    "한성대입구", "혜화", "동대문", "동대문역사문화공원", "충무로", "명동", "회현", "서울역", "숙대입구",
    "삼각지", "신용산", "이촌", "동작", "총신대입구", "사당", "남태령", "선바위", "경마공원", "대공원",
    "과천", "정부과천청사", "인덕원", "평촌", "범계", "금정", "산본", "수리산", "대야미", "반월",
    "상록수", "한대앞", "중앙", "고잔", "초지", "안산", "신길온천", "정왕", "오이도"
]


import random



def play_subway(players:list):
    print("___________________________________________")
    print("_______지하철 지하철 몇호선 몇호선___________")
    print("___________________________________________")
    print("")
    print("")

    start_player = players[0]
    line_list = [line_1, line_2, line_3, line_4]
    line_num = 0
    

    if start_player.is_user:
        while True:
            try:
                line_num = int(input("원하는 호선은? (1~4 숫자로 입력하기)"))
                if 1<=line_num<=4:
                    break
                else:
                    print("범위에 있는 숫자를 입력해 주세요.")
            except:
                print("숫자를 입력해 주세요.")
    else:
        line_num = random.randint(1,5)

    print(f'{line_num}호선 {line_num}호선')
    print("게임 시작!!!!")

    speaked_station = []

    cnt = 0

    while True:
        game_player = players[cnt%len(players)]

        # 플레이어가 사람일 때
        if game_player.is_user:
            print(f'{game_player.name}:  ', end = "")
            answer = input()
            if answer in speaked_station:
                print('집중은 생명! 집중은 생명!')
                print(f'누가 술을 마셔 {game_player.name}이(가) 술을 마셔 원샷!!')
                break
            elif answer in line_list[line_num-1]:
                cnt +=1
                speaked_station.append(answer)
                print("통과")
            else:
                print(f'{line_num}호선에 그런 역은 없! 어! 요!')
                print(f'누가 술을 마셔 {game_player.name}이(가) 술을 마셔 원샷!!')
                game_player.drink(1)
                break

        else:
            # 확률생성기(1~10까지 숫자중 1~7이 나오면 해당 호선에 맞는 대답, 아니면 다른 호선 말하기)
            random_num = random.randint(1,11)

            print(f'{game_player.name}:  ', end = "")

            if random_num <=7:
                answer = random.choice(line_list[line_num])
                print(answer)
                if answer in speaked_station:
                    print('집중은 생명! 집중은 생명!')
                    print(f'누가 술을 마셔 {game_player.name}이(가) 술을 마셔 원샷!!')
                    break
                else:
                    cnt +=1
                    speaked_station.append(answer)
                    print("통과")
            else:
                incorrect_line = range(1,5).pop(line_num-1)
                answer = random.choice(line_list[random.choice(incorrect_line)])
                print(answer)
                print(f'{line_num}호선에 그런 역은 없! 어! 요!')
                print(f'누가 술을 마셔 {game_player.name}이(가) 술을 마셔 원샷!!')
                game_player.drink(1)
                break