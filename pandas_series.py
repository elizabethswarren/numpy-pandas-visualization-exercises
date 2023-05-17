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
# Instructor Answers: fruits.size

# 2.
fruits.index

# 3.
fruits.values
#Instructor Answers: list(fruits.values)

# 4.
fruits.head()
#Instructo Answers: fruits.dtypes

# 5.
fruits.head(5)
fruits.tail(3)
fruits.sample(2)
#Instructor Answers: adding ? will return the docstrings
# fruits[:5]
# fruits[-3:]

# 6.
fruits.describe()

# 7.
fruits.unique()
# Instructor Answer: set(fruits)

# 8.
len(fruits.unique())
# Instructor Answer: fruits.nunique()
# fruits.value_counts()

# 9.
fruits.mode()
# Instructor Answer: fruits.value_counts().index[0]
#order_fruits = fruits.value_counts()
#order_fruits.nlargest(n=1)

# 10.
fruits.min()
#Instructor Answer: order_fruits.tail(1)
#order_fruits.nsmallest(n=1, keep='all')


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
#Instructor Answer: fruits.capitalize()

# 2.
fruits.str.count('a')
#Instructor Answer: to get the total number of a's :
# fruits.str.count('a').sum()

# 3.
fruits.str.count("a|e|i|o|u")
# Instructor Answer: fruits.str.count('[aeiou]')

# 4.
alpha = "[a-z]"
fruits[fruits.str.count(alpha).max()]
# Instructor Answer: 
# fruits.apply(len).nlargest(1)
# max(fruits, key=len)
# 

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
#Instructor Answer :fruits.str.count(r'[aeiou]').nlargest(n=1, keep='all')

## Exercises Part III

# 1. Which letter occurs the most frequently in the letters Series?

# 2. Which letter occurs the Least frequently?

# 3. How many vowels are in the Series?

# 4. How many consonants are in the Series?

# 5. Create a Series that has all of the same letters but uppercased.

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.

string_list = ['hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy']
letter_list = [i for let in string_list for i in let]
letter_series = pd.Series(letter_list)

# 1.
letter_series.value_counts().head(1)

# 2.
letter_series.value_counts().tail(1)

# 3.
vowels = 'a|e|i|o|u'
letter_series.str.contains(vowels).count()

# 4.


# 5.
letter_series.str.upper()

# 6.
letter_series.value_counts().head(6).plot()


## Exercise III part 2
#How many elements are in the exam_scores Series?

#Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

#Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

#Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.

#Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.

#Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.

exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# 1.
len(exam_scores)

# 2.
exam_scores.describe()

# 3.


# 4.
curved_grades = exam_scores + (100.00 - max(exam_scores))

# 5.


# 6.