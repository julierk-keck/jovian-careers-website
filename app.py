from flask import Flask, render_template

app = Flask (__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'extra': 'Honolulu, HI'
  },
  {
    'id': 2,
    'title': 'Fascinator',
    'extra': 'Hilo, HI'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Julie's")

print(__name__)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  