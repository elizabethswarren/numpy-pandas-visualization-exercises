

# 1. Copy the code from the lesson to create a dataframe full of student grades.

# a. Create a column named passing_english that indicates whether each student has a passing grade in english.
df['passing_english'] = df.english > 70

# b. Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values(by='passing_english')

# c. Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=['passing_english','name'])

# d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(by=['passing_english','english'])

# e. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

df['overall_grade'] = (df.math + df.english + df.reading)/ 3

# 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

# a. How many rows and columns are there? 234 rows and 11 columns
mpg_df.shape
# b. What are the data types of each column? object, int, float

# c. Summarize the dataframe with .info and .describe
mpg_df.info
mpg_df.describe
# d. Rename the cty column to city.
mpg_df.rename(columns={'cty':'city'})
# e. Rename the hwy column to highway.
mpg_df.rename(columns={'hwy':'highway'})
# f. Do any cars have better city mileage than highway mileage?
# g. Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
# h. Which car (or cars) has the highest mileage difference?
# i. Which compact class car has the lowest highway mileage? The best?
# j. Create a column named average_mileage that is the mean of the city and highway mileage.
# k. Which dodge car has the best average mileage? The worst?


# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

# a. How many rows and columns are there?
# b. What are the data types?
# c. Summarize the dataframe with .info and .describe
# d. What is the the weight of the fastest animal?
# e. What is the overal percentage of specials?
# f. How many animals are hoppers that are above the median speed? What percentage is this?