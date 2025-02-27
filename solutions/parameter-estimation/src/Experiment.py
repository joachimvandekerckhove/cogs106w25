from typing import List, Tuple, Optional
from src.SignalDetection import SignalDetection

class Experiment:
    def __init__(self):
        """Initialize an empty experiment."""
        self.conditions: List[SignalDetection] = []
        self.labels: List[Optional[str]] = []
        
    def add_condition(self, sdt_obj: SignalDetection, label: str = None) -> None:
        """Add a SignalDetection object and optional label to the experiment."""
        self.conditions.append(sdt_obj)
        self.labels.append(label)
        
    def sorted_roc_points(self) -> Tuple[List[float], List[float]]:
        """Return sorted false alarm rates and corresponding hit rates."""
        if not self.conditions:
            raise ValueError("No conditions available in the experiment")
            
        # Calculate hit rates and false alarm rates for all conditions
        hit_rates = [sdt.hit_rate() for sdt in self.conditions]
        false_alarm_rates = [sdt.false_alarm_rate() for sdt in self.conditions]
        
        # Sort based on false alarm rates
        sorted_pairs = sorted(zip(false_alarm_rates, hit_rates))
        sorted_fars, sorted_hrs = zip(*sorted_pairs)
        
        return list(sorted_fars), list(sorted_hrs)
        
    def compute_auc(self) -> float:
        """Compute the Area Under the Curve using the trapezoidal rule."""
        if not self.conditions:
            raise ValueError("No conditions available in the experiment")
            
        false_alarm_rates, hit_rates = self.sorted_roc_points()
        
        # Add implicit points (0,0) and (1,1) if they don't exist
        if false_alarm_rates[0] != 0:
            false_alarm_rates = [0.0] + false_alarm_rates
            hit_rates = [0.0] + hit_rates
        if false_alarm_rates[-1] != 1:
            false_alarm_rates = false_alarm_rates + [1.0]
            hit_rates = hit_rates + [1.0]
            
        # Compute AUC using the trapezoidal rule
        auc = 0.0
        for i in range(len(false_alarm_rates) - 1):
            width = false_alarm_rates[i + 1] - false_alarm_rates[i]
            height = (hit_rates[i] + hit_rates[i + 1]) / 2
            auc += width * height
            
        return auc
        
    def plot_roc_curve(self, show_plot: bool = True) -> None:
        """Plot the ROC curve using matplotlib."""
        try:
            import matplotlib.pyplot as plt
            
            false_alarm_rates, hit_rates = self.sorted_roc_points()
            
            plt.figure(figsize=(8, 8))
            plt.plot(false_alarm_rates, hit_rates, 'bo-', label='ROC Curve')
            plt.plot([0, 1], [0, 1], 'k--', label='Chance Level')
            plt.xlabel('False Alarm Rate')
            plt.ylabel('Hit Rate')
            plt.title('ROC Curve')
            plt.legend()
            plt.grid(True)
            
            if show_plot:
                plt.show()
        except ImportError:
            print("matplotlib is required for plotting") 