from classes.car import Car
from tabulate import tabulate
import random
carlist = []
for i in range(10): # can also use for i in range(1,11), 11 will be excluded
    reg_num = "ABC-" +str(i+1)   #then we do not use +1
    max_speed = random.randint(100,200)
    car = Car(reg_num, max_speed)
    carlist.append(car)

print(carlist)

for car in carlist:
    print(car.reg_num, car.max_speed)

race = True

while race:
    for car in carlist:
        acc = (random.randint(-15,10))
        car.accelerate(acc)
        car.drive(1)
        if car.distance >= 10000:
            race = False

printable_cars = []
for car in carlist:
    printable_cars.append(car.get_info())

tabulate = tabulate(printable_cars, headers="keys", tablefmt="psql")
print(tabulate)