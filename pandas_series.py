import pandas as pd

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple",
                     "honeycrisp apple", "tomato", "watermelon", "honeydew",
                     "kiwi", "kiwi", "kiwi", "mango", "blueberry",
                     "blackberry", "gooseberry", "papaya"])

#Determine the number of elements in fruits.

#Output only the index from fruits.

#Output only the values from fruits.

#Confirm the data type of the values in fruits.

#Output only the first five values from fruits. Output the last three values. Output two random values from fruits.

#Run the .describe() on fruits to see what information it returns when called on a Series with string values.

#Run the code necessary to produce only the unique string values from fruits.

#Determine how many times each unique string value occurs in fruits.

#Determine the string value that occurs most frequently in fruits.

#Determine the string value that occurs least frequently in fruits.

# 1.
len(fruits)

# 2.
fruits.index

# 3.
fruits.values

# 4.
fruits.head()

# 5.
fruits.head(5)
fruits.tail(3)
fruits.sample(2)

# 6.
fruits.describe()

# 7.
fruits.unique()

# 8.
len(fruits.unique())

# 9.
fruits.mode()

# 10.
fruits.min()