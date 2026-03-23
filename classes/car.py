class Car:
    def __init__(self,reg_num:str ,max_speed:float, cur_speed = 0, distance = 0):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.cur_speed = cur_speed
        self.distance = distance
    def accelerate(self, change):
        self.cur_speed += change
        if self.cur_speed<0:
            self.cur_speed = 0
        if self.cur_speed>self.max_speed:
            self.cur_speed = self.max_speed

    def drive(self, hours):
        self.distance += self.cur_speed * hours

    def get_info(self):
        return {"reg_num":self.reg_num, "max_speed":self.max_speed,
                "cur_speed": self.cur_speed, "distance":self.distance}