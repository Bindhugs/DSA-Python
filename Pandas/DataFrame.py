#Data_Frame

import pandas as ad
student = {
    "Name": ("Antony","Bobby","Curdy"), 
    "Age": (24,26,27),
    "City": ("Delhi","Mumbai","Bangalore"),
    "Gender": ("Male","Male","Female")
           }

df = ad.DataFrame(student,index = ["Emp 1","Emp 2","Emp 3"])

print(df)
