url = def get_db_url(user, host, password, db_name):
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