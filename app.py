from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    author = "starsnstripes"
    name = "hacker"

    return render_template('index.html', author=author, name=name)

@app.route('/arena')
def mass_drill():

    return render_template('drill.html')

if __name__ == '__main__':
    app.run()
