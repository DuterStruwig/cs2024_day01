# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:36:58 2024

@author: duter
"""

"""
Storing data in Python
1. Lists
2. Dictionaries
3. Data Frames - specific to pandas
"""

import pandas

"""
import pandas as pd 

to instead of typing pandas you can just type pd
"""

file = pandas.read_csv("country_data.csv")
                       
print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

age1 = 30   # Tedious
age2 = 25
age3 = 29

# ---LISTS---

age = [30,25,29,46,22]

print(age)

"""
[30, 25, 29, 46, 22]
"""

print(age[0])

"""
30
"""

print(age[1])

"""
25
"""

print(min(age))

"""
22
"""   

print(max(age))
print(sum(age))
print(len(age))

"""
46
152
5
"""

avg = sum(age)/len(age)
print(avg)

"""
30.4
"""

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M","F","F"]

c1 = "South Africa"
c2 = "Lesotho"

country_list = ["South Africa","Lesotho"]

print(age[0:2])

"""
[30, 25]
"""

age.append(100)

print(age)

"""
[30, 25, 29, 46, 22, 100]
"""

age.insert(0,100)   # Insert a value anywhere in the list

# ---DICTIONARIES---

"""
Dictionaries are key:value pairs

cat: "a cute animal"

Does not have an index

"""

mammals = {"cat":"a cute animal", "lion":"king of the jungle", "elephant":"a gigantic herbivore"}

print(mammals["cat"])

"""
a cute animal
"""

# Interesting fact: Pachyderm -> A very large mammal with thick skin, especially an elephant, rhinoceros, or hippopotamus.

# ---DATA FRAMES---

"""
Mostly used
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

Size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits':fruits,
    'sizes':Size_nm
        
    
    }

# df = dataframe

df = pandas.DataFrame(fruit_sizes)

print(df)

"""
   fruits  sizes
0   apple    9.8
1  banana   10.1
2  orange   13.2
3   grape    8.7
4    kiwi   20.5
"""

print(df['fruits'])

"""
0     apple
1    banana
2    orange
3     grape
4      kiwi
"""

print(df['sizes'])

"""
0     9.8
1    10.1
2    13.2
3     8.7
4    20.5
"""

print(df['sizes'].min())

print(df['sizes'].mean())

"""
8.7
12.459999999999999
"""

print(df.describe())

"""
           sizes
count   5.000000
mean   12.460000
std     4.795102
min     8.700000
25%     9.800000
50%    10.100000
75%    13.200000
max    20.500000
"""

print(df[ df["sizes"] > 10])

"""
   fruits  sizes
1  banana   10.1
2  orange   13.2
4    kiwi   20.5
"""

print(df[1:3])

"""
   fruits  sizes
1  banana   10.1
2  orange   13.2
4    kiwi   20.5
"""

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

print(df)

"""
   fruits  sizes  prices
0   apple    9.8    10.0
1  banana   10.1    12.5
2  orange   13.2    16.0
3   grape    8.7    23.0
4    kiwi   20.5     7.0
"""

df.drop(columns=['sizes'], inplace=True)

"""
The inplace=True parameter is often used in pandas DataFrame and 
Series methods to indicate that the operation should modify the 
existing object rather than creating a new one. When inplace=True 
is set, the modifications are applied directly to the object, and 
there's no need to assign the result back to a variable.
"""






      


