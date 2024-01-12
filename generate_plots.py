import json
import matplotlib.pyplot as plt


# reading json data
with open('output.json', 'r') as openfile:
    json_object = json.load(openfile)    



# Generating Plots

# Plot properties
plt.figure(figsize = (10, 8)) 

# Adding Values ,type histogram
for i in json_object:
    values = json_object[i]
            
    print(" name : {}\n\
            max : {}\n\
            min : {}\n".\
            format(i,max(values),min(values)))
    
            
    if max(values) - min(values) <= 0:
        continue
    plt.hist(values, bins=abs(max(values) - min(values)), density=True,label=str(i))      

# showing plot
plt.legend()
plt.show()     