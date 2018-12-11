
'''

perception -> rozpoznanie
endurance -> vydrz
charisma -> charizma kokot -.-
agility -> obratnost
inteligence
class_type -> mage/rough/etc ....

helma
chestplate
nohavice
topanky
rukavice
2x prsten
1x nahrdelnik


'''


class New_Player:
    def __init__(self,class_type, strength, inteligence, agility, perception, endurance, charisma):
        self.hp = 100
        self.class_typ = class_type
        self.strength = strength
        self.inteligence = inteligence
        self.agility = agility
        self.perception = perception
        self.endurance = endurance
        self.charisma = charisma
        # self.inhand = Weapon(stick)
        # self.offhand = Defence(wooden_plate)
        # self.helmet = Item(default_helmet)
        # self.chestplate = Item(default_chestplate)
        # self.leggins = Item(default_leggins)
        # self.shoes = Item(default_shoes)
        # self.gloves = Item(default_gloves)
        # self.ring1 = Item(default_ring)
        # self.ring2 = Item(default_ring)
        # self.necklece = Item(default_necklace)


class Load_Player:
    def __init__(self):
        with open("player",'r') as f:
            counter = 0
            for line in f:
                if counter == 0:
                    (hp, class_type, strength, inteligence, agility, perception, endurance, charisma) =line.split(';')
                    self.hp = hp
                    self.class_typ = class_type
                    self.strength = strength
                    self.inteligence = inteligence
                    self.agility = agility
                    self.perception = perception
                    self.endurance = endurance
                    self.charisma = charisma
                if counter == 1:
                    self.inhand = Weapon(stick)
                if counter == 2:
                    self.offhand = Defence(wooden_plate)
                if counter == 3:
                    self.helmet = Item(default_helmet)
                if counter == 4:
                    self.chestplate = Item(default_chestplate)
                if counter == 5:
                    self.leggins = Item(default_leggins)
                if counter == 6:
                    self.shoes = Item(default_shoes)
                if counter == 7:
                    self.gloves = Item(default_gloves)
                if counter == 8:
                    self.ring1 = Item(default_ring)
                if counter == 9:
                    self.ring2 = Item(default_ring)
                if counter == 10:
                    self.necklece = Item(default_necklace)
                line.split(';')


class Player:
    def __init__(self, X_Player):
        self.hp = 100
        self.class_typ = X_Player.class_type
        self.strength = X_Player.strength
        self.inteligence = X_Player.inteligence
        self.agility = X_Player.agility
        self.perception = X_Player.perception
        self.endurance = X_Player.endurance
        self.charisma = X_Player.charisma

    def change_strength(self, addition):
        self.strength += addition

    def change_inteligence(self, addition):
        self.inteligence += addition

    def change_agility(self, addition):
        self.agility += addition

    def change_perception(self, addition):
        self.perception += addition

    def change_endurance(self, addition):
        self.endurance += addition
