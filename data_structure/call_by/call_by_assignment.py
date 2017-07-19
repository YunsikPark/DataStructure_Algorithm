class Base:
    def __init__(self, a):
        self.a = a

    def set_a(self, new_a):
        self.a = new_a

def func(b, data):
    b.set_a(data)     # 아래의 결과 b값이 바뀐다. 함수가 끝나도 스텍에 b값이 날아가기 때문
    # b = Base(data)      # 아래의 결과 b값이 안바뀐다. 함수가 끝나면 스텍에서 사라지기때문

if __name__ == "__main__":
    b = Base(4)
    func(b, 10)
    print(b.a)
