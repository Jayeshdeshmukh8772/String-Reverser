from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    reversed_string = ''
    if request.method == 'POST':
        original_string = request.form['input_string']
        reversed_string = original_string[::-1]
    return render_template('index.html', reversed=reversed_string)

if __name__ == '__main__':
    app.run(debug=True)
