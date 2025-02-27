Signal detection theory is a statistical framework for understanding the
performance of human observers (or machines) in detecting signals in noise. It
provides a mathematical description of how well the observer can discriminate
between signal and noise, and how they balance the trade-off between detecting
signals and avoiding false alarms.

* * *

### Background material on SDT

  * Introduction to Signal Detection Theory. [[video](https://youtu.be/bekyQYaG9cc)] [[slides](https://osf.io/e7kpq/)]
  * Signal Detection Theory modeling of recognition memory. [[video](https://youtu.be/Q3TeIdPvmP4)] [[slides](https://osf.io/byune/)]
  * An application of signal detection theory to shape perception. [[video](https://youtu.be/KxLMqBAPpXw)] [[slides](https://osf.io/vn4su/)]
  * Text by David Heeger [[pdf](https://www.cns.nyu.edu/~david/handouts/sdt-advanced.pdf)]

### Formulas

The following formulas are the core of signal detection theory:

#### Hit Rate

The hit rate (H) is the proportion of signal trials that are correctly
detected by the observer. It is calculated as:

$$
\text{H} = \frac{\text{hits}}{\text{hits}+\text{misses}}
$$

where `hits` is the number of correctly detected signals, and `misses` is the
number of signals that were not detected.

#### False Alarm Rate

The false alarm rate (FA) is the proportion of noise trials that are
incorrectly detected as signals by the observer. It is calculated as:

$$
\text{FA} = \frac{\text{false alarms}}{\text{false alarms} + \text{correct rejections}}
$$

where `false alarms` is the number of noise trials that were incorrectly
detected as signals, and `correct rejections` is the number of noise trials
that were correctly identified as noise.

#### d-prime (d')

d-prime (d') is a measure of the observer's sensitivity to the signal, defined
as the difference between the standard deviations of the distributions of
signal and noise:

$$
d' = \Phi^{-1}(\text{H}) - \Phi^{-1}(\text{FA})
$$

where $\Phi^{-1}(\text{H})$
is the _inverse cumulative distribution function of the standard normal
distribution_.

#### Criterion (C)

The criterion (C) is a measure of the observer's response bias, defined as the
participant's deviation from the optimal point above which they should decide
"signal":

$$
C = -0.5 \times \left( \Phi^{-1}(\text{H}) + \Phi^{-1}(\text{FA}) \right)
$$

where $\Phi^{-1}(\text{H})$ and $\Phi^{-1}(\text{FA})$ are as defined above.

* * *

### Your Assignment: Implement Signal Detection Theory in a Python Class

In this assignment, you will write a class in Python that implements the
formulas described above. The class should at least have the following
methods:

  * `d_prime`: Returns the d-prime value given the hit rate and false alarm rate.
  * `criterion`: Returns the criterion value given the hit rate and false alarm rate.

Your implementation should at a minimum pass the unit test suite provided in
the class repository
([link](https://github.com/joachimvandekerckhove/cogs106w25/blob/main/src/tdd/TestSignalDetection.py)).
Your total grade will be based on the passing of a more extensive test suite,
so make sure your code is as error-free as you can get it. I will run the
tests inside the class container so you should make sure your code runs in it
too!

* * *

### Some hints to get started

  1. Start by checking out the test suite ([link](https://github.com/joachimvandekerckhove/cogs106w25/blob/main/src/tdd/TestSignalDetection.py)) to get an idea of what they expect.
  2. Always,  _always_ work inside the class container.
  3. Use the BayesFactor class ([link](https://github.com/joachimvandekerckhove/cogs106w25/blob/main/src/tdd/BayesFactor.py)) as a template.
  4. Start writing your class with the constructor method, which takes four inputs in the right order:

`SignalDetection(hits, misses, falseAlarms, correctRejections)`

* * *

Please submit the link to your GitHub repository.  Links to GitHub
repositories have the format
https://github.com/\<username\>/\<gitarchive\>.

Everyone should submit a link to their own repository. The easiest way to make
sure that everyone's repositories are in sync is by choosing one of your team
as the creator and everyone else can make a
[fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-
requests/working-with-forks/fork-a-repo).

**Make sure the visibility of the repository is set to public.**   [Here's how
to do that.](https://docs.github.com/en/repositories/managing-your-
repositorys-settings-and-features/managing-repository-settings/setting-
repository-visibility#changing-a-repositorys-visibility)

