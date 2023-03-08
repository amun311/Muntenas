from flask import Flask
from flask import render_template 
app = Flask(__name__)

FAMILY = [
  {
    'id': 1,
    'fam': 'Tata',
    'nombre': 'Alexandru Gheorghe',
    'edad': '39'
  },
  {
    'id': 2,
    'fam': 'Mama',
    'nombre': 'Florentina Rodica',
    'edad': '40'
  },
  {
   'id': 3,
    'fam': 'Fiu',
    'nombre': 'Alexandru Theodor',
    'edad': '17'
  }
]

#@app.route('/')
#def index():
#    return 'Hello from Flask!'
@app.route('/')
def hello():
  return render_template('home.html',family = FAMILY, family_name = 'Muntenas')

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
