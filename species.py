from typing import *
from defaults import *
from copy import deepcopy

class Specie:
    def __init__(   self,\
                    name: str = default_specie_name,\
                    count: int = default_specie_count):
        self.name = name
        self.count = int(count)
    def get_name(self) -> str:
        return self.name
    def get_count(self) -> int:
        return self.count
    
    def __eq__(self,another_specie):
        if hasattr(another_specie,"get_name") and hasattr(another_specie,"get_count"):
            if another_specie.get_name() == self.name and another_specie.get_count == self.count:
                return True
        return False
    
    def __repr__(self) -> str:
        return str("    Name : {}\n\
                        Count : {}\n".\
                        format(self.name,self.count))
            
class Species:
    def __init__(self,species : List[Specie] = []):
        self.species = species
        self.counts = {i.get_name():i.get_count() for i in species}

    def update_count(self,specie : Specie, offset : int) -> int:
        self.counts[specie.get_name()] += int(offset)
        return self.counts[specie.get_name()]
          
    def add_species(self,specie : Specie , count : int) -> List[Specie]:
        self.counts[specie.get_name()] = int(count)
        self.species.append(specie)
        return self.species
    
    def get_specie_count(self,specie) -> int:
        return self.counts[specie.get_name()]
    
    def get_species(self) -> List[Specie]:
        return self.species

        
    def show_counts(self) -> dict:    
        return self.counts
    
    
    def __add__(self,another_species_list) -> 'Species': 
        result = deepcopy(self.species)
        for i in another_species_list.get_species():
            if not i in self.species:
                result.append(i)
        return Species(result)
    
    def __repr__(self) -> str:
        return str(self.counts) # TODO pprint?
