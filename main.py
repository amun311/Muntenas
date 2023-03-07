from flask import Flask
from flask import render_template 
app = Flask(__name__)

FAMILY = [
  {
    'id': 1,
    'title': 'Padre',
    'nombre': 'Alexandru Gheorghe',
    'edad': '39'
  },
  {
    'id': 2,
    'title': 'Madre',
    'nombre': 'Florentina Rodica',
    'edad': '40'
  },
  {
   'id': 3,
    'title': 'Hijo',
    'nombre': 'Alexandru Theodor',
    'edad': '17'
  }
]

#@app.route('/')
#def index():
#    return 'Hello from Flask!'
@app.route('/')
def hello():
  return render_template('home.html')
app.run(host='0.0.0.0', port=81)
