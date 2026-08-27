# 가위 바위 보 게임

import random as r

print('가위 바위 보 게임')
print('-'*50)

# '가위', '바위', '보' 중 하나를 선택해서 com에 저장    
com = r.choice(['가위', '바위', '보'])
user = input('가위, 바위, 보 중 하나를 선택하세요: ')

if user == com:
    print('무승부입니다.')
elif (user == '가위' and com == '보') or (user == '바위' and com == '가위') or (user == '보' and com == '바위'):
    print('사용자가 이겼습니다.')
else:
    print('컴퓨터가 이겼습니다.')