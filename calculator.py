class Calculator:
    def add(self, a, b):
        """Adds two numbers and returns the result."""
        return a+b

    def subtract(self, a, b):
        """Subtracts the second number from the first and returns the result."""
        return a-b

    def multiply(self, a, b):
        """Multiplies two numbers and returns the result."""
        return a*b

    def divide(self, a, b):
        """Divides the first number by the second and returns the result.
        Raises a ValueError if the second number is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a/b

    def power(self, base, exponent):
        """Raises the base to the power of the exponent and returns the result."""
        return base**exponent

    def modulus(self, a, b):
        """Calculates the modulus of two numbers and returns the result."""
        return a%b
