from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('bmi_form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])

        # Backend validation
        if weight <= 0 or height_cm <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        if weight > 600:
            return render_template('error.html', 
                                 message="Weight must be ≤ 600 kg.",
                                 error_type="weight")

        if height_cm > 272:
            return render_template('error.html', 
                                 message="Height must be ≤ 272 cm.",
                                 error_type="height")

        if height_cm < 50:
            return render_template('error.html', 
                                 message="Height must be ≥ 50 cm.",
                                 error_type="height")

        if weight < 10:
            return render_template('error.html', 
                                 message="Weight must be ≥ 10 kg.",
                                 error_type="weight")

        # BMI Calculation
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        # BMI Category
        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"
            advice = "Consider consulting a healthcare provider for a healthy weight gain plan."
        elif bmi < 24.9:
            category = "Normal weight"
            color = "#27ae60"
            advice = "Great! You're in the healthy weight range. Maintain your current lifestyle."
        elif bmi < 29.9:
            category = "Overweight"
            color = "#f39c12"
            advice = "Consider a balanced diet and regular exercise to reach a healthier weight."
        else:
            category = "Obese"
            color = "#e74c3c"
            advice = "It's recommended to consult with a healthcare provider for a weight management plan."

        return render_template('bmi_result.html', 
                             bmi=bmi, 
                             category=category, 
                             color=color,
                             advice=advice,
                             weight=weight,
                             height=height_cm)

    except ValueError as e:
        return render_template('error.html', 
                             message="Invalid input. Please enter valid positive numbers for weight and height.",
                             error_type="input")

if __name__ == '__main__':
    app.run(debug=True)
