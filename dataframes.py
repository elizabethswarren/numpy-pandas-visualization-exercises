

# 1. Copy the code from the lesson to create a dataframe full of student grades.

# a. Create a column named passing_english that indicates whether each student has a passing grade in english.
df['passing_english'] = df.english > 70

#Instructor Answer: df.assign

# b. Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values(by='passing_english')

# c. Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=['passing_english','name'])

# d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(by=['passing_english','english'])

# e. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

df['overall_grade'] = (df.math + df.english + df.reading)/ 3

# Instructor Answer: students_df['overall_grade']=students_df[['english','math','reading']].mean(axis=1)

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
# f. Do any cars have better city mileage than highway mileage? No
mpg_df[mpg_df['cty'] > mpg_df['hwy']]
#Instructor Answer:(mpg_df['city'] > mpg_df['highway']).any()

# g. Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg_df['mileage_difference'] = mpg_df['hwy'] - mpg_df['cty']
# h. Which car (or cars) has the highest mileage difference?
mpg_df.sort_values(by='mileage_difference', ascending=False)
# i. Which compact class car has the lowest highway mileage? The best?
mpg_df.sort_values(by='mileage_difference')
# j. Create a column named average_mileage that is the mean of the city and highway mileage.
mpg_df['average_mileage'] = (mpg_df['hwy'] - mpg_df['cty']) / 2
# k. Which dodge car has the best average mileage? The worst?
mpg_df.sort_values(by='average_mileage')
mpg_df.sort_values(by='average_mileage', ascending=False)
#Instructor Answer: dodge_cars = mpg_df['manufacture'] == 'dodge'
#dodge_cars.sort_values('average_milage').head(1)
#dodge_cars.sort_values('average_milage').tail(1)

# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

# a. How many rows and columns are there? 107 rows 4 columns
mammal_df.shape
# b. What are the data types? float and bool

# c. Summarize the dataframe with .info and .describe
mammal_df.info()
mammal_df.describe()
# d. What is the the weight of the fastest animal? 55
mammal_df.sort_values(by='speed', ascending=False)
# e. What is the overal percentage of specials? 9.3%
mammal_df['specials'].value_counts(normalize=True).mul(100)
# f. How many animals are hoppers that are above the median speed? What percentage is this?
median = mammal_df['speed'].median()
mammal_df.hoppers == [(True &(mammal_df.speed > median)]
