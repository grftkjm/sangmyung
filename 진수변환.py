x = int(input("입력 진수 결정. (16, 10, 8, 2): "))
y = input("변환할 값 입력: ")
if x in [16, 10, 8, 2]:
    if x == 16 :
        십진수 = int(y, 16)
    elif x == 10 :
        십진수 = int(y, 10)
    elif x == 8 :
        십진수 = int(y, 8)
    elif x == 2 :
        십진수 = int(y, 2)
    print(f"변환 진수: {x}\n입력값: {y}\n16진수==> {hex(십진수)}\n10진수==> {십진수}\n8진수==> {oct(십진수)}\n2진수==> {bin(십진수)}")
else:
    print("잘못된 진수를 선택했습니다.")

