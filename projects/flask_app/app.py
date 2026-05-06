from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name')
def name():
    return 'Hello, apu'

@app.route('/contact')
def mail():
    return 'you can contact me at apu@example.com!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)