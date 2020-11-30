from flask import Flask, request, send_from_directory, make_response
from flask_restful import Api
from flask_cors import CORS
from src.models.scheduller import Scheduler
from src.models.task import Task

CLIENT_APP_FOLDER = '../client'
APP_RUN_DEBUG_MODE = True
APP_USE_RELOADER = False
APP_PORT = 5000

app = Flask(__name__)

@app.route('/api/schedule', methods=['POST'])
def schedule():
    body = request.json
    print(body)
    tasks = [Task(t['name'], t['deadline'], t['computeTime']) for t in body['tasks']]
    scheduler = Scheduler(tasks, body['processors'], body['planner'])
    result = scheduler.schedule()
    return make_response(result.to_dict())

@app.route('/', methods=['GET'])
def root():
    return send_from_directory(CLIENT_APP_FOLDER, 'index.html')

@app.route('/<path:path>', methods=['GET'])
def static_file(path):
    return send_from_directory(CLIENT_APP_FOLDER, path)

def run_server():
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    api = Api(app)
    app.run(debug=APP_RUN_DEBUG_MODE,
            use_reloader=APP_USE_RELOADER,
            port=APP_PORT)
