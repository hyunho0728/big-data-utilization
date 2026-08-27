import random as r

print('업다운 게임')
print('='*50)

number = r.randint(1, 99)        # number 변수에 1~99사이의 난수를 생성.
count = 10                       # 사용자가 입력할 수 있는 횟수.

while count > 0:
    #print(number)  # 정답 확인용
    user = int(input('생각한 숫자를 입력하세요(1~99) : '))
    count -= 1
    
    if user == number:
        print('정답입니다.')
        break
    elif user < number:
        print('up! (남은 기회 : %d회)' % count)
    else:
        print('down! (남은 기회 : %d회)' % count)