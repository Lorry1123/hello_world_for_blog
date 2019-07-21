from flask import Flask

app = Flask('app')

@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/index')
def index_page():
    return 'this is a index page'

if __name__ == '__main__':
    app.run(port=80, host='0.0.0.0', debug=True)