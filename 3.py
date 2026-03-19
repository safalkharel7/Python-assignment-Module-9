from classes.car import Car

Ford = Car("ABC-123", 142)
Ford.distance = 2000
Ford.accelerate(60)
print(f"The new car with registration number {Ford.reg_num} is {Ford.max_speed} km/h.")
Ford.drive(1.5)
print(f"The current distance travelled is {Ford.distance:.2f} kilometers.")