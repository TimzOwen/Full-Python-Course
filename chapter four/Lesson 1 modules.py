

## Python Modules
# Modules helps us organize code in multiple Files
# Each File is a module  
# create a new File / modelu to import from
# make sure Files are in the same folder 
# check the Modules Folder to upload



# import specific modules
from ecommerce.shipping import cal_shipping

cal_shipping() # now the method gets called.


# import all functions in a package
from ecommerce import shipping
shipping.customer_address()
shipping.cal_shipping()

# Central bank package fow cash payments and transactions
from banking import withdrawals
withdrawals.transactions(50000)
withdrawals.monthly_withdrawals(120000)



# check if path exists in a direcrtory
from pathlib import Path

path = Path() # the current path

path5 = Path("checkPath")
print(path5.exists()) # Returns a boolean

# create a new directory
path2 = Path("MainServer")
# print(path2.mkdir()) # creates a new directory

path3 = Path("MainServer")
print(path3.exists()) # Returns True
# path3.rmdir()
# print(path3.exists()) # returns False

for files in path.glob('*'):
    print(files) # prints all Files in the iteration




# Challenge 
# create a numbers iteration loop to find the largest
# make sure to have sepate modules





# PACKAGES
# This is a way of organizing your large projects
# This is a container for multiple modules
 # check VS Code for the package modules
 
 
