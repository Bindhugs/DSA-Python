import matplotlib.pyplot as plt
import numpy as np

#BAR CHARTS

catgeories = np.array(['Grains',"Fruits","vegetables","Proteins","Dairy","Sweets"])
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(catgeories,values, color = 'lavender') #This is with color


plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()


#PIE CHARTS


categories = np.array(["Freshmen","Sophomore","Junior","Senior"])
values = np.array([300, 200, 275, 150])
colors = ['lavender','violet','plum','thistle']
plt.pie(values, 
        labels = categories,
        autopct = '%1.1f%%',
        colors = colors,
        explode = [0, 0, 0, 0.5],
        shadow = True,
        startangle = 180
        )  
plt.title("Cool College")
plt.show()