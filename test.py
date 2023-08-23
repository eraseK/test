# up down 게임
import random


test = 0

num = random.randint(1,100)
while True:
    try:
        x = int(input('숫자를 입력해주세요 : '))
    except:
        print("숫자를 입력해주세요")
        continue
    if x < 1 or x > 100:
        print('1~100사이의 숫자를 입력해주세요')
        continue
    if num > x:
        print('UP')
    if num < x:
        print('DOWN')
    test += 1
    if num == x:
        print(f'정답입니다!@! {test}번만에 맞추셨습니다!')

        a = input('게임을 계속 진행하시겠습니까? (y/n)')
        if a == 'y':
            test = 0
            num = random.randint(1, 100)
            continue
        else:
            print('게임을 종료합니다.')
            break

# 가위바위보
import random
list = ['가위','바위','보']

choice = random.choice(list)

while True:
    print('게임을 시작하려면 엔터, 종료 하려면 아무 글자나 입력해주세요')
    a = input('>')
    if a == '':
        print('가위바위보 게임을 진행합니다. 가위 바위 보 중 하나 입력해주세여')
        b = input('>>')
        if b == choice:
            print('비겼습니다!')
            choice = random.choice(list)
            continue
        if b == '가위' and choice == '보':
            print('이겼습니다!')
            choice = random.choice(list)
            continue
        if b == '가위' and choice == '바위':
            print('졌습니다ㅠㅠ!')
            choice = random.choice(list)
            continue
        if b == '보' and choice == '바위':
            print('졌습니다ㅠㅠ!')
            choice = random.choice(list)
            continue
        if b == '보' and choice == '가위':
            print('이겼습니다!')
            choice = random.choice(list)
            continue
        if b == '바위' and choice == '가위':
            print('이겼습니다!')
            choice = random.choice(list)
            continue
        if b == '바위' and choice == '보':
            print('졌습니다ㅠㅠ')
            choice = random.choice(list)
            continue

    else:
        print('게임을 종료합니다.')
        break



#3번째
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'name : {self.name}  username : {self.username}')

class post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

members = []
m1 = Member('kim', 'kk','1234')
m2 = Member('lee', 'll','1234')
m3 = Member('kang', 'gg','1234')
members.append(m1)
members.append(m2)
members.append(m3)

for mem in members:
    print(f'name : {mem.name}, usernaem : {mem.username}')

p1 = post('안녕하세영','잘부탁드립니당',m1.username)
p2 = post('두번째 글','둘둘둘둘',m1.username)
p3 = post('세번째','세세세셋',m1.username)

o1 = post('안녕하세요','하나하나',m2.username)
o2 = post('두번째 글','둘둘둘둘',m2.username)
o3 = post('세번째','셋둘하나',m2.username)

s1 = post('잘부탁','하나',m3.username)
s2 = post('꺄르를','둘둘둘둘',m3.username)
s3 = post('세번째','잘부탁드려요',m3.username)

po = []

po.append(p1)
po.append(p2)
po.append(p3)
po.append(o1)
po.append(o2)
po.append(o3)
po.append(s1)
po.append(s2)
po.append(s3)

for idx, st in enumerate(po,start=1):
    # if '안녕' in st.title:
    #     print(f'{idx}. 제목 : {st.title}    내용 : {st.content}    작성자 : {st.author}')
    # if 'kk' == st.author:
    #     print(f'{idx}. 제목 : {st.title}    내용 : {st.content}    작성자 : {st.author}')
    print(f'{idx}. 제목 : {st.title}    내용 : {st.content}    작성자 : {st.author}')


# 터미널에 입력하기

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'name : {self.name}  username : {self.username}')

class post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

members = []

name = input('name : ')
username = input('username : ')
password = input('password : ')

m1 = Member(name, username, password)
m1.display()

title = input('제목 : ')
content = input('내용 : ')
p1 = post(title,content,m1.username)

print(p1.title, p1.content, p1.author)

