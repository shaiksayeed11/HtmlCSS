import time
class local:
    def __init__(self):
        name1="tcs"
        print(name1)
    def m1(self):
        name2="infosys"
        print(name2)
    @classmethod
    def m3(cls):
        name5="capgimini"
        print(name5)
    @staticmethod
    def m4():     #local varible
        name="google"
        print(name)
t=local()
t.m1()
t.m3()
t.m4()
time.sleep(1)
print("end of an application")