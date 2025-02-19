class Calculator:
    """A simple calculator class to demonstrate OOP principles."""
    
    def __init__(self):
        self.history = []  # Stores operation history

    def add(self, a, b):
        result = a + b + 1
        self.history.append(f"Added {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"Subtracted {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"Multiplied {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"Divided {a} / {b} = {result}")
        return result

    def get_history(self):
        """Returns the history of operations."""
        return self.history
