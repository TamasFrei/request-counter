from flask import Flask, redirect, render_template, request, url_for
import os
import connection

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/request-counter', methods=['POST', 'GET', 'DELETE', 'PUT'])
def request_counter():
    dir_path = os.path.dirname(os.path.realpath('request_counts.txt'))
    filename = dir_path + '/request_counts.txt'
    counter = connection.read_file(filename)
    if request.method == 'POST':
        counter['POST'] += 1
    elif request.method == 'GET':
        counter['GET'] += 1
    elif request.method == 'DELETE':
        counter['DELETE'] += 1
    elif request.method == 'PUT':
        counter['PUT'] += 1
    connection.write_to_file(filename, counter)
    return redirect(url_for(main))


if __name__ == '__main__':
    app.run(port=5000,
            debug=True)
