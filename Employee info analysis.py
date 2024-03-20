# Employee_info_analysis.py
import pandas as pd

data = {'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
        'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
        'Age': [30, 40, 25, 35, 45, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
        'Experience': [3, 7, 2, 5, 10, 4]}

employee_df = pd.DataFrame(data)
employee_df

#Use the iloc method to select the first 3 rows of the dataframe.
employee_df.iloc[0:3]

#Use the loc method to select all rows where the Department is "Marketing".
print(employee_df.loc[employee_df['Department'] == 'Marketing'])

#Use the iloc method to select the Age and Gender columns for the first 4 rows of the dataframe.
print(employee_df.iloc[0:5,2:4])

#Use the loc method to select the Salary and Experience columns for all rows where the Gender is "Male".
print(employee_df.loc[employee_df['Gender'] == 'Male',['Salary', 'Experience']])

