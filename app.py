from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask (__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name="Julie's")

@app.route("/api")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/jobs/<id>")   #define a dynamic route by using <variable>
def job_page(id):
  job = load_job_from_db(id)
  #return jsonify(job)
  if not job:
    return render_template('notFound.html'), 404
  
  return render_template('jobApply.html', job=job, company_name="Julie's")

print(__name__)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  