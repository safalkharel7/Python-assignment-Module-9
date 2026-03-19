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
        self.distance = self.distance + self.cur_speed * hours

    def get_info(self):
        return {"reg_num":self.reg_num, "max_speed":self.max_speed,
                "cur_speed": self.cur_speed, "distance":self.distance}