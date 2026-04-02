#Basics of matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.array([12,23,34,25])
y = np.array([12,14,15,19])
plt.plot(x,y, 
         color = 'Blue',
         linestyle = 'dashdot',
         marker = '*',
         linewidth = 5,
         markeredgecolor = 'yellow',
         markerfacecolor = 'Blue',
         markersize = 20
         ) #This is for ploting customization
  

plt.title("Class size",
          fontsize = 20,
          family = "Algerian",
          color = 'Red',
          )

plt.xlabel("Number of students",
          fontsize = 15,
          family = "Times New Roman",
          color = 'Blue'
          )
plt.ylabel("Marks",
          fontsize = 15,
          family = "Times New Roman",
          color = 'Blue'
          )

plt.show()

