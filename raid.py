class Mechanic:
    def __init__(self, description: str, hp: int):
        self.description = description
        self.hp = hp


class Gate:
    def __init__(self, mechanics, names):
        self.mechanics = mechanics
        self.names = names

    def get_next_mechanic(self, hp: int) -> Mechanic:
        valid_mechanics = [mechanic for mechanic in self.mechanics if hp >= mechanic.hp]

        if valid_mechanics:
            return valid_mechanics[0]
        return Mechanic("Just kill", 1)


class Boss:
    def __init__(self, name: str, gates):
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
        brel_g3 = Gate([
            Mechanic("x145 Meteor and stagger", 145),
            Mechanic("x100 Medusa stagger", 100),
            Mechanic("x42 Shapes", 42),
            Mechanic("x0 Scythes and spears", 0)],
                       ["Ashtarot"])
        brel_g4 = Gate([
            Mechanic("x170 Wipe mech", 170),
            Mechanic("x160 Color change", 160),
            Mechanic("x135 Color change", 135),
            Mechanic("x120 Wipe mech", 120),
            Mechanic("x95 Stagger", 95),
            Mechanic("x65 Color change", 65),
            Mechanic("x55 Wipe mech", 55),
            Mechanic("x40 Color change", 40),
            Mechanic("x20 Stagger", 20)],
                       ["Primordial Nightmare"])
        brel_g5 = Gate([
            Mechanic("x180 Shapes appear", 180),
            Mechanic("x144 Last shapes", 144),
            Mechanic("x140 Spots x3", 140),
            Mechanic("x110 memory stagger - cubes - stagger / safe spot", 110),
            Mechanic("x90 Shapes appear", 90),
            Mechanic("x54 Last shapes", 54),
            Mechanic("x50 Spots x3 + 1", 50)],
                       ["Brelshaza. Monarch of Nightmares"])
        brel_g6 = Gate([
            Mechanic("x222 Tornado", 222),
            Mechanic("x212 Shape dimension", 212),
            Mechanic("x188 Meteors", 188),
            Mechanic("x112 Worship", 112),
            Mechanic("x65 Tornado", 65),
            Mechanic("x32 Shape Dimension", 32),
            Mechanic("x25 Corner breaking", 25)],
                       ["Phantom Legion Commander Brelshaza"])
            
        self.brel = Boss("brel", [brel_g1, brel_g2, brel_g3, brel_g4, brel_g5, brel_g6])

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
        
        kayangel_g1 =  Gate([
            Mechanic("x55 Pizza/Safe spots", 55),
            Mechanic("x25 Orbs", 25)],
                            ["TBA"])
        kayangel_g2 = Gate([
            Mechanic("x55 Lightning pillars", 55)],
                           ["TBA"])
        kayangel_g3 = Gate([
            Mechanic("x60 Rotate anti-clockwise", 60),
            Mechanic("x40 Counter", 40),
            Mechanic("x16 Rings", 16)],
                           ["TBA"])
        kayangel_g4 = Gate([
            Mechanic("x180 Slashes", 180),
            Mechanic("x140 Light rays", 140),
            Mechanic("x100 Orbs/Shade pillars", 100),
            Mechanic("x60 Clones", 60)],
                           ["TBA"])
        
        self.kayangel = Boss("kayangel", [kayangel_g1, kayangel_g2, kayangel_g3, kayangel_g4])
        
        akkan_g1 = Gate([
            Mechanic("x140 8 Tumor Orbs/Spear", 140),
            Mechanic("x128 Cleanse Yellow", 128),
            Mechanic("x112 Orb Grab", 112),
            Mechanic("x75 Stop Mobs", 75),
            Mechanic("x50 Inana Phase", 50),
            Mechanic("x20 Remove Shield/Bells", 20)],
                        ["TBA"])
        akkan_g2 = Gate([
            Mechanic("x175 Tentacles", 175),
            Mechanic("x160 Ghost", 160),
            Mechanic("x140 Red Hole", 140),
            Mechanic("x110 Hide", 110),
            Mechanic("x85 Red Hole", 85),
            Mechanic("x55 Ghost", 55),
            Mechanic("x30 Red Hole", 30),
            Mechanic("x0 Destruction", 0)],
                        ["TBA"])
        akkan_g3 = Gate([
            Mechanic("x200 Stagger", 200),
            Mechanic("x165 Line Delivery & Stagger", 165),
            Mechanic("x140 Star or Hexagon", 140),
            Mechanic("x139 - x31 Random Party Gimmicks", 139),
            Mechanic("x30 Arena Break", 30),
            Mechanic("x0 Destruction", 0)],
                        ["TBA"])
        akkan_hard_phase = Gate([
            Mechanic("x300 Extra Phase Begins", 300),
            Mechanic("x235 Akkan Smash 1", 235),
            Mechanic("x200 Water Park", 200),
            Mechanic("x135 Akkan Smash 2", 135)],
                                ["Plague Legion Commander"])
        
        self.akkan = Boss("akkan", [akkan_g1, akkan_g2, akkan_g3, akkan_hard_phase])
        
        self.bosses = [self.brel, self.valtan, self.clown, self.kayangel, self.akkan]
