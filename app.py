from flask import Flask
import os
app = Flask(__name__)
hostname = os.environ['HOSTNAME']

@app.route('/')
def hello_world():
    return 'Hello QConSP 2017! I am container {}'.format(hostname)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
