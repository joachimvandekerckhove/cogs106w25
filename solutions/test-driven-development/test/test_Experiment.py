import unittest
from src.Experiment import Experiment
from src.SignalDetection import SignalDetection

class TestExperiment(unittest.TestCase):
    def setUp(self):
        self.exp = Experiment()
        
    def test_empty_experiment_raises_error(self):
        """Test that methods raise ValueError when experiment has no conditions"""
        with self.assertRaises(ValueError):
            self.exp.sorted_roc_points()
        with self.assertRaises(ValueError):
            self.exp.compute_auc()
            
    def test_add_condition(self):
        """Test adding conditions with and without labels"""
        sdt = SignalDetection(hits=10, misses=5, falseAlarms=3, correctRejections=12)
        self.exp.add_condition(sdt, "Condition A")
        self.assertEqual(len(self.exp.conditions), 1)
        self.assertEqual(self.exp.labels[0], "Condition A")
        
        # Test adding without label
        sdt2 = SignalDetection(hits=15, misses=5, falseAlarms=4, correctRejections=11)
        self.exp.add_condition(sdt2)
        self.assertEqual(len(self.exp.conditions), 2)
        self.assertIsNone(self.exp.labels[1])
        
    def test_auc_perfect_discrimination(self):
        """Test AUC calculation for perfect discrimination case"""
        # Perfect discrimination: points at (0,0), (0,1), and (1,1)
        sdt1 = SignalDetection(hits=0, misses=10, falseAlarms=0, correctRejections=10)  # (0,0)
        sdt2 = SignalDetection(hits=10, misses=0, falseAlarms=0, correctRejections=10)  # (0,1)
        sdt3 = SignalDetection(hits=10, misses=0, falseAlarms=10, correctRejections=0)  # (1,1)
        
        self.exp.add_condition(sdt1)
        self.exp.add_condition(sdt2)
        self.exp.add_condition(sdt3)
        
        auc = self.exp.compute_auc()
        self.assertEqual(auc, 1.0)
        
    def test_auc_chance_performance(self):
        """Test AUC calculation for chance performance"""
        # Chance performance: points at (0,0) and (1,1)
        sdt1 = SignalDetection(hits=0, misses=10, falseAlarms=0, correctRejections=10)  # (0,0)
        sdt2 = SignalDetection(hits=10, misses=0, falseAlarms=10, correctRejections=0)  # (1,1)
        
        self.exp.add_condition(sdt1)
        self.exp.add_condition(sdt2)
        
        auc = self.exp.compute_auc()
        self.assertEqual(auc, 0.5)
        
    def test_sorted_roc_points(self):
        """Test that ROC points are correctly sorted by false alarm rate"""
        # Add conditions in unsorted order
        sdt1 = SignalDetection(hits=8, misses=2, falseAlarms=4, correctRejections=6)   # (0.4, 0.8)
        sdt2 = SignalDetection(hits=6, misses=4, falseAlarms=2, correctRejections=8)   # (0.2, 0.6)
        
        self.exp.add_condition(sdt1, "high")
        self.exp.add_condition(sdt2, "low")
        
        far, hr = self.exp.sorted_roc_points()
        
        # Check specific values and their ordering
        self.assertAlmostEqual(far[0], 0.2)
        self.assertAlmostEqual(far[1], 0.4)
        self.assertAlmostEqual(hr[0], 0.6)
        self.assertAlmostEqual(hr[1], 0.8)

if __name__ == '__main__':
    unittest.main() 