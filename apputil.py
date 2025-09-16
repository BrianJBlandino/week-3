# Exercise 1

# The Fibonacci Series starts with 0 and 1. Each of the following numbers are the sum of the previous two numbers in the series:
# 0 1 1 2 3 5 8 13 21 34 ...
# So, fib(9) = 34.
# Write a recursive function (fib) that, given n, will return the nth number of the Fibonacci Series.

def fib(n):
    
    """Creating a function that takes the parameter and
    returns a value that is the sum of the previous two numbers
    in the series imitating the Fibonacci Series"""
    
    # Base case created in order to stop the function from running indefinitely
    if n == 0:
        return 0
        
    # Second base case created in order to stop the function from running indefinitely
    elif n == 1:
        return 1
        
    # This is the recursive case in the function to propertly calculate
    # and return the value of the previous two numbers
    else:
        return fib(n - 1) + fib(n - 2)

# Exercise 2
# Write a (single) recursive function, to_binary(), that converts an integer into its binary representation. So, for example:
# to_binary(2)   -->  10
# to_binary(12)  -->  1100

def to_binary(n):
    
    """Creating a function in order to produce the binary representative
    of the integer variable n"""
    
    # Base case created to ensure the function does not run indefinitely
    if n <= 1:
        return str(n)
        
    # This is the recursive case to return the proper mathematical result
    return to_binary(n // 2) + str(n % 2)

# Exercise 3

# Use the raw Bellevue Almshouse Dataset (df_bellevue) extracted at the top of the lab (i.e., with pd.read_csv ...).
# Write a function for each of the following tasks. Name these functions task_i() (i.e., without any input arguments).

# Task 1: Return a list of all column names, sorted such that the first column has the least missing values, and the last column has the most missing values (use the raw column names).
# Note: there is an issue with the gender column you'll need to remedy first ...

# Task 2: Return a data frame with two columns:
# the year (for each year in the data), year
# the total number of entries (immigrant admissions) for each year, total_admissions

# Task 3: Return a series with:
# Index: gender (for each gender in the data)
# Values: the average age for the indexed gender.

# Task 4: Return a list of the 5 most common professions in order of prevalence (so, the most common is first).
# For each of these, if there are messy data issues, use the print statement to explain.

# TASK 1
# Importing the necessary Python libraries
import pandas as pd
import numpy as np

def task_1():
    """Creating a function that returns a list of all the column names in the 
    df_bellevue dataset that is sorted as cuh that the first column has the least missing values
    and the last column has the most missing values"""

    # First bringing in the dataset and reading it
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)

    # Creating a list of the valid values in the gender column
    valid_genders = ['m', 'w']
    
    # Replacing outlier values that do not fit the scope of the data
    df_bellevue['gender'] = df_bellevue['gender'].apply(lambda gender: gender if gender in valid_genders else np.nan)

    # Creating a variable for the sum of the missing values in each column
    missing_counts = df_bellevue.isnull().sum()

    # Sorting the columns by the number of missing values in ascending order and making it a list
    sorted_columns = missing_counts.sort_values().index.tolist()

    # Returning the sorted columns result
    return sorted_columns

task_1()
['date_in',
 'last_name',
 'first_name',
 'gender',
 'age',
 'profession',
 'disease',
 'children']

# TASK 2
# Importing the necessary Python libraries
import pandas as pd
import numpy as np

def task_2():
    """Creating a function that returns a data frame with a column of the year for each year
    in the data frame, and a column for the total number of entries (immigrant admissions)
    for each year, total_admissions"""

    # First bringing in the dataset and reading it
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)

    # Pulling the year out of the date_in column
    df_bellevue['year'] = pd.to_datetime(df_bellevue['date_in']).dt.year

    # Grouping the results by year and counting the number of entries for each year
    result = df_bellevue.groupby('year').size().reset_index(name='total_admissions')

    # Renaming the headers of the columns to 'year' and 'total_admissions'
    result.columns = ['year', 'total_admissions']

    # Returning the result
    return result

task_2()
	year	total_admissions
0	1846	3073
1	1847	6511

# TASK 3
# Importing the necessary Python libraries
import pandas as pd
import numpy as np

def task_3():
    """Creating a function to return a series from the Bellevue data with:
    Index: gender (for each gender in the data)
    Values: the average age for the indexed gender"""

    # First bringing in the dataset and reading it
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)

    # Creating a list of the valid values in the gender column
    valid_genders = ['m', 'w']
    
    # Replacing outlier values that do not fit the scope of the data
    df_bellevue['gender'] = df_bellevue['gender'].apply(lambda gender: gender if gender in valid_genders else np.nan)
    
    # Cleaning and converting the 'age' column to numbers, changing possible errors to NaN values
    df_bellevue['age'] = pd.to_numeric(df_bellevue['age'], errors='coerce')
    
    # Creating a variable that groups the data by the gender and calculating the mean age of each gender
    average_age_by_gender = df_bellevue.groupby('gender')['age'].mean()
    
    # Returning the result
    return average_age_by_gender

task_3()
gender
m    31.813433
w    28.725162
Name: age, dtype: float64

# TASK 4
# Importing the necessary Python libraries
import pandas as pd
import numpy as np
from collections import Counter

def task_4():
    """Creating a function that will return a list of the 5 most common professions 
    in order of prevalence. For each of these, if there are messy data issues,
    the print statements will explain"""

    # First bringing in the dataset and reading it
    url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
    df_bellevue = pd.read_csv(url)

    # Cleaning the profession column to allow for proper data retrieval
    if 'profession' in df_bellevue.columns:
        df_bellevue['profession'] = df_bellevue['profession'].str.lower().str.strip()
    else:
        print("Error: 'profession' column is missing in the dataset.")
        return

    # Counting the number of occurrences of each profession, not counting missing of NaN values
    profession_counts = Counter(df_bellevue['profession'].dropna())

    # Checking for empty strings, 'unknown' value, or 'none' values in the profession column
    # removing the above values from the calculations after checking for them
    if '' in profession_counts:
        print("Note: Empty strings detected in 'profession' column.")
        profession_counts.pop('')

    if 'unknown' in profession_counts:
        print("Note: 'unknown' is a placeholder in the 'profession' column.")
        profession_counts.pop('unknown')

    if 'none' in profession_counts:
        print("Note: 'none' appears in the 'profession' column, possibly indicating no profession.")
        profession_counts.pop('none')

    # Find the 5 most common professions
    most_common_professions = profession_counts.most_common(5)

    # Return the results
    return most_common_professions

task_4()
[('laborer', 3108),
 ('married', 1584),
 ('spinster', 1521),
 ('widow', 1053),
 ('shoemaker', 158)]
