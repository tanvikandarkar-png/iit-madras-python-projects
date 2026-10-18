
from turtle import pd

import cowsay
cowsay.cow("hello from vs code!")
import random
#Pick a random number between 1 and 10
lucky_number=random.randint(1,10)
print("Your lucky number today is:", lucky_number)
import cowsay
import random

# 1. Pick a random number between 1 and 100
lucky_number = random.randint(1, 100)

# 2. Convert the number into a text message
message = f"Your lucky number is {lucky_number}!"

# 3. Make the cow say it!
cowsay.cow(message)
import numpy as np
# create a Numpy array (a list of numbers optimized for math)
prices=np.array([100,200,300,400,500]) 
print("original prices:", prices)
import numpy as np

# 1. Create a NumPy array (a list of numbers optimized for math)
prices = np.array([100, 200, 300, 400, 500])

print("Original Prices:", prices)

# 2. Apply math to ALL numbers at once! 
# Let's give a 10% discount to every price in a single line of code.
discounted_prices = prices * 0.9

print("Prices after 10% discount:", discounted_prices)

# 3. Find some quick statistics
print("Average Price:", np.mean(prices))
print("Highest Price:", np.max(prices))
import numpy as np

# 1. Create a sequence of 12 numbers (from 0 to 11)
numbers = np.arange(12)
print("Original flat numbers:\n", numbers)

# 2. Reshape them into a 3 rows by 4 columns grid (like a table)
grid = numbers.reshape(3, 4)
print("\nReshaped into a 3x4 grid:\n", grid)

# 3. Access a specific item (Row 1, Column 2)
# Remember, programming usually starts counting at 0!
print("\nItem at Row 1, Column 2:", grid[1, 2])
s={1,2,3,4,5}
l=[]
for i in range(len(s)):
    l +=[1+i]
print(l)
import numpy as np
arr=np.array(np.arange(0,15))
print(arr.reshape(3,5))
name="Mahesh"
l=[]
for i in name:
    l.append(i.capitalize())
print(l)
import os
print(os.getcwd())  
import pandas as pd
print("Pandas version:", pd.__version__)
import pandas as pd
df=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\input_data.txt",sep=',')
# Step 1: Read the text file (assuming it uses commas to separate data)
# Change sep=',' to sep='\t' if your text file uses tabs instead of commas
df = pd.read_csv('input_data.txt', sep=',')

# Step 2: Save the data directly into an Excel file
df.to_excel('output_data.xlsx', index=False)

print("Conversion successful! Excel file created.")

