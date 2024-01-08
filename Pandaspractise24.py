import pandas as pd

df = pd.read_csv('C:\\Users\\gaura\\OneDrive\\Desktop\\Practise Pandas 24\\data.csv')   #to read csv files
# print(df)  #give you top 5 head and tail details
# print(df.loc[0])  #Gives you 0 index details
# print(df.loc[0:4])  #Gives you 0-4 index details
# print(df.to_string)  #all details
pd.options.display.max_rows = 9999    #to set no of max rows to display
# print(pd.options.display.max_rows)    #to see max row limit
# print(df.to_string)  #all details
# df = pd.read_json('data.json')  #To read Json file


#Data Analysis always tart with head ()

# print(df.head())  # You see top 5 rows by default 
# print(df.head(10))  # You see top 10 rows
# print(df.tail())  # You see bottom 5 rows

#info(), that gives you more information about the data set.
# print(df.info())  #gives you details line column name and its types
  

#Data Cleaning
# new = df.dropna() #return a new Data Frame with no empty cells:
# print(new)  #get non empty rows only
# print(df.duplicated()) #gives you boolean value true or false for duplicate values  
# print(df)
# df.dropna(inplace = True) # If you want to change the original DataFrame, use the inplace = True argument 
"""Dont run above command"""


#Replace Empty Values

# df["Date"].fillna("25-12-2024", inplace = True)  #fill value as 130 in row calories

#Pandas has a to_datetime() method for this

# df['Date'] = pd.to_datetime(df['Date'])  #change format of date


#Replacing Values
# df.loc[0, 'Duration'] = 124
# print(df.head())

#loop through and check
# for x in df.index:
#   if df.loc[x, "Date"] > '15-01-2024':
#     df.loc[x, "Date"] = '25-12-2024'


#Finding Relationships
#A great aspect of the Pandas module is the corr() method.

# print(df.corr())


#Plotting
#Pandas uses the plot() method to create diagrams.
import matplotlib.pyplot as plt

# df.plot()
# plt.show()

#histogram chart 
# df["Duration"].plot(kind = 'hist')
# df.plot()
# plt.show()

