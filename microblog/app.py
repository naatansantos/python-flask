from flask import flask
app = flask (__nome__)
@app.route('/')
def index():
    return 'olá mundo!'
if __name__ == '__main__':
    app.run()