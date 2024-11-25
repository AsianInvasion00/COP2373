# Tyler Vo

import numpy as np

# Load the CSV file
file_path = 'grades.csv' 
data = np.genfromtxt(file_path, delimiter=',', skip_header=1, dtype=float, encoding='utf-8')

# Check if the data was loaded correctly
print("Loaded data:")
print(data)

# Ensure the data is 2-dimensional
if data.ndim == 1:
    print("Error: Check the file format and delimiter.")
else:
    # Extract only numeric columns (assuming scores start at the third column)
    numeric_data = data[:, 2:]

    # Display the first few rows of the numeric dataset
    print("First few rows of the dataset:")
    print(numeric_data[:5])

    # Calculate for each exam (columns)
    exam_means = np.mean(numeric_data, axis=0)
    exam_medians = np.median(numeric_data, axis=0)
    exam_std_devs = np.std(numeric_data, axis=0)
    exam_mins = np.min(numeric_data, axis=0)
    exam_maxs = np.max(numeric_data, axis=0)

    print("\nStatistics for each exam (columns):")
    for i, (mean, median, std_dev, min_, max_) in enumerate(zip(exam_means, exam_medians, exam_std_devs, exam_mins, exam_maxs), start=1):
        print(f"Exam {i}: Mean = {mean:.2f}, Median = {median:.2f}, Std Dev = {std_dev:.2f}, Min = {min_}, Max = {max_}")

    # Calculate overall for the entire dataset (all exams combined)
    all_grades = numeric_data.flatten()  
    overall_mean = np.mean(all_grades)
    overall_median = np.median(all_grades)
    overall_std_dev = np.std(all_grades)
    overall_min = np.min(all_grades)
    overall_max = np.max(all_grades)

    print("\nOverall statistics for the entire dataset:")
    print(f"Mean = {overall_mean:.2f}, Median = {overall_median:.2f}, Std Dev = {overall_std_dev:.2f}, Min = {overall_min}, Max = {overall_max}")

    # Determine the number of students who passed and failed each exam
    passing_threshold = 60
    passed_per_exam = np.sum(numeric_data >= passing_threshold, axis=0)
    failed_per_exam = np.sum(numeric_data < passing_threshold, axis=0)

    print("\nNumber of students who passed and failed each exam:")
    for i, (passed, failed) in enumerate(zip(passed_per_exam, failed_per_exam), start=1):
        print(f"Exam {i}: Passed = {passed}, Failed = {failed}")

    # Calculate the overall pass percentage across all exams
    total_grades = numeric_data.size
    total_passed = np.sum(numeric_data >= passing_threshold)
    overall_pass_percentage = (total_passed / total_grades) * 100

    print(f"\nOverall pass percentage across all exams: {overall_pass_percentage:.2f}%")
