class car:
    def _init_(self,model,make,year_of_manufacture,enginecapacity):
        self.model = model
        self.make = make
        self.year_of_manufacture = year_of_manufacture
        self.enginecapacity = enginecapacity

    def get_model(self):
        return self.model
    def get_make(self):
        return self.make
    def get_year_of_manufacture(self):
        return self.year_of_manufacture
    def get_engine_capacity(self):
        return self.enginecapacity
    def set_model (self.model):
        self.model = "model"
    def set_make ( self.make):
        self.make = "make"
    def set_year_of_manufacture(self.year_of_manufacture):
        self.year_of_manufacture = "year_of_manufacture"
    def set_enginecapacity(enginecapacity):
        self.enginecapacity = "enginecapacity"

car1 = car("demio","nissan",2018,1300)
car2 = car("hilux","toyota",2020,3500)
car3 = car("passat","vw",2009,2600)
print(car1.get_model())
print(car1.get_make())
print(car1.get_year_of_manufacture())
print(car1.get_enginecapacity())

print(car2.get_model())
print(car2.get_make())
print(car2.get_year())
print(car2.get_enginecapacity())

print(car3.get_model())
print(car3.get_make())
print(car3.get_year())
print(car3.get_enginecapacity())
