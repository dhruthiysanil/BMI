from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('bmi_form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = request.form['weight']
    height = request.form['height']

    try:
        weight = float(weight)
        height_cm = float(height)

        if weight <= 0 or height_cm <= 0:
            raise ValueError("Positive numbers only.")

        # Check if both values are unrealistic
        if weight > 600 and height_cm > 272:
            return "<h3 style='color:red;'>Both weight and height are out of bounds. Please enter realistic values (Weight ≤ 600 kg, Height ≤ 272 cm).</h3><a href='/'>Go Back</a>"

        if height_cm > 272:
            return "<h3 style='color:red;'>Height is out of bounds. Please enter a value within a realistic range (≤ 272 cm).</h3><a href='/'>Go Back</a>"

        if weight > 600:
            return "<h3 style='color:red;'>Weight is out of bounds. Please enter a value within a realistic range (≤ 600 kg).</h3><a href='/'>Go Back</a>"

        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            result = "Underweight"
        elif bmi < 24.9:
            result = "Normal weight"
        elif bmi < 29.9:
            result = "Overweight"
        else:
            result = "Obese"

        return render_template('bmi_result.html', bmi=bmi, result=result)

    except ValueError:
        return "<h3 style='color:red;'>Please enter valid positive numbers for weight and height.</h3><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
