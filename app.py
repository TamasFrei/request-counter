from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/')
def main():
    global counter
    counter += 1
    return render_template('index.html', counter=counter)


@app.route('/request-counter')
def request_counter():
    global counter
    counter += 1
    return redirect('/')


counter = 0
if __name__ == '__main__':
    app.run(port=5000,
            debug=True)
