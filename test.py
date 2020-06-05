import matplotlib.pyplot as plt
import numpy as np

#x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
#plt.plot(x, np.sin(x))       # Plot the sine of each x point
#plt.show()                   # Display the plot
print("hello world") 
x=[[6,7,2],[1,5,9],[8,3,4]]
print(x)

for n in range(0,3):
    print(f" {x[n][0]} {x[n][1]} {x[n][2]} ")

# check each row for magic
for n in range(0,3):
    print(f" {x[n][0]} {x[n][1]} {x[n][2]} ={sum(x[0])}") 
for n in range(0,3):
    print(f" {x[n][0]} {x[n][1]} {x[n][2]} ={sum(x[0])}")  
