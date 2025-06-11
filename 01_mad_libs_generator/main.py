import random

def get_user_input(prompt: str) -> str:
    """
    사용자 입력을 받으며, 공백이 입력되었을 경우 재입력 요청
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("입력은 비워둘 수 없습니다. 다시 입력해주세요.")


def generate_story(noun: str, verb: str, adjective: str, place: str) -> str:
    """
    다양한 스토리 템플릿 중 하나를 랜덤하게 선택하여 이야기 생성
    """
    templates = [
        f"오늘 나는 {place}에 갔다. 나는 {adjective} {noun}를(을) 보았고, 갑자기 그것이 {verb}기 시작했다!",
        f"{place}에서 나는 전혀 예상치 못한 {adjective} {noun}를(을) 만났고, 그것은 갑자기 {verb}기 시작했다.",
        f"그날 {place}에서는, 모든 것이 조용했지만 {adjective} {noun} 하나가 {verb}는 소리로 침묵을 깼다.",
        f"누군가 {place}에서 {adjective} {noun}를(을) 발견했고, 그것은 서서히 {verb}기 시작했다."
    ]
    return random.choice(templates)


def save_story_to_file(story: str, filename: str = "story.txt") -> None:
    """
    생성된 이야기를 텍스트 파일로 저장
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(story)

def show_intro():
    print("\033[95m" + "="*40)
    print("     이야기 생성기에 오신 것을 환영합니다")
    print("="*40 + "\033[0m\n")

def main():
    show_intro()

    noun = get_user_input("명사를 입력하세요 : ")
    verb = get_user_input("동사를 입력하세요 : ")
    adjective = get_user_input("형용사를 입력하세요 : ")
    place = get_user_input("장소를 입력하세요 : ")

    story = generate_story(noun, verb, adjective, place)

    print("\n📝 생성된 이야기 :")
    print(f"\033[92m{story}\033[0m")

    while True:
        save = input("\n이 이야기를 파일로 저장하시겠습니까? (y/n) : ").strip().lower()
        if save in ['y', 'n']:
            break
        print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

    if save == 'y':
        save_story_to_file(story)
        print("이야기가 'story.txt' 파일로 저장되었습니다.")

if __name__ == "__main__":
    main()