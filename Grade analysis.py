
# grades_analysis.py

#Create a numpy array called "grades" that contains the following grades: [85, 90, 88, 92, 95, 80, 75, 98, 89, 83]
import numpy as np
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

#Use numpy functions to calculate the mean, median, and standard deviation of the grades
mean_grades = np.mean(grades)
print(mean_grades)
median_grades = np.median(grades)
print(median_grades)
std_grades = np.std(grades)
print(std_grades)

#Use numpy function to find the maximum and minimum of the grades.
max_grade = np.max(grades)
print(max_grade)
min_grade = np.min(grades)
print(min_grade)

#Use numpy function to sort the grades in ascending order.
sorted_grades = np.sort([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print(sorted_grades)

#Use numpy function to find the index of the highest grade in the array
print(grades.argmax(axis = 0))

#Use numpy function to count the number of students who scored above 90
print(np.count_nonzero(grades > 90))

#Use numpy function to calculate the percentage of students who scored above 90
print((np.count_nonzero(grades > 90) / np.count_nonzero(grades)) * 100,"%")

#Use numpy function to calculate the percentage of students who scored below 75.
print((np.count_nonzero(grades < 75) / np.count_nonzero(grades)) * 100,"%")

#Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
condition = np.where((grades > 90))
high_performers = grades[condition]
print(high_performers)

#Create a new array called "passing_grades" that contains all the grades above 75.
condition_2 = np.where((grades > 75))
passing_grades = grades[condition_2]
print(passing_grades)