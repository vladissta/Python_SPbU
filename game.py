import math
import random
from abc import ABC, abstractmethod


class Location:
    def __init__(self, name: str, width: int, height: int, length: int):
        self.name = name
        self._width = width
        self._height = height
        self._length = length
        self._objs = []

    def addObject(self, obj):
        if obj not in self._objs:
            self._objs.append(obj)

    def clear(self):
        self._objs = None

    def isInside(self, x, y, z) -> bool:
        return ((0 < x < self._length)
                and (0 < y < self._width)
                and (0 < z < self._height))

    @property
    def width(self):
        return self._width

    @property
    def length(self) -> int:
        return self._length

    @property
    def height(self):
        return self._height

    @property
    def volume(self):
        return self.height * self.length * self.width


class GameObject:
    def __init__(self, name: str, loc: Location, x, y, z):
        self.name = name
        self._loc = loc
        self._loc.addObject(self)
        self.x, self.y, self.z = x, y, z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            self._x = 0
        elif self._loc.length < x:
            self._x = self._loc.length
        else:
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if y < 0:
            self._y = 0
        elif self._loc.width < y:
            self._y = self._loc.width
        else:
            self._y = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        if z < 0:
            self._z = 0
        elif self._loc.height < z:
            self._z = self._loc.height
        else:
            self._z = z

    def move(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z

    def distance(self, obj):
        dx = self.x - obj.x
        dy = self.y - obj.y
        dz = self.z - obj.z
        r2 = dx ** 2 + dy ** 2 + dz ** 2
        return int(math.sqrt(r2))


class LivingObject(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, hp: int):
        super().__init__(name, loc, x, y, z)
        self._max_hp = hp
        self._hp = hp

    @property
    def maxHP(self):
        return self._max_hp

    @property
    def hp(self):
        return self._hp

    def changeHP(self, change):
        if not self.alive:
            return
        self._hp += change
        if self._hp < 0:
            self._hp = 0
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    @property
    def alive(self):
        return self._hp > 0

    def eat(self, obj):
        if self.distance(obj) > 1:
            return
        self.changeHP(obj.eatMe())


class Weapon(GameObject):
    def __init__(self, name: str, loc: Location, x, y, z, damage, radius):
        super().__init__(name, loc, x, y, z)
        self._damage = damage
        self._radius = radius

    @property
    def damage(self):
        return self._damage

    @property
    def radius(self):
        return self._radius

    def attack(self, obj: LivingObject):
        d = self.distance(obj)
        if d > self.radius:
            return
        obj.changeHP(-self.damage)
        print(f'{obj.name} was attacked by {self.name}')
        print(f'{obj.name}: {obj.hp} HP')


class EdgedWeapon(Weapon):

    def __init__(self, name: str, loc: Location, x, y, z, damage, radius, crit_damage: float):
        super().__init__(name, loc, x, y, z, damage, radius)
        self.crit_damage = crit_damage

    def attack(self, obj: LivingObject):
        d = self.distance(obj)
        if d > self.radius:
            return
        obj.changeHP(- self.damage - (random.random() > 0.8) * self.crit_damage)
        print(f'{obj.name} was attacked by {self.name}')
        print(f'{obj.name}: {obj.hp} HP')


class ThrowingWeapon(Weapon):

    def throw(self, target_x, target_y, target_z):

        point_target = GameObject('point', self._loc,
                                  x=target_x, y=target_y, z=target_z)

        d = self.distance(point_target)
        if d > self.radius:
            print('Too far to throw')
            return
        else:
            print(f'{self.name} thrown to {target_x} {target_y} {target_z}')
            self.x = target_x
            self.y = target_y
            self.z = target_z


class Player(LivingObject):

    def __init__(self, name: str, loc: Location, x, y, z, hp: int, equipping_radius: int):
        super().__init__(name, loc, x, y, z, hp)
        self.equipping_radius = equipping_radius
        self.weapon = None

    def equip_weapon(self, weapon: Weapon):
        """
        Equip weapon that can be used calling its methods - e.g. weapon.throw() or weapon.attack(obj)

        :param weapon: Weapon object
        :return: None
        """
        if self.equipping_radius >= self.distance(weapon):
            weapon.x, weapon.y, weapon.z = self.x, self.y, self.z
            self.weapon = weapon
            print(f'{self.weapon.name} was equipped by {self.name}')
        else:
            print("To far to handle!")
            return

    def attack(self, obj: LivingObject):
        if not self.weapon:
            print(f'{self.name} tried to attack, but has no weapon!')
            return
        self.weapon.attack(obj)
        if isinstance(self.weapon, ThrowingWeapon):
            self.weapon = None


class Eatable(ABC):
    def __init__(self, hp: int):
        self._hp = hp
        self._eaten = False

    @property
    def eaten(self):
        return self._eaten

    @abstractmethod
    def eatMe(self):
        if not self.eaten:
            self._eaten = True
            return self._hp
        else:
            return 0


class Food(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        Food.eatMe(self)


class Poison(GameObject, Eatable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)

    def eatMe(self):
        return -Eatable.eatMe(self)


class Burnable(ABC):
    def __init__(self):
        self._burned = False

    @property
    def burned(self):
        return self._burned

    @abstractmethod
    def burnMe(self):
        self._burned = True


class Cookable(GameObject, Eatable, Burnable):
    def __init__(self, name, loc, x, y, z, hp):
        GameObject.__init__(self, name, loc, x, y, z)
        Eatable.__init__(self, hp)
        Burnable.__init__(self)

    @classmethod
    def growMushroom(cls, loc, x, y, z):
        return cls('mushroom', loc, x, y, z, 20)

    def burnMe(self):
        Burnable.burnMe(self)

    def eatMe(self):
        hp = Eatable.eatMe(self)
        return hp if self.burned else -hp


if __name__ == '__main__':
    forest = Location('forest', 100, 100, 20)

    knife = EdgedWeapon('knife', forest, 1, 2, 1, 20, 5, crit_damage=50)
    grenade = ThrowingWeapon('grenade', forest, 1, 1, 1, 40, 4)

    human = Player('Sanya', forest, 1, 1, 1, 100, 5)
    enemy = Player('Baba Yaga', forest, 3, 2, 1, 100, 5)

    print(f"{human.name}: {human.hp} HP, {enemy.name}: {enemy.hp} HP")
    human.equip_weapon(knife)
    human.attack(enemy)

    enemy.equip_weapon(grenade)
    enemy.weapon.throw(2, 2, 2)
    human.equip_weapon(grenade)
    human.attack(enemy)
    human.attack(enemy)
