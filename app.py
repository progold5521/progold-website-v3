from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'kedah, malaysia',
    'salary': 'RM 5000.000',
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'perak, malaysia',
    'salary': 'RM 10000.000',
  },
  {
    'id': 3,
    'title': 'gila punya orang',
    'location': 'kelantan, malaysia',
    'salary': 'RM 15000.000',
  },
  {
    'id': 4,
    'title': 'kaki tipu',
    'location': 'pulau pinang, malaysia',
    'salary': 'RM 20000.000',
  },
]
    

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                         compony_name='progold')
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
