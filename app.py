from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100  # Convert cm to meters
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
