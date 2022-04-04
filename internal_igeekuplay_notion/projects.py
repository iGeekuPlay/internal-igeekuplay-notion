import json
from flask import Blueprint, jsonify, request
from utilities.notion import Notion
import os

PROJECT_DB = os.getenv("PROJECT_DB")

notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
project_blueprint = Blueprint('projects', __name__)

@project_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = json.dumps(request.json)
        result = n.create_page(payload=data)
        return result

    else:
        result = n.query_db(PROJECT_DB)['results']
    return jsonify(result)

@project_blueprint.route('/<event_name>', methods=['GET'])
def get_project(project_name):
    data = json.dumps({"filter": {"and": [{"property": "Name", "title": {"contains": project_name}}]}})
    result = n.query_db(PROJECT_DB, payload=data)['results']
    return jsonify(result)


@project_blueprint.route('/search', methods=['POST'])
def search_projects():
    data = json.dumps(request.json)
    print(f"DATA: {data}")
    result = n.query_db(PROJECT_DB, payload=data)['results']
    return jsonify(result)