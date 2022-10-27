
class Robot:
    # constuktor
    def __init__(self, baterie, delka_rukou):
        self.bat = baterie
        self.del_ruk = delka_rukou
        self.ukony_do_kontroly = 1000

    def krok_vpred(self):
        print("Robot udelal krok vpred")
        self.ukony_do_kontroly -= 1
        print(f"Ukony do kontroly {self.ukony_do_kontroly}")

    def krok_vzad(self):
        print("Robot udělal krok vzad")
        self.ukony_do_kontroly -= 1
        print(f"Ukony do kontroly {self.ukony_do_kontroly}")
        

robot_1 = Robot(24, 0.6)
# tohle už nemusím psát, je to v zavorce - contruktoru
# robot_1.baterie = 24
# robot_1.delka_rukou = 0.6

robot_2 = Robot(48, 0.5)
# robot_2.baterie = 48
# robot_2.delka_rukou = 0.5

robot_3 = Robot(50, 0.8)
robot_4 = Robot(45, 0.2)
#
# print(robot_2.bat)
# print(robot_2.del_ruk)
# print(robot_3.ukony_do_kontroly)

robot_1.krok_vpred()
robot_1.krok_vzad()
