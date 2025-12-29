class vehicle:

    def __init__(self, mark="Toyota", model="Corolla"):
        self.mark = mark
        self.model = model

    def moves(self):
        print(f"Vehicle {self.mark} {self.model} is moving")


my_vehicle = vehicle()
my_vehicle.moves()


class Airplane(vehicle):
    def moves(self):
        print("Airplane is flying...")


class truck(vehicle):
    def moves(self):
        print('Rumbles alonng...')


class GolCart(vehicle):
    pass


cessna = Airplane("Cessna", "Skyhawk")
mack = truck("Mack", "Pinnacle")
golfwagon = GolCart("Yamaha", "GC100")

cessna.moves()
mack.moves()
golfwagon.moves()


for v in (my_vehicle, cessna, mack, golfwagon):
    v.mark()
    v.moves()
