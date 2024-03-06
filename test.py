import random

def 가위바위보():

    # 가위: 1
    # 바위: 2
    # 보: 3

    user_input = int(input("1: 가위, 2: 바위, 3: 보"))
    bot_input = random.randint(1,3)

    if user_input == 1:
        if bot_input == 1:
            print("당신: 가위, 봇: 가위 -> 비겼습니다")
        elif bot_input == 2:
            print("당신: 가위, 봇: 바위 -> 졌습니다")
        else:
            print("당신: 가위, 봇: 보 -> 이겼습니다")

    elif user_input == 2:
        if bot_input == 1:
            print("당신: 바위, 봇: 가위 -> 이겼습니다")
        elif bot_input == 2:
            print("당신: 바위, 봇: 바위 -> 비겼습니다")
        else:
            print("당신: 바위, 봇: 보 -> 졌습니다")

    else:
        if bot_input == 1:
            print("당신: 보, 봇: 가위 -> 졌습니다")
        elif bot_input == 2:
            print("당신: 보, 봇: 바위 -> 이겼습니다")
        else:
            print("당신: 보, 봇: 보 -> 비겼습니다")

가위바위보()