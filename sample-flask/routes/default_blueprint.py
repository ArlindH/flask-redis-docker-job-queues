from flask import Blueprint
from jobs.sample_jobs import sample_job1, sample_job2
default_blueprint = Blueprint('default_blueprint', __name__)

@default_blueprint.route('/')
def index():
    return "Hello, World!"

@default_blueprint.route('/job1')
def start_job1():
    sample_job1.queue()
    return "Job 1 queued"

@default_blueprint.route('/job2')
def start_job2():
    sample_job2.queue()
    return "Job 2 queued" 
