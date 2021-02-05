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
