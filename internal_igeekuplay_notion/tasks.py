import json
from flask import Blueprint, jsonify, request
from internal_igeekuplay_notion.utilities.notion import Notion
import os

TASK_DB = os.getenv("TASK_DB")

notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = json.dumps(request.json)
        result = n.create_page(payload=data)
        return result

    else:
        result = n.query_db(TASK_DB)['results']
    return jsonify(result)

@task_blueprint.route('/<event_name>', methods=['GET'])
def get_event(task_name):
    data = json.dumps({"filter": {"and": [{"property": "Name", "title": {"contains": task_name}}]}})
    result = n.query_db(TASK_DB, payload=data)['results']
    return jsonify(result)


@task_blueprint.route('/search', methods=['POST'])
def search_tasks():
    data = json.dumps(request.json)
    print(f"DATA: {data}")
    result = n.query_db(TASK_DB, payload=data)['results']
    return jsonify(result)