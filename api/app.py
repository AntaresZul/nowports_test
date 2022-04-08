import celery.states as states
from flask import Flask, Response
from flask import url_for, jsonify
from worker import celery

dev_mode = True
app = Flask(__name__)


@app.route('/count')
def count() -> str:
    task = celery.send_task('tasks.count', args=[], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response


@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return res.result


@app.route('/')
def health_check() -> Response:
    return jsonify("Service running ...")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
