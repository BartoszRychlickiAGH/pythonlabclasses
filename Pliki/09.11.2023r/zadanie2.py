class Car:
    # konstruktor
    def __init__(self, wheels, engine, max_velocity, color, seats):
        self.wheels = wheels
        self.engine = engine
        self.max_velocity = max_velocity
        self.color = color
        self.seats = seats

    # gettery
    def wheels_get(self):
        return self.wheels

    def engine_get(self):
        return self.engine

    def max_velocity_get(self):
        return self.max_velocity

    def color_get(self):
        return self.color

    def seats_get(self):
        return self.seats

    # settery
    def wheels_set(self, new_wheels):
        self.wheels = new_wheels

    def engine_set(self, new_engine):
        self.engine = new_engine

    def max_velocity_set(self, new_max_velocity):
        self.max_velocity = new_max_velocity

    def color_set(self, new_color):
        self.color = new_color

    def seats_set(self, new_seats):
        self.seats = new_seats


car_1 = Car("four wheeler", "2.0 TDI", "270 km/h", "red", "5")
car_2 = Car("four wheeler", "1.2 DCI", "190 km/h", "green", "4")
car_3 = Car("four wheeler", "RB2", "340 km/h", "lime", "2")
car_3.color_set("Ocean Blue")
print(car_3.color_get())
# print(car_2.engine_get("2JZ")) - getter nie może zmienić wartości atrybutu gdyż jego jedynym zadaniem jest pobranie od użytkownika wartości danego atrybutu
