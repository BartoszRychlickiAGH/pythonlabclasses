class Bike:  # definicja klasy
    vehicle_type = "two-wheeler"

    def __init__(self, wheel, color):
        self.wheel = wheel
        self.color = color

    def wheel_get(self):
        return self.wheel

    def color_get(self):
        return self.color

    def color_set(self, new_color):
        return new_color


my_Bike = Bike(2, "red")
print(my_Bike.vehicle_type)

print(my_Bike.wheel_get())
my_Bike.color_set("green")
print(my_Bike.color_get())
