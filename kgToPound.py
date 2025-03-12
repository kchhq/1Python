#kg을 float로 입력받음
kg = float(input("킬로그램을 입력하세요 : "))

#kg을 pound로 변환
pound = kg*2.20462

#결과 출력, 소수점 아래 3자리까지만 표시
print(f"파운드로 변환하면 {pound:.3f}입니다.")