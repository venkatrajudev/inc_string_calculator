# String Calculator
A TDD String Calculator
## Features
- **Basic Funcationality**
  - `add("")` returns `0` for an empty string.
  - `add("1")` returns `1` for a single number.
  - `add("1,5")` returns `6` for two numbers.
  - Support any number of comma - separated values (e.g., `add("1,5,9")` returns `15`).
- **Other Features**
  - Support new line as delimiter (e.g., `add("1\n2\n3")` return `6`)
  - Support custom delimter (e.g., `add("//;\n1;2")` return `3`)
  - Negative number throws an exception (e.g., `add("1,-2")` raises negative numbers not allowed `-2`)
  - If multiple negative number throws an exception (e.g., `add("-1,-2")` raises negative numbers not allowed `-1 -2`)
  - Ignores if number greater than 1000 (e.g, `add(1,1001)` return `1`)
    
## Installation Dependecies
- Make sure python 3.x installed
- Install `pytest` using pip (e.g., `pip install pytest`)
## How to run test
- Run `pytest test_calculator.py -v` to see the test results
## Sample test output
![Alt sample output](https://github.com/user-attachments/assets/0d0a0a76-c8cc-4c76-a184-bec0c5ccdbb8)
