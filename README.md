# Data Governance and Quality Assignment

## Problem Description

In this assignment, you will create a comprehensive data quality validation framework using pandas and numpy. You will be working with the "tips" dataset from seaborn, which contains information about restaurant tips, and implement various data quality checks to ensure data integrity and compliance with business rules.

## Learning Objectives

By completing this assignment, you will learn:
- How to implement data quality validation using pandas and numpy
- How to create custom data quality checks and validation functions
- How to validate datasets against business rules and constraints
- Best practices for data governance and quality assurance
- How to generate comprehensive data quality reports

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have the following packages installed:
   - pandas
   - seaborn
   - numpy
   - matplotlib (for data visualization)

## Instructions

1. Open the `assignment.py` file.
2. You will find a function definition: `validate_tips_dataset()`.
3. Your tasks are to:
   *   **Task 1**: Load the "tips" dataset from the seaborn library into a pandas DataFrame.
   *   **Task 2**: Implement data quality validation functions for:
       *   Range validation: `total_bill` should be between 3 and 51
       *   Range validation: `tip` should be between 1 and 11
       *   Categorical validation: `day` should only contain ['Thur', 'Fri', 'Sat', 'Sun']
       *   Completeness check: No missing values in critical columns
       *   Consistency check: `tip` should be less than `total_bill`
   *   **Task 3**: Create a comprehensive data quality report with validation results
   *   **Task 4**: Return a dictionary containing validation results and quality metrics

## Hints

*   Use `seaborn.load_dataset('tips')` to get the data.
*   Use pandas methods like `.between()`, `.isin()`, `.isna()`, and `.sum()` for validation.
*   Create validation functions that return boolean results and error counts.
*   Use dictionary comprehension to build your validation results.
*   Consider using `numpy` for numerical operations and statistical calculations.

## Testing Your Solution

Run the test file to verify your implementation:
```bash
python test.py
```

The tests will check:
- That your function returns the correct type of object (dictionary)
- That all validation checks are properly implemented
- That the validation results have the expected structure
- That all validation checks pass successfully
- That data quality metrics are calculated correctly

## Expected Output

Your function should return a dictionary containing:
- `overall_success`: Boolean indicating if all validations passed
- `validation_results`: Dictionary with individual validation check results
- `quality_metrics`: Dictionary with data quality statistics (completeness, accuracy, etc.)
- `summary`: Dictionary with summary statistics about the dataset

## Further Exploration (Optional)

*   Can you create additional validation checks? For example, could you add checks for data distribution or outliers?
*   How would you save your validation results to a JSON file for reporting purposes?
*   Can you create a function to generate a visual data quality report using matplotlib?
*   What other types of data quality checks could you add for this dataset?
*   How would you extend this framework to handle different types of datasets?

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Seaborn Datasets](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
- [Data Quality Best Practices](https://www.ibm.com/cloud/learn/data-quality)
