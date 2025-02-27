import unittest
from src.SignalDetection import SignalDetection

class TestSignalDetection(unittest.TestCase):
    def test_d_prime_zero(self):
        """Test that d-prime is 0 when hits and false alarms are equal"""
        sd  = SignalDetection(15, 5, 15, 5)
        expected = 0
        obtained = sd.d_prime()
        self.assertAlmostEqual(obtained, expected, places=6)
        
    def test_d_prime_nonzero(self):
        """Test that d-prime is non-zero when hits and false alarms are not equal"""
        sd   = SignalDetection(15, 10, 15, 5)
        expected = -0.421142647060282
        obtained = sd.d_prime()
        self.assertAlmostEqual(obtained, expected, places=6)
        
    def test_criterion_zero(self):
        """Test that criterion is 0 when all trial counts are equal"""
        sd   = SignalDetection(5, 5, 5, 5)
        expected = 0
        obtained = sd.criterion()
        self.assertAlmostEqual(obtained, expected, places=6)
        
    def test_criterion_nonzero(self):
        """Test that criterion is non-zero when all trial counts are not equal"""
        sd   = SignalDetection(15, 10, 15, 5)
        expected = -0.463918426665941
        obtained = sd.criterion()
        self.assertAlmostEqual(obtained, expected, places=6)

    def test_negative_trial_counts(self):
        """Test that negative trial counts raise ValueError"""
        with self.assertRaises(ValueError):
            sd = SignalDetection(hits = -1, misses = 5, falseAlarms = 15, correctRejections = 5)
        with self.assertRaises(ValueError):
            sd = SignalDetection(hits = 5, misses = -1, falseAlarms = 15, correctRejections = 5)
        with self.assertRaises(ValueError):
            sd = SignalDetection(hits = 5, misses = 5, falseAlarms = -1, correctRejections = 5)
        with self.assertRaises(ValueError):
            sd = SignalDetection(hits = 5, misses = 5, falseAlarms = 15, correctRejections = -1)

    def test_invalid_input_types(self):
        """Test that invalid input types raise TypeError"""
        with self.assertRaises(TypeError):
            sd = SignalDetection("1", 5, 15, 5)
        with self.assertRaises(TypeError):
            sd = SignalDetection(5, "1", 15, 5)
        with self.assertRaises(TypeError):
            sd = SignalDetection(5, 5, "15", 5)
        with self.assertRaises(TypeError):
            sd = SignalDetection(5, 5, 15, "5")

    def test_zero_signal_trials(self):
        """Test that zero signal trials raise ValueError"""
        with self.assertRaises(ValueError):
            sd = SignalDetection(hits = 0, misses = 0, falseAlarms = 5, correctRejections = 5)
            
    def test_zero_noise_trials(self):
        """Test that zero noise trials raise ValueError"""
        with self.assertRaises(ValueError):
            sd = SignalDetection(hits = 5, misses = 5, falseAlarms = 0, correctRejections = 0)

if __name__ == '__main__':
    unittest.main()
