
from simulations import *
from utilities import *


# Set up the initial conditions

simulation = Simulation()
reactions = Reactions()
species = Species()

# Read Reactions from a file

reactions = reactions_parser(reactions_default_filename)
species = species_unique_parser(reactions_default_filename)



simulation.add_reactions(reactions)
simulation.add_species(species)    
simulation.fix_initial_parameters()

# Run Simulation

simulation.run()


# Show results

simulation.show_results()
simulation.write_results_to_file()
