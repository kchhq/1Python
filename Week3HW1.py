print("입력 진수 결정 (16/10/8/2) : ")
a = int(input())

print("값 입력 : ")
b = input()

print("\n16진수 ==> ", hex(int(b,a)))
print("\n10진수 ==> ", int(b,a))
print("\n8진수 ==> ", oct(int(b,a)))
print("\n2진수 ==> ", bin(int(b,a)))



