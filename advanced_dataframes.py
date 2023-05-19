url = def get_db_url(db_name):
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

#Run python -m pip install pymysql from your terminal to install the mysql client (any folder is fine)
#cd into your exercises folder for this module and run echo env.py >> .gitignore
#Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.

#Use your function to obtain a connection to the employees database.

#Once you have successfully run a query:

#a. Intentionally make a typo in the database url. What kind of error message do you see?
#name urlp is not defined

#b. Intentionally make an error in your SQL query. What does the error message look like?
# pymysql.err.ProgrammingError) (1146, "Table 'employees.semployees' doesn't exist")
#[SQL: SELECT * FROM semployees LIMIT 200]

#Read the employees and titles tables into two separate DataFrames.
titles_db = pd.read_sql('SELECT * FROM titles LIMIT 200', url)
employees_db = pd.read_sql('SELECT * FROM employees LIMIT 200', url)
#How many rows and columns do you have in each DataFrame? Is that what you expected?
titles_db.shape # 200 rows, 4 columns
employees_db.shape # 200 rows, 6 columns
#Display the summary statistics for each DataFrame.
titles_db.describe()
employees_db.describe()
#How many unique titles are in the titles DataFrame?
titles_db.nunique() # 6
#What is the oldest date in the to_date column?
titles_db['to_date'].min()
#What is the most recent date in the to_date column?
titles_db['to_date'].max()

## Exercises Part 2

#Copy the users and roles DataFrames from the examples above.

#What is the result of using a right join on the DataFrames?
# An extra row with NaN for the missing values in users is created.

#What is the result of using an outer join on the DataFrames?
# All data is maintained with nulls placed in missing values for both dfs.

#What happens if you drop the foreign keys from the DataFrames and try to merge them?
# An error with the foreign key not found
#Load the mpg dataset from PyDataset.

#Output and read the documentation for the mpg dataset.

#How many rows and columns are in the dataset?
mpg_df.shape
#Check out your column names and perform any cleanup you may want on them.
mpg_df.info(verbose=True)
#Display the summary statistics for the dataset.
mpg_df.describe()
#How many different manufacturers are there?
mpg_df['manufacturer'].nunique()
#How many different models are there?
mpg_df['model'].nunique()
#Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.
mpg_df['mileage_difference'] = mpg_df.hwy - mpg_df.cty
#Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
mpg_df['average_mileage'] = (mpg_df.cty + mpg_df.hwy) /2
#Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.
mpg_df['is_automatic'] = np.where(mpg_df.trans.str.startswith('a'), 'True', "False")
#Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
mpg_df.groupby('manufacturer').average_mileage.max().sort_values(ascending=False).head(1)
#Do automatic or manual cars have better miles per gallon?
mpg_df.groupby('is_automatic').average_mileage.max()
