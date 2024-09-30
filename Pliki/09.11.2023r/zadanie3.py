class Car():
   type = "mk5"
   def wheels_get(self):
      return self.wheels
   def wheels_set(self, wheels):
      self.wheels = wheels
   def info():
      print("Hello World!!")
   def __init__(self, marka):
      self.marka = marka
class Electric(Car):
  def __init__(self,marka, wheels):
     self.marka = marka
     self.wheels = wheels
car_1 = Electric( "Mercedes","four wheeler")
car_1.wheels_set("two wheeler")
print(Car.type)
print(car_1.wheels_get())