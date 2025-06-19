import random

def generate_number(max_value):
    """
    1부터 max_value 사이의 무작위 정수를 생성
    """
    return random.randint(1, max_value)

def get_user_guess(max_value):
    """
    사용자로부터 정수 입력을 받아 반환
    유효하지 않은 입력은 재시도
    """
    while True:
        try:
            print("\n")
            guess = int(input(f"➡ 숫자를 입력하세요. (1~{max_value}) : "))
            if 1 <= guess <= max_value:
                return guess
            else:
                print(f"1에서 {max_value} 사이의 숫자를 입력해주세요.")
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

def get_max_value():
    """
    사용자에게 최대 숫자 범위(MAX VALUE)를 입력받아 반환
    """
    while True:
        try:
            max_val = int(input("최대 숫자 범위를 입력하세요. (예 : 100, 200): "))
            if max_val > 1:
                return max_val
            else:
                print("최소 2 이상의 숫자를 입력해주세요.")
        except ValueError:
            print("정수를 입력해주세요.")

def get_max_attempts():
    """
    사용자에게 최대 시도 횟수를 입력받아 반환
    """
    while True:
        try:
            max_attempts = int(input("최대 시도 횟수를 입력하세요. (무제한은 0) : "))
            if max_attempts >= 0:
                return max_attempts
            else:
                print("0 이상의 숫자를 입력해주세요.")
        except ValueError:
            print("정수를 입력해주세요.")


def print_intro():
    """
    게임 인트로 출력
    """
    print("=" * 50)
    print("    🎯 숫자 맞추기 게임에 오신 것을 환영합니다! 🎯 ")
    print("=" * 50)
    print("컴퓨터가 1부터 설정한 숫자 범위 내에서 무작위 숫자를 선택하며, 당신은 그 숫자를 맞춰야 합니다!")
    print("\n")

def play_game():
    """
    숫자 맞추기 게임을 실행
    """
    print_intro()
    max_val = get_max_value()
    max_attempts = get_max_attempts()
    target_number = generate_number(max_val)
    attempts = 0
    hint_min = 1
    hint_max = max_val

    while True:
        print("-" * 50)  # 구분선
        guess = get_user_guess(max_val)
        attempts += 1
        result = check_guess(target_number, guess)
        print(f"\n📢 결과 : {result}")

        if guess == target_number:
            print(f"\n🎉 {attempts}번 만에 숫자를 맞추셨습니다. 축하합니다!")
            break

        # 힌트 범위 업데이트
        if guess < target_number and guess + 1 <= hint_max:
            hint_min = max(hint_min, guess + 1)
        elif guess > target_number and guess - 1 >= hint_min:
            hint_max = min(hint_max, guess - 1)
        print(f"\n💡 힌트 : 정답은 {hint_min} ~ {hint_max} 사이에 있습니다.\n")

        if max_attempts != 0:
            remaining = max_attempts - attempts
            print(f"⏳ 남은 시도 : {remaining}번\n")
            if remaining <= 0:
                print("\n" + "=" * 50)
                print(f"💥 기회를 모두 사용하셨습니다. 정답은 {target_number}였습니다!")
                print("=" * 50)
                break

if __name__ == "__main__":
    play_game()