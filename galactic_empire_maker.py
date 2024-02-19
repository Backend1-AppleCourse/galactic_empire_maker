import random
materials = [
    "Aluminum",
    "Copper",
    "Steel",
    "Titanium",
    "Silicon",
    "Polyethylene",
    "Nylon",
    "Carbon Fiber",
    "Glass",
    "Ceramic",
    "Rubber",
    "Wool",
    "Cotton",
    "Leather",
    "Polyester",
    "Brass",
    "Bronze",
    "Graphite",
    "Kevlar",
    "Plexiglass"
]

class Delegation:
    def __init__(self, name):
        self.name = name
        self.materials = random.sample(materials, random.randint(2,3))
        self.num_of_suggestions = random.randint(7,14)

    def __str__(self):
        return f'delegation: {self.name} materials:{self.materials} suggestions:{self.num_of_suggestions}'

    def negotiate(self, materialOffer):
        if materialOffer not in self.materials:
            print(f'{self.name} are not interested in {materialOffer}')
            return False
        else:
            print(f'{materialOffer} is in {self.materials}')
            print(f'{self.name} are interested in allying with Humans')
            return True
    
class HumanDelegation():
    def __init__(self):
        self.name = "Humans"
        self.alliances = []

    def __str__(self):
        return f'delegation: {self.name} alliances:{self.alliances}'

    def negotiate(self, delegation):
        if not isinstance(delegation, Delegation):
            raise ValueError('Delegation is required')
        if delegation.name in self.alliances:
            print(f'Humans are already allied with {delegation.name}')
            return
        while delegation.num_of_suggestions > 0:
            random_item = random.choice(materials)
            if delegation.negotiate(random_item):
                print(f'{delegation.name} are now allied with Humans')
                self.alliances.append(delegation.name)
                return
            delegation.num_of_suggestions -= 1  
        print(f'{delegation.name} are not interested in negotioating with Humans anymore.')
        return

class NegotioationManager:
    def __init__(self):
        self.delegations = [Delegation(i) for i in range(1, 6)]
        self.humans = HumanDelegation()
        
    def start(self):
        for delegation in self.delegations:
            self.humans.negotiate(delegation)
        if(len(self.humans.alliances)/len(self.delegations) >= 0.7):
            print(f'{self.humans.name} has successfully allied with over 70% delegations')
        else:
            print(f'{self.humans.name} has failed to ally with over 70% delegations')

negotioationManager = NegotioationManager()
negotioationManager.start()