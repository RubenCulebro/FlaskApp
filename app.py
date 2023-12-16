from flask import Flask, render_template, request
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)


#Loading the models
linear_model = pickle.load(open('linear_regression.pkl', 'rb'))
logistic_model = pickle.load(open('logistic_regression.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Render the home page with a form for user input
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        print(request.form)
        prediction_type = request.form['prediction_type']

        if prediction_type == 'glucose':
            return render_template('glucose_prediction.html')

        elif prediction_type == 'diabetes':
            return render_template('diabetes_prediction.html')



# Endpoint to handle the prediction
@app.route('/predict_glucose', methods=['POST'])
def predict_glucose():
    if request.method == 'POST':
        pregnancies = float(request.form['pregnancies'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree_function = float(request.form['diabetes_pedigree_function'])
        age = float(request.form['age'])
        outcome = float(request.form['outcome'])

        # Scaling the input data
        input_data = [[pregnancies, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
        input_data_scaled = scaler.transform(input_data)
        input_data_scaled_with_outcome = np.append(input_data_scaled, [[outcome]], axis=1)

        predicted_glucose = linear_model.predict(input_data_scaled_with_outcome)
        predicted_glucose[0] = "{:.2f}".format(predicted_glucose[0])
        return render_template('glucose_result.html', predicted_glucose=predicted_glucose[0])




@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    if request.method == 'POST':
        pregnancies = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree_function = float(request.form['diabetes_pedigree_function'])
        age = float(request.form['age'])

        # Assuming your input_data is a NumPy array
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

        # Extracting the glucose column
        glucose_column = input_data[:, 1]
        # Dropping the glucose column before scaling
        input_data_without_glucose = np.delete(input_data, 1, axis=1)
        # Scaling the input data without glucose
        input_data_scaled_without_glucose = scaler.transform(input_data_without_glucose)
        # Appending the glucose column back at the same position
        input_data_scaled_with_glucose = np.insert(input_data_scaled_without_glucose, 1, glucose_column, axis=1)

        predicted_diabetes = logistic_model.predict(input_data_scaled_with_glucose)
        print("Yes this is diabetes",predicted_diabetes)
        return render_template('diabetes_result.html', predicted_diabetes=predicted_diabetes[0])

if __name__ == '__main__':
    app.run(debug=True)