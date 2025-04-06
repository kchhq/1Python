#f-string 사용한 버전
numbers1 = [2,3,4,5,6,7,8,9]
numbers2 = [1,2,3,4,5,6,7,8,9]

for num1 in numbers1 :
    print(f"#   {num1}단   #", end =' ')


for num2 in numbers2 :
    print()
    for num1 in numbers1 :
        if num1*num2<10 :
            print(f"{num1}X   {num2}=  {num1 * num2} ", end=' ')
        else :
            print(f"{num1}X   {num2}= {num1 * num2} ", end=' ')
