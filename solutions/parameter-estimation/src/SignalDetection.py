import scipy.stats as stats

class SignalDetection:

    def __init__(self, hits, misses, falseAlarms, correctRejections):
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections
        
        self._validate_inputs()

    def _validate_inputs(self):
        # Check that inputs are integers
        if not isinstance(self.hits, int):
            raise TypeError("Hits must be integer.")
        if not isinstance(self.misses, int):
            raise TypeError("Misses must be integer.")
        if not isinstance(self.falseAlarms, int):
            raise TypeError("False alarms must be integer.")
        if not isinstance(self.correctRejections, int):
            raise TypeError("Correct rejections must be integer.")
            
        # Check for non-negative values
        if self.hits < 0:
            raise ValueError("Hits must be non-negative.")
        if self.misses < 0:
            raise ValueError("Misses must be non-negative.")
        if self.falseAlarms < 0:
            raise ValueError("False alarms must be non-negative.")
        if self.correctRejections < 0:
            raise ValueError("Correct rejections must be non-negative.")

        # Check trial counts
        if self.n_signal_trials() == 0:
            raise ValueError("You must have at least one signal trial.")
        if self.n_noise_trials() == 0:
            raise ValueError("You must have at least one noise trial.")

    def hit_rate(self):
        return self.hits / self.n_signal_trials()

    def false_alarm_rate(self):
        return self.falseAlarms / self.n_noise_trials()

    def _z_hit(self):
        hit_rate = self.hit_rate()
        if hit_rate == 1:
            return float('inf')
        elif hit_rate == 0:
            return float('-inf')
        else:
            return stats.norm.ppf(hit_rate)
    
    def _z_fa(self):
        fa_rate = self.false_alarm_rate()
        if fa_rate == 1:
            return float('inf')
        elif fa_rate == 0:
            return float('-inf')
        else:
            return stats.norm.ppf(fa_rate)

    def d_prime(self):
        return self._z_hit() - self._z_fa()

    def criterion(self):
        return -0.5 * (self._z_hit() + self._z_fa())

    def n_correct_responses(self):
        return self.hits + self.correctRejections
    
    def n_incorrect_responses(self):
        return self.misses + self.falseAlarms
    
    def n_signal_trials(self):
        return self.hits + self.misses
    
    def n_noise_trials(self):
        return self.falseAlarms + self.correctRejections
    
    def n_total_responses(self):
        return self.n_correct_responses() + self.n_incorrect_responses()