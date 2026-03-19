from classes.car import Car

Ford = Car("ABC-123", 142)

Ford.accelerate(30)
Ford.accelerate(70)
Ford.accelerate(50)
print(f"The current speed of the car is: {Ford.cur_speed}")

Ford.accelerate(-200)
print(f"The current speed of the car is: {Ford.cur_speed}")