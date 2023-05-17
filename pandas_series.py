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


## Exercises Part II

#Capitalize all the string values in fruits.

#Count the letter "a" in all the string values (use string vectorization).

#Output the number of vowels in each and every string value.

#Write the code to get the longest string value from fruits.

#Write the code to get the string values with 5 or more letters in the name.

#Find the fruit(s) containing the letter "o" two or more times.

#Write the code to get only the string values containing the substring "berry".

#Write the code to get only the string values containing the substring "apple".

#Which string value contains the most vowels?

# 1.
fruits.str.upper()

# 2.
fruits.str.count('a')

# 3.
fruits.str.count("a|e|i|o|u")

# 4.
alpha = "[a-z]"
fruits[fruits.str.count(alpha).max()]

# 5.
fruits[fruits.str.count(alpha) > 5]

# 6.
fruits[fruits.str.count("o") >= 2]

# 7.
fruits[fruits.str.contains("berry")]

# 8.
fruits[fruits.str.contains("apple")]

# 9.
fruits[fruits.str.count("a|e|i|o|u").max()]