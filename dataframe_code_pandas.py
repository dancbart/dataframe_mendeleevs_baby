# %% markdown
# ## Homework #3.  Daniel Barton.  Physics 3200 - Python
# %% markdown
# #### Q1:    Create a dictionary with four key-value pairs. The keys are the names of four countries and the values are the corresponding capitals. From this create a series. Make a slice of this series that consists of the second and third rows.
# %% codecell
import pandas as pd

#Dictionary with 4 key-value pairs (countries and cities)
names={'Lebanon':'Beirut','Wales':'Cardiff','Mexico':'Mexico City','Kenya':'Nairobi'}

#From this create a series
c=pd.Series(names)
print ("Here is the original series:\n")
print (c)
#Slice the series consisting of second and third rows
print('\nSlice series showing only 2nd and 3rd rows:\n')
print(c[1:3])
# %% markdown
# #### Q2: Create a dataframe consisting of ten rows and three columns. The indices are the names of the first ten elements of the periodic table (Hydrogen … Neon). The first column consists of the chemical symbols for the atoms, the second column has the atomic numbers, and the third column gives the electronegativities of the corresponding atoms.
# %% codecell
import pandas as pd
# get required list from internet of the Periodic Table (first created by Dmitri Mendeleev)
mendeleevs_baby = pd.read_csv('https://bit.ly/2V1yDIN') #This is a bit.ly that I made for this program.  The source data comes from Github website.  Follow Bitly link to source.
# remove unnecessary columns
mendeleevs_baby.drop([' atomicMass',' cpkHexColor',' electronicConfiguration',' atomicRadius',' ionRadius',' vanDelWaalsRadius',' ionizationEnergy',' electronAffinity',' oxidationStates',' standardState',' bondingType',' meltingPoint',' boilingPoint','density',' groupBlock',' yearDiscovered'], axis=1, inplace=True)
# swap columns to appear in desired order
mendeleevs_baby = mendeleevs_baby[[' name',' symbol', 'atomicNumber', ' electronegativity']]
# set row indices to return "element name" from source data
mendeleevs_baby.set_index(' name', inplace=True)
# print the result
mendeleevs_baby[:10]

#below is code used to manipulate data (not part of assignment)
#cols = list(mendeleevs_baby.columns.values).  Used to print list of headers to copy into code.
#cols

# Note, if the bit.ly link breaks for you, I will provide alternate code without refering to outside link.  At the time of writing, the link was active.
# %% markdown
# #### Q3: Consider the following dictionary: { 'EmpCode': ['Emp001', ...    Create a dataframe from this dictionary and print it. Drop the column ‘Age’ and print the resulting dataframe. Print the last two rows. Print the second and fourth columns.
# %% codecell
import pandas as pd
# Here is the given dictionary that the DataFrame will use:
emp_info = { 'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
        'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
        'Occupation': ['Chemist', 'Statistician', 'Statistician', 'Statistician', 'Programmer'],
        'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26', '2018-03-16'],
        'Age': [23, 24, 34, 29, 40]
        }

#Now, create the DataFrame
print('\nOriginal data frame:\n')
df1 = pd.DataFrame(emp_info)
print(df1)

#Drop the 'Age' column
print("\nRemove the 'Age' column:\n")
df1.drop(['Age'], axis='columns', inplace=True)
print(df1)

print("\nPrint last 2 rows from DataFrame:\n")
df1LastTwoRows = df1.tail(2)
print(df1LastTwoRows)

print("\nShow 2nd and 4th columns:\n")
print(df1.iloc[:,[1,3]])
# %% markdown
# #### Q4: Write a Python program to add, subtract, multiply and divide two Pandas Series. Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
# %% codecell
import pandas as ps
import numpy as np

# Use DataFrame to nicely display the series:

data = {'series_1':[2, 4, 6, 8, 10],
       'series_2':[1, 3, 5, 7, 9]}

indices = ['','','','','']

fr1 = pd.DataFrame(data, index = indices)
print(fr1)

# Now, manipulate actual series:

srs_a = ps.Series([2, 4, 6, 8, 10])
srs_b = ps.Series([1, 3, 5, 7, 9])

print("\nAdd two series together:\n")
sab = srs_a + srs_b
print(sab)

print("\nSubtract each:\n")
sab = srs_a - srs_b
print(sab)

print("\nMultiply each:\n")
sab = srs_a * srs_b
print(sab)

print("\nDivide first series by second:\n")
sab = srs_a.divide(srs_b.values)
print(sab)
# %% markdown
# #### Q5: Consider the following Python dictionary data and Python list labels: data = {'animal': ['cat', ...  PERFORM THE FOLLOWING 10 TASKS:
# %% codecell
import numpy as np
import pandas as pd

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],

        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],

        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}


labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

fr1 = pd.DataFrame(data,index = labels)
# Print DataFrame from above dictionary with 'labels' used for the indices
fr1
# %% codecell
#Display a summary of the basic information about the DaraFrame, and its data
fr1.describe()
# %% codecell
# Return the first 3 rows of the DataFrame
fr1.head(3)
# %% codecell
#Select just the 'animal' and 'age' columns from the DataFrame
fr1[['animal','age']]
# %% codecell
# Select the data in rows [3, 4, 8] and in columns ['animal','age']
fr1.iloc[[2,3,7]][['animal','age']]
# %% codecell
# Select only the rows where the number of visits is greater than 3
# Notice, there are no visits 'greater than' 3.  There are some that = 3, but none greater.
fr1[fr1['visits']>3]
# %% codecell
#Select rows where the age value is missing 'NaN'
fr1[fr1['age'].isna()]
# %% codecell
# Select the rows where the animal is a cat andthe age is less than 3.
fr1[(fr1['age'] < 3) & (fr1['animal']=='cat')]
# %% codecell
# Change the age in row 'f' to 1.5
fr1.at['f','age'] = 1.5
fr1
# %% codecell
# Calculate the sum of all visits (the total number of visits).
fr1['visits'].sum()
