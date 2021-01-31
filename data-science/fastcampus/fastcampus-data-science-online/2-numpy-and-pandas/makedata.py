
# 사람의 이름과 나이가 들어간 데이터를 만듭니다.
import random
import numpy as np

# 랜덤한 이름 출력하는 함수
def get_name():
    names = ["Adam", "Alan", "Alex", "Alvin", "Andrew",
             "Anthony", "Arnold", "Jin", "Billy", "Anchal"]
    return random.choice(names)

# 랜덤한 나이 출력
def get_age(start=20, end=40):
    return np.random.randint(start, end + 1)

# 랜덤하게 나이와 이름을 출력
def make_data(rows=10):
    datas = []
    for _ in range(rows):
        data = {"Age": get_age(), "Name": get_name()}
        datas.append(data)
    return datas
