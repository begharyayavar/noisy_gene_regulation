from copy import deepcopy

from tqdm import tqdm

import json

from species import *
from reactions import *
from noise import *
from simulationmethods import *

from defaults import *

class Simulation:
    def __init__(   self,length_trial : int = default_length_trials ,\
                    num_trials : int = default_num_trials,\
                    time_step : int = default_time_step,\
                    simulation_type : str = default_simulation_type,\
                    initial_parameters_fixed = False):
        
        self.length_trial = length_trial
        self.num_trials = num_trials
        self.time_step = time_step
        
        self.simulation_type = simulation_type
        
        self.initial_parameters_fixed = initial_parameters_fixed
        self.results = []
        self.collated_results = {}
    
    def add_reactions(self,reactions: Reactions) -> Reactions:
        self.reactions = reactions
        return self.reactions
    def add_species(self,species: Species) -> Species:
        self.species = species
        return self.species
    
    def get_species(self) -> Species:
        return self.species
    def get_reactions(self) -> Reactions:
        return self.reactions
 
    def fix_initial_parameters(self) -> [Species,Reactions]:
        self.initial_species = deepcopy(self.species)
        self.initial_reactions = deepcopy(self.reactions)
        self.initial_parameters_fixed = True
        return [self.species,self.reactions]

    def reset(self) -> [Species,Reactions]:
        self.species = deepcopy(self.initial_species)
        self.reactions = deepcopy(self.initial_reactions)
        return [self.species,self.reactions]
    
    def collect_results(self) ->  Species:
        self.results.append(self.species.show_counts())
       
    def run(self) -> None:
        for i in tqdm(range(self.num_trials)):
            self.reset()
            for j in range(self.length_trial):
                for k in self.reactions:
                    if transition(k,self.species):
                        for p in k.products.get_species() :
                            self.species.update_count(p,+1)
                        if k.get_reaction_type() == "conversion":
                            for p in k.reactants.get_species():
                                self.species.update_count(p,-1)


            self.collect_results()
        self.collate_results()
    
    def collate_results(self) -> dict:
        final_results = {i:[] for i in self.species.show_counts()}
        for j in self.results:
            for k in j.keys():
                final_results[k].append(j[k])
        self.collated_results = final_results
        return self.collated_results
    
        
            
    def write_results_to_file(self) -> None:

        with open("output.json", "w") as outfile:
            json.dump(self.collated_results, outfile)
        return
        

