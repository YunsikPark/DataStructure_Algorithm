# 경찰이 있고
# 총이 있는 경찰
# 총이 없는 경찰

# 총
# 이름(멤버)
# 발사(메서드)

# is-a
# laptop IS A computer(랩탑컴퓨터는 컴퓨터의 일종)
# has-a
# A policeman has a gun(소유, 가지고 있음을 구현하는 것)

# is-a: 상속으로 구현

# 객체 합성: has-a 상태를 구현(과거에는 상속을 받았었지만 현재는 쓰지 않는다.)
# class Policeman(Gun):
#     def __init__(self):
#         self.gun = None
#
#     def set_gun(self, gun):
#         self.gun = gun


class Gun:
    def __init__(self, name):
        self.name = name

    def shoot(self):
        print("bbang")


class Policeman:
    def __init__(self):
        self.gun = None

    def set_gun(self, gun):
        self.gun = gun

