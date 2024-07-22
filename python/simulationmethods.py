import random
import math

from functools import reduce

from reactions import Reaction
from species import Species


class SimulationVariable:
    def __init__(self,specie,reactions):
        self.name = specie.name()
        self.count = specie.count()
        

class SimulationVariables:
    def __init__(self,species,reactions):
        self.species = species
        self.species_count = {i.name():0 for i in self.species}
        self.reactions = reactions
        self.reactions_list = [i.repr() for i in self.reactions]
        self.rate_constants = []
        pass
    def add_species(self):
        pass
    def remove_species(self):
        pass
    def add_reaction(self):
        pass
    def remove_reaction(self):
        pass
    


def transition(reaction : Reaction,species : Species,reaction_rates,method = "Gillespie"):
    
    if method == "MonteCarlo":

        probablity = pow(math.e,-(reaction.get_rate_constant().get_value()))
        check_val = random.random()
        return (check_val >= probablity)


    elif method == "Gillespie":

        reactants = reaction.get_reactants()
        products = reaction.get_products()

        Na = reduce(lambda x,y: x*y,[species.get_specie_count(i) for i in reactants.get_species()])
        Nb = reduce(lambda x,y: x*y,[species.get_specie_count(i) for i in products.get_species()])

        Kf = reaction.get_reaction_rate_constant().get_Kf()
        Kb = reaction.get_reaction_rate_constant().get_Kb()

        r = reaction.get_noise().get_coefficient()
        
        total_reaction_rate = (Kf * Na) + (Kb * Nb)
        forward_rate = Kf*Na + r * reaction.get_noise().generate()
            
        probablity = 0

        if total_reaction_rate != 0:
            probablity = forward_rate/total_reaction_rate

        check_val = random.random()
        return (check_val <= probablity)
