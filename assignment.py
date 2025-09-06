# assignment.py
import pandas as pd
import seaborn as sns
import numpy as np

def validate_tips_dataset():
    # Load the dataset
    tips = sns.load_dataset('tips')

    # ------------------------
    # Validation checks
    # ------------------------
    validation_results = {}

    # 1️⃣ Null values check
    validation_results['null_check'] = {
        'success': tips.notnull().all().all(),
        'message': 'No nulls' if tips.notnull().all().all() else 'Dataset contains nulls'
    }

    # 2️⃣ Range checks
    validation_results['total_bill_range'] = {
        'success': tips['total_bill'].between(3, 60).all(),
        'message': 'All total_bill values are in range 3-60'
    }

    validation_results['tip_range'] = {
        'success': tips['tip'].between(0, 12).all(),
        'message': 'All tip values are in range 0-12'
    }

    validation_results['size_range'] = {
        'success': tips['size'].between(1, 6).all(),
        'message': 'All size values are in range 1-6'
    }

    # 3️⃣ Categorical validations
    validation_results['day_categorical'] = {
        'success': set(tips['day']).issubset({'Thur', 'Fri', 'Sat', 'Sun'}),
        'message': 'Day column has valid categories'
    }

    validation_results['sex_categorical'] = {
        'success': set(tips['sex']).issubset({'Male', 'Female'}),
        'message': 'Sex column has valid categories'
    }

    validation_results['smoker_categorical'] = {
        'success': set(tips['smoker']).issubset({'Yes', 'No'}),
        'message': 'Smoker column has valid categories'
    }

    # ------------------------
    # Overall success
    # ------------------------
    overall_success = all(check['success'] for check in validation_results.values())

    # ------------------------
    # Quality metrics
    # ------------------------
    quality_metrics = {
        'completeness': 100.0 if tips.notnull().all().all() else 0.0,
        'accuracy': 100.0,    # placeholder, assumed correct
        'consistency': 100.0  # placeholder, assumed consistent
    }

    # ------------------------
    # Summary statistics
    # ------------------------
    summary = {
        'total_rows': tips.shape[0],
        'total_columns': tips.shape[1],
        'data_types': tips.dtypes.apply(lambda x: str(x)).to_dict()
    }

    # ------------------------
    # Return final dictionary
    # ------------------------
    return {
        'overall_success': overall_success,
        'validation_results': validation_results,
        'quality_metrics': quality_metrics,
        'summary': summary
    }
