from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/contato')
def contato():
    return render_template('contato.html', tel='(75)99814-2794', nome='tanzin')

@app.route('/p1')
def p1():
    return render_template('p1.html')
@app.route('/p2')
def p2():
    return render_template('p2.html', nc='natanael santos barbosa', id='22')
# calculadora para somar dois números passados por parâmetros
@app.route("/soma/<int:num1>/<int:num2>")
def soma (num1,num2):
    return f'total {num1 + num2}'
# Minha página pessoal
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route('/dados')
def dados():
    return render_template('dados.html')

if __name__ == '__main__':
    app.run()