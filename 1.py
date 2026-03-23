from classes.car import Car

Ford = Car("ABC-123", 142)
print(f"\nNew Car properties:\n\nRegistration number:{Ford.reg_num}\nMax speed:{Ford.max_speed} km/h\nCurrent Speed:{Ford.cur_speed} km/h\nDistance Travelled:{Ford.distance} kilometers")