from copy import deepcopy
from noise import *
from species import *
from rateconstant import *
from typing import *

default_noise = Noise()
default_rate_constant = RateConstant("Def",1)
    
class Reaction:
    def __init__(self,\
                    reactants: Species,\
                    products: Species,\
                    reaction_rate_constant: ReactionRateConstants,\
                    reaction_type : str = default_reaction_type,\
                    noise : Noise = default_noise):
        self.reactants = reactants
        self.products = products
        self.reaction_rate_constant = reaction_rate_constant
        self.reaction_type = reaction_type
        self.noise = noise
        
    def get_reactants(self) -> Species:
        return self.reactants
    def get_products(self) -> Species:
        return self.products
    def get_reaction_rate_constant(self) -> ReactionRateConstants:
        return self.reaction_rate_constant
    def get_reaction_type(self) -> str:
        return self.reaction_type    
    def get_noise(self) -> Noise:
        return self.noise
    
    
    def __eq__(self,another) -> bool:
        if  hasattr(another,"reactants") and\
            hasattr(another,"products") and\
            hasattr(another,"reaction_rate_constant") and\
            hasattr(another,"reaction_type"): # Fill noise_factor equality and write __eq__ and __add__ methods for all
            pass
    def __add__(self,another) -> 'Reaction' :
        pass # TODO fill this up
    
    def __repr__(self) -> str:
        return "    Reaction:\n\
                    Reactants: {},\n\
                    Products: {},\n\
                    Reaction Rate Constant: \n\t\t{}\n\
                    Type: {}\n\
                    Noise: \n\t{}\n".\
                    format(self.reactants,self.products,self.reaction_rate_constant,self.reaction_type,self.noise)
    
        
class Reactions:
    def __init__(self,reactions : List[Reaction] = []):
        self.reactions = reactions

    def add_reaction(self,reaction : Reaction) -> List[Reaction]:
        self.reactions.append(reaction)
        return self.reactions
    
    def add_reactions(self,reactions: List[Reaction]) -> List[Reaction]:
        self.reactions = reactions
        return self.reactions

    def __add__(self) -> 'Reactions':
        pass # TODO fill this up

    def __repr__(self) -> str:
        return "Species:{} \n Reactions:{}\n".format(self.species,self.list_reactions)

