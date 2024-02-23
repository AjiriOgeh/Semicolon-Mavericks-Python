class Bullet:
    def __init__(self, gun_for_bullet):
        self.gun_for_bullet = gun_for_bullet
    


class Magazine:
    #it is an array of bullets
    def __init__(self, gun_type):
        self.gun_type = gun_type


class Gun:
    gun_chamber = []

    def __init__(self, gun_type):
        self.gun_type = gun_type

    def fire(self, bullet):
        if len(self.gun_chamber) <= 0:
            raise ValueError
        else:
            self.gun_chamber.remove(bullet)

    def load(self, bullet):
        if len(self.gun_chamber) >= 6:
            raise ValueError
        elif bullet.gun_for_bullet != self.gun_type:
            raise ValueError
        else:
            self.gun_chamber.append(bullet)

    def check_ammunition(self):
        return len(self.gun_chamber)
