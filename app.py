from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/wykres')
def wykres():
    return render_template('wykres.html')

if __name__ == '__main__':
    app.run(debug=True)