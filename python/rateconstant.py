from typing import *
from defaults import *

class RateConstant:
    def __init__(   self,name: str = default_rate_constant_name,\
                    value: float = default_rate_constant_value):
        self.name = name
        self.value = float(value)
    
    def get_name(self) -> str:
        return self.name
    def get_value(self) -> float:
        return self.value
    def set_value(self,value) -> float:
        self.value = value
        return self.value
    
    def __repr__(self) -> str:
        return str({self.name:self.value})
        
class ReactionRateConstants:
    def __init__(self,  \
                    forward_rate_constant: RateConstant = RateConstant(),\
                    backward_rate_constant : RateConstant = RateConstant(),\
                    reaction_type : str = default_reaction_type):
       
        self.name = forward_rate_constant.get_name() + " + " + backward_rate_constant.get_name()
        
        self.forward_rate = forward_rate_constant
        self.backward_rate = backward_rate_constant
        
        self.reaction_type = reaction_type
        
    def get_Kf(self) -> float:
        return self.forward_rate.get_value()
    def get_Kb(self) -> float:
        return self.backward_rate.get_value()
    
    def set_Kf(self,value: float) -> float:
        self.forward_rate.set(value)
        return self.forward_rate
    def set_Kb(self,value: float) -> float:
        self.backward_rate.set_value(value)
        return self.backward_rate
    
    def get_reaction_type(self) -> str:
        return self.reaction_type
    
    
    def __repr__(self) -> str:
        return "    Name : {}\n\
                    Ka : {}\n\
                    Kb : {}\n\
                    Type : {}\n".\
                    format(self.name,self.forward_rate.get_value(),self.backward_rate.get_value(),self.reaction_type)
                    
class ReactionsRateConstants:
    def __init__(self,\
                    reactionsRateConstants : list[ReactionRateConstants] = []):
        self.reactionsRateConstants = reactionsRateConstants
        
    def add(    self,reactionRateConstant : ReactionRateConstants)\
                    -> list[ReactionRateConstants]:
        self.reactionsRateConstants.append(reactionRateConstant)
        return self.reactionsRateConstants
    
    def remove( self,reactionRateConstant : ReactionRateConstants)\
                    -> list[ReactionRateConstants]:
        if reactionRateConstant in self.reactionsRateConstants:
            self.reactionsRateConstants.remove(reactionRateConstant)
        return self.reactionsRateConstants
