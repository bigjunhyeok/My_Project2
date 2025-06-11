def main():
    # 사용자 입력 받기
    noun = input("명사를 입력하세요: ")
    verb = input("동사를 입력하세요: ")
    adjective = input("형용사를 입력하세요: ")
    place = input("장소를 입력하세요: ")

    # 스토리 템플릿
    story = f"오늘 나는 {place}에 갔다. 나는 {adjective} {noun}를(을) 보았고, 갑자기 그것이 {verb}기 시작했다!"

    # 결과 출력
    print("\n생성된 이야기:")
    print(story)

if __name__ == "__main__":
    main()