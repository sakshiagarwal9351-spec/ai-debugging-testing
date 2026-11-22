# ai-debugging-testing
AI-assisted Python debugging and unit testing project


## Project Overview
This project demonstrates how AI can help identify and fix errors in Python programs and generate unit tests.

## Objectives
- Identify bugs in Python code.
- Use AI for debugging.
- Generate unit tests.
- Test the corrected program.

## Technology Used
- Python
- GitHub
- AI Tools

## Debugging and Testing

### Bugs Identified
1. Incorrect total calculation.
2. Missing empty-list validation.

### Fixes Applied
- Replaced `total = mark` with `total += mark`.
- Added empty-list validation.

### Unit Testing
Created `test_calculator.py` using Python's unittest framework.

### Test Cases
1. Average calculation.
2. Single mark calculation.
3. Empty list validation.
4. Pass result validation.
5. Fail result validation.

### Expected Results
All five test cases should pass successfully.
