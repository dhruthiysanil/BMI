# BMI Calculator

This is a simple Flask-based BMI Calculator app.

## Features
- Calculates BMI based on weight (kg) and height (cm).
- Validates input to ensure:
  - Weight and height are positive numbers.
  - Height is within a realistic range (≤ 272 cm).
  - Weight is within a realistic range (≤ 600 kg).
  - Displays an error message if inputs are invalid or out of bounds.
- Displays BMI category:
  - Underweight
  - Normal weight
  - Overweight
  - Obese

## How to Run
1. Install requirements: `pip install flask`
2. Run the app: `python app.py`
3. Open browser and visit `http://127.0.0.1:5000/`
