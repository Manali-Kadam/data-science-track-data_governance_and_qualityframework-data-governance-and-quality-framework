import unittest
from assignment import validate_tips_dataset
import pandas as pd
import seaborn as sns
import numpy as np

class TestDataGovernance(unittest.TestCase):
    def test_validate_tips_dataset_returns_validation_result(self):
        """Test that the function returns a validation result dictionary"""
        validation_results = validate_tips_dataset()
        self.assertIsInstance(validation_results, dict)
    
    def test_validation_results_structure(self):
        """Test that validation results have the expected structure"""
        validation_results = validate_tips_dataset()
        
        # Check that results contain the expected keys
        expected_keys = ['overall_success', 'validation_results', 'quality_metrics', 'summary']
        for key in expected_keys:
            self.assertIn(key, validation_results, f"Missing key: {key}")
        
        # Check if the validation was successful
        self.assertTrue(validation_results['overall_success'])
    
    def test_validation_checks_implemented(self):
        """Test that all required validation checks are implemented"""
        validation_results = validate_tips_dataset()
        
        # Should have at least 5 validation checks
        validation_checks = validation_results['validation_results']
        self.assertGreaterEqual(len(validation_checks), 5, "Should have at least 5 validation checks")
        
        # Check that all validations passed
        for check_name, check_result in validation_checks.items():
            self.assertTrue(check_result['success'], f"Validation check '{check_name}' failed: {check_result.get('message', 'No message')}")
    
    def test_quality_metrics_calculated(self):
        """Test that quality metrics are calculated correctly"""
        validation_results = validate_tips_dataset()
        
        quality_metrics = validation_results['quality_metrics']
        self.assertIsInstance(quality_metrics, dict)
        
        # Check for expected quality metrics
        expected_metrics = ['completeness', 'accuracy', 'consistency']
        for metric in expected_metrics:
            self.assertIn(metric, quality_metrics, f"Missing quality metric: {metric}")
    
    def test_summary_statistics(self):
        """Test that summary statistics are calculated"""
        validation_results = validate_tips_dataset()
        
        summary = validation_results['summary']
        self.assertIsInstance(summary, dict)
        
        # Check for basic summary statistics
        expected_stats = ['total_rows', 'total_columns', 'data_types']
        for stat in expected_stats:
            self.assertIn(stat, summary, f"Missing summary statistic: {stat}")
    
    def test_data_loading(self):
        """Test that the tips dataset is loaded correctly"""
        # This test ensures the student actually loaded the data
        tips_df = sns.load_dataset('tips')
        self.assertIsInstance(tips_df, pd.DataFrame)
        self.assertGreater(len(tips_df), 0)
        self.assertIn('total_bill', tips_df.columns)
        self.assertIn('tip', tips_df.columns)
        self.assertIn('day', tips_df.columns)
    
    def test_range_validations(self):
        """Test that range validations work correctly"""
        validation_results = validate_tips_dataset()
        
        # Check that range validations are present
        validation_checks = validation_results['validation_results']
        
        # Look for range validation checks
        range_checks = [check for check in validation_checks.keys() if 'range' in check.lower()]
        self.assertGreater(len(range_checks), 0, "Should have range validation checks")
    
    def test_categorical_validations(self):
        """Test that categorical validations work correctly"""
        validation_results = validate_tips_dataset()
        
        # Check that categorical validations are present
        validation_checks = validation_results['validation_results']
        
        # Look for categorical validation checks
        categorical_checks = [check for check in validation_checks.keys() if 'categorical' in check.lower() or 'day' in check.lower()]
        self.assertGreater(len(categorical_checks), 0, "Should have categorical validation checks")

if __name__ == '__main__':
    unittest.main()
