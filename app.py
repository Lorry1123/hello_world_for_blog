from flask import Flask

app = Flask('app')

@app.route('/')
def hello_world() -> str:
    return 'hello world'


@app.route('/<name>')
def hello_name(name: str) -> str:
    return f'hello {name}'

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)
