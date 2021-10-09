from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')
    # return "Yes we are live"


@app.route('/prediction', methods=['POST'])
def predict_page():
    model = pickle.load(open('LogisticRegression.pickle', "rb"))

    if request.method == 'POST':
        user_input1 = float(request.form.get('input1'))
        user_input2 = float(request.form.get('input2'))
        user_input3 = float(request.form.get('input3'))
        user_input4 = float(request.form.get('input4'))
        user_input5 = float(request.form.get('input5'))
        user_input6 = float(request.form.get('input6'))
        user_input7 = float(request.form.get('input7'))
        user_input8 = float(request.form.get('input8'))

        prediction = model.predict(
            [[user_input1, user_input2, user_input3, user_input4, user_input5, user_input6,
              user_input7, user_input8]])
        if prediction == 0:
            prediction_real = '100%'
        else:
            prediction_real = '0%'
        return render_template("results.html", prediction=prediction_real)


if __name__ == '__main__':
    app.run(debug=True)
