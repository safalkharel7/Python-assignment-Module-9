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

Cars = []
count = 0
while count < 5:
    car = input("Enter the car name: ")
    Cars.append(car)
    count += 1
print(Cars)
import random
for car in Cars:
    max_speed = random.randint(100,200)
    car.max_speed = max_speed
    car.reg_num = ("ABC -"+str(count))
    print(f"The {car} registered as {car.reg_num} has a max speed of {car.max_speed}")