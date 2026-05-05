import pandas

mydataset = {
    "cars" : ["BMW", "Volvo", "Ford"],
    "passings" : [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

# pandas as pd
import pandas as pd

mydataset = {
    "cars" : ["BMW", "Volvo", "Ford"],
    "passings" : [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

# series with index
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# series with index

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# key objects as series
import pandas as pd

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}

myvar = pd.Series(calories)

print(myvar)

# dataframe 
import pandas as pd

data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

# locating rows
print(myvar.loc[0])

# named indexes

import pandas as pd

data = {
    "calories" : [420, 380, 390],
    "duration" : [50, 40, 45]
}

myvar = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(myvar)

# cleaning empty cells

# replacing specified columns

myvar = pd.read_csv('data.csv')
myvar['calories'].fillna(130, inplace = True)

print(myvar.to_string())

# this operation inserts 130 in empty cells in the "calories" column. (row 18 and row28)


