import numpy as np
import matplotlib.pyplot as plt

# Fix random seed for repeatability
np.random.seed(123)

###### Fix model parameters ######
A = Specie("A")
B = Specie("B")
AB = Specie("AB")
S = Species()
S.add([A,B,AB])
R =  Reaction()
R.add_reactants(A)
R.add_reactants(B)
R.add_products(AB)
R.add_forward_rate_constant(2)
R.add_backwards_rate_constant(1)

reactions = Reactions()
reaction.add_reaction(R)

S1 = SimulationVariable(A)
S2 = SimulationVariable(B)
S3 = SimulationVariable(AB)
S1.init_count(25)
S2.init_count(35)
S3.init_count(5)
SS = SimulationVariables()
SS.add_reaction(R)
SS.add_variable(S1)
SS.add_variable(S2)
SS.add_variable(S3)

simpara = SimulationParameters()
simpara.add_steps(25)
simpara.add_cycles(100)

N_A0 = 25     # Initial number of A molecules
N_B0 = 35     # Initial number of B molecules
N_AB0 = 5     # Initial number of AB molecules

rf = 2        # Forward reaction rate
rb = 1        # Backwards reaction rate

steps = 25    # Number of reactions per trajectory
cycles = 100  # Number of trajectories iterated over

# Set up holder arrays
T = np.zeros((cycles, steps+1))
N_A = np.zeros((cycles, steps+1))
N_B = np.zeros((cycles, steps+1))
N_AB = np.zeros((cycles, steps+1))

# Store initial conditions
N_A[:,0] = N_A0
N_B[:,0] = N_B0
N_AB[:,0] = N_AB0

###### Main Code Loop ######
for i in range(cycles):
    for j in range(steps):
        # Calculate updated overall reaction rate
        R = rf * N_A[i,j] * N_B[i,j] + rb * N_AB[i,j]
        
        # Calculate time to next reaction
        u1 = np.random.random()
        tau = 1/R * np.log(1/u1)
        
        # Store reaction time
        T[i, j+1] = T[i,j] + tau
        
        # Select which reaction to occur
        Rf = rf * N_A[i,j] * N_B[i,j] / R
        u2 = np.random.random()
        
        # Update populations
        if u2 < Rf:
            N_A[i,j+1] = N_A[i,j] - 1
            N_B[i,j+1] = N_B[i,j] - 1
            N_AB[i,j+1] = N_AB[i,j] + 1
        else:
            N_A[i,j+1] = N_A[i,j] + 1
            N_B[i,j+1] = N_B[i,j] + 1
            N_AB[i,j+1] = N_AB[i,j] - 1

# Calculate an average trajectory plot
ave_steps = 100
T_max = T.max()

# Set up average arrays
T_ave = np.linspace(0,T_max,ave_steps+1)
N_A_ave = np.zeros(ave_steps+1)
N_B_ave = np.zeros(ave_steps+1)
N_AB_ave = np.zeros(ave_steps+1)

N_A_ave[0] = N_A0
N_B_ave[0] = N_B0
N_AB_ave[0] = N_AB0

# Pass over average array entries
for i in range(1, ave_steps+1):
    tmax = T_ave[i]
    A_sum = 0
    B_sum = 0
    AB_sum = 0
    t_count = 0
    
    # Pass over each trajectory and step therein
    for j in range(cycles):
        for k in range(steps):
            if T[j,k] <= tmax and T[j,k+1] > tmax:
                t_count += 1
                A_sum += N_A[j,k]
                B_sum += N_B[j,k]
                AB_sum += N_AB[j,k]
    
    # Caclulate average - taking care if no samples observed
    if t_count == 0:
        N_A_ave[i] = N_A_ave[i-1]
        N_B_ave[i] = N_B_ave[i-1]
        N_AB_ave[i] = N_AB_ave[i-1]
    else:
        N_A_ave[i] = A_sum / t_count
        N_B_ave[i] = B_sum / t_count
        N_AB_ave[i] = AB_sum / t_count


###### Plot Trajectories ######
fig, axs = plt.subplots(3, 1, figsize=(10,20))

# Plot average trajectories
axs[0].plot(T_ave, N_A_ave, marker='', color='red', linewidth=1.9, alpha=0.9)
axs[0].set_title('Number A Molecules')
axs[0].set_ylim((0,35))
axs[0].set_xlim((0,0.125))
axs[1].plot(T_ave, N_B_ave, marker='', color='red', linewidth=1.9, alpha=0.9)
axs[1].set_title('Number B Molecules')
axs[1].set_ylim((0,35))
axs[1].set_xlim((0,0.125))
axs[2].plot(T_ave, N_AB_ave, marker='', color='red', linewidth=1.9, alpha=0.9)
axs[2].set_xlabel("Time")
axs[2].set_title('Number AB Molecules')
axs[2].set_ylim((0,35))
axs[2].set_xlim((0,0.125))

# Plot each simulated trajectory
for i in range(cycles):
    axs[0].plot(T[i,:], N_A[i,:], marker='', color='grey', linewidth=0.6, alpha=0.3)
    axs[1].plot(T[i,:], N_B[i,:], marker='', color='grey', linewidth=0.6, alpha=0.3)
    axs[2].plot(T[i,:], N_AB[i,:], marker='', color='grey', linewidth=0.6, alpha=0.3)

plt.show()
