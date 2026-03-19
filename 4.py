class Car:
    def __init__(self,newcar_reg_num:str ,newcar_max_speed:float):
        self.reg_num = newcar_reg_num
        self.max_speed = newcar_max_speed
        self.cur_speed = 0
        self.distance = 0
    def accelerate(self, change):
        self.cur_speed = self.cur_speed + change
        if self.cur_speed<0:
            self.cur_speed = 0
        if self.cur_speed>self.max_speed:
            self.cur_speed = self.max_speed
    def drive(self, hours):
        self.distance = 0
        self.cur_speed = 60
        self.distance = self.distance + self.cur_speed * hours
import random
count = 0
while count < 2:
    name = input("Enter the car name: ")
    speed = random.randint(100,200)
    reg = ("ABC-"+ str(count+1))
    print(f"Name: {name}, Registration num: {reg} Max speed: {speed}")
    count = count + 1