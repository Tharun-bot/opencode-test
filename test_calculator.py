#!/usr/bin/env python3
"""
Test script for calculator functionality
"""

import subprocess
import sys

def test_calculator():
    """Test calculator operations"""
    print("Testing calculator operations...")
    
    # Test addition
    result = subprocess.run([sys.executable, 'calculator.py'], 
                          input='1\n5\n3\nn', 
                          text=True, 
                          capture_output=True)
    
    print("Addition test completed")
    print("Return code:", result.returncode)
    print("Output:", result.stdout)
    
    # Test subtraction  
    result = subprocess.run([sys.executable, 'calculator.py'], 
                          input='2\n10\n4\nn', 
                          text=True, 
                          capture_output=True)
    
    print("Subtraction test completed")
    print("Return code:", result.returncode)
    print("Output:", result.stdout)

if __name__ == "__main__":
    test_calculator()