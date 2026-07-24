import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.components.data_validation import DataValidator
from src.recommendation_engine import RecommendationEngine
from src.report_generator import ReportGenerator
from src.utils import model_exists

class TestPredictiveMaintenance(unittest.TestCase):

    def test_data_validator_valid(self):
        # Valid inputs (all non-negative)
        self.assertTrue(DataValidator.validate_input(298.0, 308.0, 1500, 40.0, 100))
        
    def test_data_validator_invalid(self):
        # Invalid inputs (negative values)
        self.assertFalse(DataValidator.validate_input(-1.0, 308.0, 1500, 40.0, 100))
        self.assertFalse(DataValidator.validate_input(298.0, -5.0, 1500, 40.0, 100))
        self.assertFalse(DataValidator.validate_input(298.0, 308.0, -100, 40.0, 100))
        self.assertFalse(DataValidator.validate_input(298.0, 308.0, 1500, -10.0, 100))
        self.assertFalse(DataValidator.validate_input(298.0, 308.0, 1500, 40.0, -1))

    def test_recommendation_engine(self):
        self.assertEqual(RecommendationEngine.recommend(85), "Immediate shutdown and inspection")
        self.assertEqual(RecommendationEngine.recommend(65), "Maintenance within 24 hours")
        self.assertEqual(RecommendationEngine.recommend(35), "Schedule preventive maintenance")
        self.assertEqual(RecommendationEngine.recommend(20), "Normal operation")

    def test_report_generator(self):
        report = ReportGenerator.generate(25.5, "Low", "Normal operation")
        self.assertIn("Failure Probability: 25.50%", report)
        self.assertIn("Risk: Low", report)
        self.assertIn("Recommendation: Normal operation", report)

    def test_model_exists(self):
        self.assertTrue(model_exists())

if __name__ == '__main__':
    unittest.main()
