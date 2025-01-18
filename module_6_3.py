import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_coords = [x + dx * self.speed for x in self._cords[:3]]
        if new_coords[2] < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = new_coords
            print(f"Moved to coordinates: X: {new_coords[0]}, Y: {new_coords[1]}, Z: {new_coords[2]}")

    def get_cords(self):
        return f"Cords: X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        num_eggs = random.randint(1, 4)
        print(f"Here are({num_eggs}) eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        new_z = max(0, self._cords[2] - abs(dz) * self.speed // 2)
        self._cords[2] = new_z



class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def speak(self):
        print(self.sound)

    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def make_sound(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()