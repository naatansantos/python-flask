from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'olá mundo!'
if __name__ == '__main__':
    app.run()