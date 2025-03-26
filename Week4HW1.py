def calc_2(a, b) :
    if a>b :
        a, b = b, a
    return sum(range(a,b+1))

OR = int(input(("1. 입력한 수식 계산 2. 두 사이의 합계 : ")))
 
if OR == 1 :
    expression = input("*** 수식을 입력하세요 : ")
    result = eval(expression)
    print(f"{expression}결과는 {result}입니다.")

elif OR == 2:
    num1 = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("*** 두 번째 숫자를 입력하세요 : "))
    sum = calc_2(num1, num2)
    print(f"{num1}+...+{num2}는 {sum}입니다.")

else :
    print("입력이 잘못되었습니다. 1 또는 2를 입력해주세요. ")
