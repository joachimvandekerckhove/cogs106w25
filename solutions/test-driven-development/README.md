# Signal Detection Theory II: Experiments and ROC Curves

In this assignment, you will extend your **Signal Detection Theory (SDT)**
implementation to handle multiple conditions and analyze performance across an
experiment. Specifically, you will:

  1. Implement an **Experiment** class that stores multiple SDT objects.
  2. Compute the **ROC curve** and **AUC (Area Under the Curve)** for an entire experiment.
  3. Add appropriate **unit tests** to verify the functionality.

* * *

### **Background on SDT and ROC Curves**

Signal detection theory provides a framework for analyzing how well an
observer (human or machine) can distinguish between signal and noise. In real
experiments, we often have multiple conditions, each with different levels of
sensitivity and bias. To summarize performance across conditions, we use:

  * **ROC Curve** (Receiver Operating Characteristic): A plot of **hit rate (vertical axis) vs.  false alarm rate (horizontal axis)** across different conditions.
  * **AUC (Area Under the Curve)** : A single value summarizing overall performance--higher values indicate better discrimination.

#### **Reference Material**

  * A blog post that explains ROCs and AUC well [[link](https://www.displayr.com/what-is-a-roc-curve-how-to-interpret-it/)].

* * *

### **Your Assignment: Implement the Experiment Class**

You will implement a new `Experiment` class that manages multiple conditions
and computes the **ROC curve and AUC**.

* * *

### **Class Specification**

Your `Experiment` class should have the following methods:

#### **1\. Constructor**

**`__init__(self)`**

  * **Purpose** : Initializes an empty list to store SDT objects and their corresponding condition labels.

  * **Parameters** : None.

  * **Returns** : None.

  * **Example Usage** :
    
        exp = Experiment()

  * **Expectation** : A new object is created.

#### **2\. Add Condition**

**`add_condition(self, sdt_obj: SignalDetection, label: str = None) -> None`**

  * **Purpose** : Adds an `SignalDetection` object and an optional label to the experiment.

  * **Parameters** :

    * `sdt_obj` (`SignalDetection`): An instance of the `SignalDetection` class representing a condition.
    * `label` (`str`, optional): A label describing the condition (e.g., `"High Noise"`).
  * **Returns** : None.

  * **Example Usage** :
    
        exp.add_condition(SignalDetection(40, 10, 20, 30), label="Condition A")

  * **Expectation** : The `exp' object contains an additional SignalDetection object with the associated label.

* * *

#### **3\. Generate Sorted ROC Points**

**`sorted_roc_points(self) -> tuple[list[float], list[float]]`**

  * **Purpose** : Returns **sorted** false alarm rates and hit rates for plotting the ROC curve.

  * **Parameters** : None.

  * **Returns** : A tuple containing:

    * **First element** : A sorted list of **false alarm rates**.
    * **Second element** : A sorted list of **hit rates** corresponding to the sorted false alarm rate values.
  * **Example Usage** :
    
        falseAlarmRate, hitRate = exp.sorted_roc_points()

  * **Constraints** :

    * Both lists must be **sorted in ascending order of false alarm rate**.
    * If no conditions are present, the method should raise a `ValueError`.

* * *

#### **4\. Compute AUC**

**`compute_auc(self) -> float`**

  * **Purpose** : Computes the **Area Under the Curve (AUC)** for the stored SDT conditions.

  * **Parameters** : None.

  * **Returns** : A floating-point number representing the AUC value.

  * **Example Usage** :
    
        auc_score = exp.compute_auc()
    print(f"AUC: {auc_score:.3f}")

  * **Expectation** :

    * Computes the AUC, possibly using the [Trapezoidal Rule](https://blogs.sas.com/content/iml/2011/06/01/the-trapezoidal-rule-of-integration.html).
    * If no conditions have been added, the method should raise a `ValueError`.

* * *

#### **5\. Plot ROC Curve**

**`plot_roc_curve(self, show_plot: bool = True)`**

You may implement this however you like. It will help you do the rest of the
assignment but will not be part of the grading.

* * *

### **Unit Testing Requirements**

Your implementation must include unit tests that verify:

  * `compute_auc()` produces expected AUC values for known test cases, such as 
    * AUC = 0.5 if there are only two experiments and they fall at (0,0) and (1,1).
    * AUC = 1 if there are three experiments and they fall at (0,0), (0,1), and (1,1).
  * `sorted_roc_points()` correctly returns **false alarm rate and hit rate sorted by false alarm rate**.
  * `add_condition()` correctly stores SignalDetection objects and labels.
  * Edge cases such as **empty experiment (no conditions)** raise the appropriate errors.

Write at least 8 tests. Ideally, _write the tests first_.

* * *

### **Hints to Get Started**

  * **Start by reviewing the previous test suite**.
  * **Your code must run in the class container** , so develop and test inside it.
  * **Use`matplotlib` for plotting**.
  * **Follow best practices** : Name variables according to a consistent scheme, avoid duplicating code, etc.

* * *

You should make a new GitHub repository (or a fork) called `test-driven-
development` with subfolder `src/`, containing these files named exactly like
this:

    
    
    test-driven-development/  
    └── src/  
        ├── Experiment.py  
        ├── SignalDetection.py  
        └── TestExperiment.py  
    

* * *

Please submit the link to your GitHub repository.  The link to your GitHub
repository should have the format `https://github.com/<your-username>/test-driven-development`.

**Make sure the visibility of the repository is set to public.**   [Here's how to do that.](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility#changing-a-repositorys-visibility)

