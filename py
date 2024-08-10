# Importar
from flask import Flask, render_template


app = Flask(__name__)


# La primera página
@app.route('/')
def index():
    return render_template('index.html')

# La segunda página
@app.route('/masinformacion')
def masinformacion():
    return render_template(
                            'masinformacion.html', 
                           )


app.run(debug=True)
