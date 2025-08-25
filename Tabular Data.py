"""
# Declare variable `house_0_list`
house_0_list = [115910.26, 128, 4]

# Print object type of `house_0_list`
# (We'll learn more about object types in later projects 😉)
print("house_0_list type:", type(house_0_list))

# Print length of `house_0_list`
print("house_0_list length:", len(house_0_list))

# Get output of `house_0_list`
house_0_list
"""
"""""
# Data for houses
area_m2 = [235.0, 130.0, 137.0]
price_cop = [400000000.0, 850000000.0, 475000000.0]

# 📐 Calculate price per square meter for the first house (index 0)
house_0_price_m2 = price_cop[0] / area_m2[0]

# 🔍 Print the type of house_0_price_m2
print("house_0_price_m2 type:", type(house_0_price_m2))

# 💰 Output the price per square meter value
print("house_0_price_m2 value:", house_0_price_m2)
"""

"""""
# Data for houses
area_m2 = [235.0, 130.0, 137.0]
price_cop = [400000000.0, 850000000.0, 475000000.0]

# 🏠 Create list with house 0 info
house_0_list = [area_m2[0], price_cop[0]]

# ➗ Calculate price per square meter and append
price_per_m2 = price_cop[0] / area_m2[0]
house_0_list.append(price_per_m2)

# 🖨️ Print object type
print("house_0_list type:", type(house_0_list))

# 📏 Print list length
print("house_0_list length:", len(house_0_list))

# 📦 Print contents of the list
print("house_0_list:", house_0_list)
"""

"""""
# Declare variable `houses_nested_list`
houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]

# Print `houses_nested_list` type
print("houses_nested_list type:", type(houses_nested_list))

# Print `houses_nested_list` length
print("houses_nested_list length:", len(houses_nested_list))

# Get output of `houses_nested_list`
houses_nested_list
"""""

"""""
for house in houses_nested_list:
    price_m3 = house[0] * house[1]
    house.append(price_m3)
houses_nested_list
"""

"""""
for house in houses_nested_list:
    price_m3 = house[0] * house[1]
    house.append(price_m3)

print("houses_nested_list type:", type(houses_nested_list))
print("houses_nested_list length:", len(houses_nested_list))
houses_nested_list
"""

"""
house_columnwise = {
    'price_usd_price' : [134.5, 5679398, 34893234],
    'price_per_square_meter' : [34756, 84394, None],
    'Sum_of_squares' : [45, 4334, 3242334]
}

print("house_columnwise:", type(house_columnwise))
house_columnwise
"""

""""
house_columnwise = {
    'price_usd_price' : [134.0, 5679398, 34893234],
    'price_per_square_meter' : [34756, 84394, 45],
    'Sum_of_squares' : [45, 4334, 3242334]
}

mean_house_price = sum(house_columnwise["price_usd_price"]) / len(house_columnwise["price_usd_price"])
mean_house_price
"""

""""
# Import pandas library, aliased as `pd`
import pandas as pd

# Define dictionary `houses_columnwise`
houses_columnwise = {
    'price_usd_price': [134.0, 5679398, 34893234],
    'area_in_m2': [0.00386, 67.2, 413.3]
}

# Declare variable `df_houses`
df_houses = pd.DataFrame(houses_columnwise)

# Print `df_houses` object type
print("df_houses type:", type(df_houses))

# Print `df_houses` shape
print("df_houses shape:", df_houses.shape)

# Get output of `df_houses`
print(df_houses)
"""

"""
import pandas as nf

houses_columnwise = {
    "fun" : ["Watching TV", "Playing Fifa", "Movies"],
    "Read" : ["Books", "Notes", "Novel"],
}

nf_houses = nf.DataFrame(houses_columnwise)
print("nf_houses type", type(nf_houses))

print(nf_houses)

"""

"""
import pandas as pd
data = {"col_1" : [1,2,3], "col_2" : [4,5,6], "col_3" : [7,8,9]}

print(pd.DataFrame.from_dict(data))

"""

"""
import pandas as fg

data = {"line_1" : ["a","b","c"], "line_2" : [121,345,677]}
print(fg.DataFrame.from_dict(data, orient = "index"))

"""

"""
import pandas as fg

data = {"line_1" : ["a","b","c"], "line_2" : [121,345,677]}
print(fg.DataFrame.from_dict(data, orient = "index", columns= ["A","B","C"]))
"""


""""
info = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobby": "running",
    "age": 35
}
print(info)

import json
import pandas as pd

data = json.loads(info)

df = pd.DataFrame.from_dict([data])

print(df)
"""


"""""
import json
import pandas as ro

data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobby": "running",
    "age": 35
}

info = json.loads(data)

ro = pd.DataFrame.from_dict([info])

print(ro)
"""""


""""
import json
import pandas as pd

clothes = {"shirt": ["red","M"], "sweater": ["yellow","L"]}

data = json.loads(clothes)

df = pd.DataFrame.from_dict(data, orient = "index", columns = ["color","size"]) 
print(df)

"""

"""
import gzip
import json
import pandas as pd

with gzip.open("data/poland-bankruptcy-data-2008.json.gz", "r") as f:
    poland_data_gz = json.load(f)
    
poland_data_gz.keys()
df = pd.DataFrame().from_dict(poland_data_gz["data"])
df.head()
"""

""""
import pandas as pd

data = {
    "letter": ["a", "b", "c", "d"],
    "number": [3, 2, 1, 0],
    "location": ["east", "east", "east", "west"],
}
df = pd.DataFrame.from_dict(data)

# set index 'numbers'
df.set_index("letter",inplace = True)
df.head(5)


# reset index
df.reset_index(inplace = True)
df.head(5)
"""

""""
import pandas as pd

df = pd.read_csv("data/colombia-real-estate-2.csv")
print (df.shape)  
"""""


