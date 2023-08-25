class Mechanic:
    def __init__(self, description, hp):
        self.description = description
        self.hp = hp

class Gate:
    def __init__(self, mechanics, names):
        self.mechanics = mechanics
        self.names = names
        
    def get_next_mechanic(self, hp):
        
        valid_mechanics = [mechanic for mechanic in self.mechanics if hp >= mechanic.hp]
        if valid_mechanics:
            return valid_mechanics[0]
        else:
            return Mechanic("Just kill", 1)

class Boss:
    def __init__(self, name, gates):
        self.name = name
        self.gates = gates

class Raids:
    def __init__(self):
        valtan_g1 = Gate([
            Mechanic("x30 Orbs", 30),
            Mechanic("x15 Orbs", 15)],
                         ["Dark Mountain Predator", "Leader Lugaru", "Destroyer Lucas"])
        valtan_g2 = Gate([
            Mechanic("x160 Armor break", 160),
            Mechanic("x130 Balthor", 130),
            Mechanic("x110 Pillars", 110),
            Mechanic("x85 Arena break", 85),
            Mechanic("x60 Counter", 60),
            Mechanic("x35 Arena break", 35),
            Mechanic("x15 Ghost phase", 15)],
                         ["Demon Beast Commander Valtan"])
        valtan_ghost = Gate([
            Mechanic("Counters and kill", 1)],
                            ["Ravaged Tyrant of Beasts"])
        
        self.valtan = Boss("valtan", [valtan_g1, valtan_g2, valtan_ghost])
        
        brel_g1 = Gate([
            Mechanic("x85 Safe zones", 85),
            Mechanic("x45 Counter", 45)],
                       ["Gehenna Helkasirs"])
        brel_g2 = Gate([
            Mechanic("Just kill", 1)],
                       ["Prokel's Spiritual Echo"])
        
        self.brel = Boss("brel", [brel_g1, brel_g2])
        
        clown_g1 = Gate([
            Mechanic("x130 Reflect stagger", 130),
            Mechanic("x110 Odd one out", 110),
            Mechanic("x85 Simon says", 85),
            Mechanic("x65 Reflect stagger", 65),
            Mechanic("x45 Roulette", 45),
            Mechanic("x25 Odd one out", 25)],
                        ["Saydon"])
        clown_g2 = Gate([
            Mechanic("x125 Saydon appears", 125),
            Mechanic("x110 Safe spots", 110),
            Mechanic("x95 Find kakul", 95),
            Mechanic("x75 Maze", 75),
            Mechanic("x55 Velganos", 55),
            Mechanic("x30 Find kakul", 30)],
                        ["Kakul"])
        clown_g3 = Gate([
            Mechanic("x155 Mario 1", 155),
            Mechanic("x125 Mario 2", 125),
            Mechanic("x90 Showtime", 90),
            Mechanic("x80 Mario 3", 80),
            Mechanic("x55 Mario 4", 55),
            Mechanic("x0 Bingo", 1)],
                        ["Kakul-Saydon"])
        clown_bingo = Gate([
            Mechanic("Just kill", 1)],
                           ["Encore-Desiring Kakul-Saydon"])
        
        self.clown = Boss("clown", [clown_g1, clown_g2, clown_g3, clown_bingo])
        
        self.bosses = [self.brel, self.valtan, self.clown]
        
        

