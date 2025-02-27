# Assignment: Implementing a 3PL Model with Maximum Likelihood Estimation

## Background

The three-parameter logistic (3PL) model describes the probability of a correct response. For this assignment, you will implement a simplified version in which the difficulty parameters $b_i$ are known to be (2, 1, 0, -1, -2) in five conditions. Moreover, the person parameter $\theta$ is fixed at 0. We will focus on estimating the discrimination parameter $a$ for a single participant and the base rate parameter $c$.

### Mathematical Formulation

The probability of a correct response in condition $i$ is given by:

$$
P(\text{correct} | a, \theta, b_i, c) = c + (1 - c) \frac{1}{1 + e^{-a (\theta - b_i)}}
$$

where $\theta$ is the participant ability parameter, $a$ is the discrimination parameter, $b_i$ is the difficulty parameter for condition $i$, and $c$ is the base rate parameter. 

For each condition $i$, we observe:
- $n_i^c$: number of correct responses
- $n_i^e$: number of errors

The likelihood function for the data is then:

$$
L(a, \theta, b_i, c) = \prod_{i=1}^n \left[ P(\text{correct} | a, \theta, b_i, c) \right]^{n_i^c} \left[ 1 - P(\text{correct} | a, \theta, b_i, c) \right]^{n_i^e}
$$

The negative log likelihood function for the data is:

$$
-\log L(a, \theta, b_i, c) = -\sum_{i=1}^n \left[ n_i^c \log\left(P\left(\text{correct} | a, \theta, b_i, c\right)\right) + n_i^e \log\left(1 - P\left(\text{correct} | a, \theta, b_i, c\right)\right) \right]
$$

This will be our loss function, that needs to be minimized.

### Logit Link for the Base Rate Parameter

It will be convenient to use the logit link for the base rate parameter. That means that we will be using the logit function to transform the base rate parameter $c$ into a variable $q$ that can take any value on the real line. This is a common technique in statistics for dealing with parameters that are bounded between 0 and 1.  Instead of estimating $c$, we will estimate $q$, which will be easier because it is not bounded.  Then after estimating $q$, we will transform it back to $c$ using the inverse logit function.

Logit link (left) and inverse logit link (right):

$$
q = \log \left( \frac{c}{1 - c} \right) \Leftrightarrow c = \frac{1}{1 + e^{-q}}
$$

The negative log-likelihood function with the logit link becomes:

$$
-\log L(a, \theta, b_i, q) = -\sum_{i=1}^n \left[
      n_i^c \log \left[ 
         \frac{1}{1 + e^{-q}} + \left(1 - \frac{1}{1 + e^{-q}}\right) \frac{1}{1 + e^{-a(\theta-b_i)}} 
      \right] + 
      n_i^e \log \left[ 
         1 - \frac{1}{1 + e^{-q}} - \left(1 - \frac{1}{1 + e^{-q}}\right) \frac{1}{1 + e^{-a(\theta-b_i)}} 
      \right] 
\right]
$$

This is a little cumbersome, but when we split the calculation into components, it will be easy to implement.


## Task Description

### Part I: Create a Python class called SimplifiedThreePL that implements the following:

#### Class Requirements:
1. Constructor should accept:
   - An object of class `Experiment`
   - (If you are not happy with your implementation of `Experiment` or `SignalDetection`, you can use the one provided in the repo.)

2. Methods:
   - `summary(self)`: Returns a dictionary with the following keys:
     - `n_total`: total number of trials
     - `n_correct`: number of correct trials
     - `n_incorrect`: number of incorrect trials
     - `n_conditions`: number of conditions
   - `predict(self, parameters)`: Returns probability of correct response in each condition, given the parameters
   - `negative_log_likelihood(self, parameters)`: Computes negative log-likelihood of the data given the parameters
   - `fit(self)`: Implements maximum likelihood estimation to find best fitting discrimination parameter and base rate parameter
   - `get_discrimination(self)`: Returns estimate of discrimination parameter $a$
   - `get_base_rate(self)`: Returns estimate of base rate parameter $c$ (not $q$!)

3. Attributes:
   - `_base_rate`: base rate parameter $c$
   - `_logit_base_rate`: logit of the base rate parameter $q$
   - `_discrimination`: discrimination parameter $a$
   - `_is_fitted`: boolean indicating whether the model has been fitted successfully (if the model has not been fitted, the user should not be able to access the parameters)

Note that these attributes are private, so you need to create methods to get and set them.

#### Example Usage:

    # Example of intended usage
    model = SimplifiedThreePL(experiment)  # initialize the model
    model.summary()  # should return a dictionary with the number of trials, correct trials, incorrect trials, and number of conditions
    est_a = model.get_discrimination()  # this should throw an error because the model has not been fitted yet
    model.fit()  # fit the model
    est_a = model.get_discrimination()  # should return discrimination parameter $a$
    est_c = model.get_base_rate()  # should return base rate parameter $c$


### Part II: Unit Tests

Using unittest, write multiple test cases:

1. Initialization:
   - Test that constructor properly handles valid inputs
   - Test that constructor raises appropriate exceptions for invalid inputs (e.g., mismatched lengths, or trying to access parameter estimates that aren't determined yet)

2. Prediction:
   - Test that `predict()` returns values between 0 and 1 (inclusive)
   - Test that higher base rate values $c$ result in higher probabilities, all other parameters being equal
   - Test that higher difficulty values $b_i$ result in lower probabilities when $a$ is positive, and higher probabilities when $a$ is negative
   - Test that higher ability parameters $\theta$ result in higher probabilities when $a$ is positive, and lower probabilities when $a$ is negative
   - Test that prediction with known parameter values matches the expected output

3. Parameter Estimation:
   - Test that `negative_log_likelihood` improves after fitting compared to the initial guess of the parameters
   - Test that a larger estimate of $a$ is returned when we supply data with a steeper curve (i.e., higher discrimination)
   - Verify that the user cannot request parameter estimates before the model is fit

4. Integration:
   - Test that parameters remain approximately stable when fitting multiple times (i.e., that `fit()` approximately converges to stable values)
   - In your unit test class, create one integration test that:
       1. Creates a dataset with five conditions and 100 trials per condition, with accuracy rates of exactly 0.55, 0.60, 0.75, 0.90, and 0.95 (do not use random numbers)
       2. Fits the model to this data
       3. Verifies that predictions for each condition align with the observed response patterns

5. Corruption:
   - Write corruption tests to make sure that the user can't accidentally create an inconsistent object (we will assume that the user is not malicious and is aware they should not be accessing private attributes that start with underscores directly)


### Part III: Bash script to run tests

Create a `#!` bash script in `src/run_tests.sh` that runs the tests.


## Notes
- You will need the `SignalDetection` and `Experiment` classes, place them in their own `.py` files in `src/`
- You will need `numpy` and scipy`
- To test `numpy` arrays, you need a `numpy` function:

```python
    def test_default_difficulty(self):
        """Test that default difficulty values are 2, 1, 0, -1, -2."""
        self.assertTrue(np.array_equal(self.model._difficulties, np.array([2.0, 1.0, 0.0, -1.0, -2.0])))
```

## Submission Requirements
- Submit a link to your github repo, which should contain the following:
    - `src/SimplifiedThreePL.py` (Python file containing `SimplifiedThreePL` class)
    - `src/Experiment.py` (Python file containing `Experiment` class)
    - `src/SignalDetection.py` (Python file containing `SignalDetection` class)
    - `tests/test_SimplifiedThreePL.py` (Unit and integration tests)
    - `src/run_tests.sh` (Bash script to run tests)
    - `__init__.py` files in appropriate places
