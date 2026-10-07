#!/usr/bin/env python3
"""
Simple CLI Calculator Application
Supports basic operations: add, subtract, multiply, divide
"""

import sys

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def get_number(prompt):
    """Get a number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def get_operation():
    """Get operation from user input"""
    operations = {
        '1': ('add', add),
        '2': ('subtract', subtract),
        '3': ('multiply', multiply),
        '4': ('divide', divide)
    }
    
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("\nEnter choice (1/2/3/4): ")
        if choice in operations:
            return operations[choice]
        print("Invalid choice. Please try again.")

def main():
    """Main calculator function"""
    print("Welcome to the CLI Calculator!")
    
    while True:
        try:
            # Get operation
            operation_name, operation_func = get_operation()
            
            # Get numbers
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            # Perform calculation
            result = operation_func(num1, num2)
            
            # Display result
            print(f"\n{num1} {operation_name} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        
        # Ask if user wants to continue
        again = input("\nDo you want to perform another calculation? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()