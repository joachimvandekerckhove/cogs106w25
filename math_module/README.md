# Running Tests with `unittest`

To run tests in this project using Python's built-in `unittest` module, use the following command from the root directory:

```sh
python -m unittest discover -s tests
```

### Explanation:
- `python -m unittest discover` automatically discovers and runs tests.
- `-s tests` specifies the `tests` directory as the location to search for test modules.

Ensure that:
- The `tests` directory contains an `__init__.py` file (even if empty) to mark it as a package.
- Your test files follow the naming convention `test_*.py` so they are detected by `unittest`.

You can also run a specific test file directly:

```sh
python -m unittest tests.test_operations
```

Or run a specific test case:

```sh
python -m unittest tests.test_operations.TestClass.test_method
```

