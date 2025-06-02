import threading

## 합을 계산하는 함수 ##
def calculate_sum(start, end):
    total = sum(range(start, end + 1))
    print(f"{start}~{end}까지의 합: {total}")

## 스레드 생성 및 실행 ##
th1 = threading.Thread(target=calculate_sum, args=(1, 1000))
th2 = threading.Thread(target=calculate_sum, args=(1, 100000))
th3 = threading.Thread(target=calculate_sum, args=(1, 10000000))

th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()