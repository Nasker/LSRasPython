from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    # A simple form for input
    form = """
    <form method="POST" action="/submit">
        <input type="text" name="user_input" />
        <input type="submit" />
    </form>
    """
    return render_template_string(form)


@app.route('/submit', methods=['POST'])
def submit():
    # Get the input from the form
    user_input = request.form.get('user_input')
    # Print the input to the console
    print(user_input)
    return 'Success!'


if __name__ == '__main__':
    app.run(debug=True)
