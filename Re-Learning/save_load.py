# How to save data 

import pickle 
import os 
os.system("clear")

#Create a list
names = ["Saeed", "Anas", "Bon", "John"]

#Print the list 
print("Original List")
print(names)

#Save the list 
pickle.dump(names, open("names.dat", "wb"))

#Change 
names.remove("Bon")

#Print the list
print("Changed List")
print(names)

#Load saved data
names = pickle.load(open("names.dat", "rb"))

#Print the list 
print("Original List")
print(names)