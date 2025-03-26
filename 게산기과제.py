select = input("1. 수식계산, 2.두 수 사이 합계\n선택>")
if select == "1":
    print("결과:", eval(input("수식을 입력하세요.")))
elif select == "2":
    a = int(input("첫 번째 숫자를 입력하세요 :"))
    b = int(input("두 번째 숫자를 입력하세요 :"))
    오름차순 = sorted([a, b])
    result = (오름차순[1] * (오름차순[1] + 1) - (오름차순[0]-1) * 오름차순[0])/ 2
    print(f"{a}부터 {b}까지의 합={result}")
else:
    print("1과 2 중에서 선택하세요.")
