#인치를 float로 입력받기
inch = float(input("인치를 입력하세요 : "))

#인치를 cm로 변환
cm = inch*2.54

#결과 출력, 소수잠 아래 3번째자리까지만 표시
print(f"cm로 변환하면 {cm:.3f}입니다.")