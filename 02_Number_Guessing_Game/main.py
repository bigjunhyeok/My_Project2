import random

def generate_number(min_value=1, max_value=100):
    """
    지정된 범위에서 무작위 정수를 생성합니다.
    """
    return random.randint(min_value, max_value)

def get_user_guess():
    """
    사용자로부터 정수 입력을 받아 반환합니다.
    유효하지 않은 입력은 재시도합니다.
    """
    while True:
        try:
            guess = int(input("숫자를 입력하세요 (1~100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("1에서 100 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("유효한 숫자를 입력해주세요.")

def check_guess(target, guess):
    """
    사용자의 추측을 실제 숫자와 비교하고 결과 문자열을 반환합니다.
    """
    if guess < target:
        return "너무 낮아요!"
    elif guess > target:
        return "너무 높아요!"
    else:
        return "정답입니다!"

def play_game():
    """
    숫자 맞추기 게임을 실행합니다.
    """
    print("숫자 맞추기 게임에 오신 것을 환영합니다!")
    target_number = generate_number()
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1
        result = check_guess(target_number, guess)
        print(result)

        if guess == target_number:
            print(f"{attempts}번 만에 숫자를 맞추셨습니다. 축하합니다!")
            break

if __name__ == "__main__":
    play_game()