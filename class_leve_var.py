class car:
    #class level varable 
    wheels = 4
    def __init__(self):
        milage = 10
        brand = "bmw"
    
car1 = car()
car2 = car()
car1.milage = 8
car1.brand = "ferari"

print(car1.milage, car1.brand,car1.wheels )

print(car2.milage, car2.brand,car2.wheels )


        