"""We have a class defined for vehicles. Create two new vehicles called car1 and car2.
Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00."""

class Vehicles:
    def __init__(self,model,prize,brand):
        self.model = model
        self.prize = prize
        self.brand = brand
    

car1 = Vehicles("Red Convertible", "$60,000","Fer")
car2 = Vehicles("Blue Van","$10,000","Jump")

print(f"I've recently purchased a {car1.model} costing {car1.prize} and named it {car1.brand}")

print(f"I also got another car  {car2.model} costing {car2.prize} and named it {car2.brand}")
    