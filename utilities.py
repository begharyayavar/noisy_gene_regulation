from species import *
from reactions import *
from rateconstant import *
from noise import *
from defaults import *
from functools import reduce
def species_parser(string) -> [Species,Species]:
    
    tokens = list(\
                map(\
                    str.strip,string.split("->")))

    reactants = Species(\
                    [Specie(i[0],i[1]) \
                        for i in list(\
                            map(lambda x: list(map(str.strip,x.split("="))),\
                                        tokens[0].split("+")))])
    
    products = Species(\
                    [Specie(i[0],i[1]) \
                        for i in list(\
                            map(lambda x: list(map(str.strip,x.split("="))),\
                                        tokens[1].split("+")))])
    
    return [reactants,products]

def reaction_rate_constant_parser(string) -> ReactionRateConstants:
    if string:
        tokens = list(\
                    map(\
                        str.strip,string.split(",")))
        r1 = RateConstant(default_rate_constant_name,default_rate_constant_value)
        r2 = RateConstant(default_rate_constant_name,default_rate_constant_value)
        T = default_reaction_type

        if len(tokens) >= 1:
            a = list(map(str.strip,tokens[0].split("=")))
            r1 = RateConstant(str(a[0]),float(a[1]))
        
        assigned_type = False
        if len(tokens)>= 2: 
            b = list(map(str.strip,tokens[1].split("=")))
            if b[0].strip().lower() == "Type".lower():
                T=str(b[1]).strip()
                assigned_type = True
            else :
                r2 = RateConstant(str(b[0]),float(b[1]))
                
        if len(tokens) == 3:
            c = list(map(str.strip,tokens[2].split("=")))
            if assigned_type:
                r2 = RateConstant(str(c[0]),float(c[1]))
            else :
                if c[0].strip().lower() == "Type".lower():
                    T=str(c[1]).strip()
                    assigned_type = True
    return ReactionRateConstants(r1,r2,T)            
        
def noise_parser(string) -> Noise:
    
    noise_type = default_noise_type
    noise_mu = default_noise_mu
    noise_sigma = default_noise_sigma
    noise_coefficient = default_noise_coefficient
    
    if string:
        tokens = list(\
                    map(\
                        str.strip,string.split(",")))
      
        for i in tokens:
            s = i.lower()
            if "Type".lower() in s:
                noise_type = str(list(map(str.strip,s.split("=")))[1])
                continue
            if "mu".lower() in s:
                noise_mu = float(list(map(str.strip,s.split("=")))[1])
                
            if "sigma".lower() in s:
                noise_sigma = float(list(map(str.strip,s.split("=")))[1])
                continue
            
            if "coefficient".lower() in s:
                noise_coefficient = float(list(map(str.strip,s.split("=")))[1])
                continue
    
    return Noise(   noise_type=noise_type,\
                    noise_mu=noise_mu,\
                    noise_sigma=noise_sigma,\
                    noise_coefficient=noise_coefficient)


def reaction_parser(string) -> Reaction:
    
    # A + B -> C + D ; Ka=Na,Kb=Nb,Type=conversion ; Type=Gaussian mu=x,sigma=y,coef=n
    tokens = list(\
                map(\
                    str.strip,string.split(";")))
    
    species_str = tokens[0]
    reaction_rate_constant_str = tokens[1]
    noise_str = tokens[2]
    
    species = species_parser(species_str)
    reaction_rate_constants = reaction_rate_constant_parser(reaction_rate_constant_str)
    noise = noise_parser(noise_str)
    
    return Reaction(    reactants = species[0],\
                        products = species[1],\
                        reaction_rate_constant=reaction_rate_constants,
                        reaction_type=reaction_rate_constants.get_reaction_type(),\
                        noise = noise) # TODO Fix the reaction type mess -_-


def reactions_parser(filename):
    reactions = []
    with open(filename,"r") as f:
        for line in f:
            print(line)
            if line[0] == "#":
                continue
            reaction = reaction_parser(line)
            reactions.append(reaction)
    return reactions

def specie_parser(string):
    tokens = list(\
                map(\
                    str.strip,string.split(";")))[0]    
    reactants,products = species_parser(tokens)
    all_species = reactants + products
    return all_species


def species_unique_parser(filename):
    specie = []
    with open(filename,"r") as f:
        for line in f:
            print(line)
            if line[0] == "#":
                continue
            specie.append(specie_parser(line))

    species = reduce(lambda a,b : a + b ,specie)
        
    return species

def verify_unique():
    pass
        

    
    