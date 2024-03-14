

#LOAN_ANALYSIS.PY

#SOLUTION
import numpy as np
# Step 1: Specify the path to your CSV file
csv_file_path = "Loan_prediction_dataset.csv"

# Step 2: Use the open() function to open csv file and assign the result to a variable.
loan_data = open(csv_file_path, "r")

# Step 3: use the readline() function to print the first two rows of the file
print(loan_data.readline())
print(loan_data.readline())

# Step 4: Load the CSV data using genfromtxt()
# Use the delimiter parameter to specify that the values in the file are separated by commas.
data = np.genfromtxt(loan_data, delimiter=',', skip_header=0, dtype=None, encoding=None)
#print(data)

# Step 5: Extract the loan amounts from the dataset and store in a variable "Loan_Amount"
# usecols=8. 8 is the index of the loan amount column that we wish to access
# Replace 8 with the index of the column you want to extract (0-based index)
Loan_Amount = np.genfromtxt(csv_file_path, delimiter=',', filling_values=0, usecols=8, skip_header=1, dtype=None, encoding=None)

# Print the extracted column data
#print(Loan_Amount)

# Step 6: Perform basic statistical analysis
mean_loan_amount = np.mean(Loan_Amount)
median_loan_amount = np.median(Loan_Amount)
std_deviation_loan_amount = np.std(Loan_Amount)

#Step 4: Display the results
print(f"Mean Loan Amount: {mean_loan_amount:.2f}")
print(f"Median Loan Amount: {median_loan_amount:.2f}")
print(f"Standard Deviation of Loan Amount: {std_deviation_loan_amount:.2f}")


loan_data.close()

