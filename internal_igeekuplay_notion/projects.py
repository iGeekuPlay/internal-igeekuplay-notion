import json
from flask import Blueprint, jsonify, request
from internal_igeekuplay_notion.utilities.notion import Notion
import os
from internal_igeekuplay_notion.utilities.auth import auth


PROJECT_DB = os.getenv("PROJECT_DB")

notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
project_blueprint = Blueprint('projects', __name__)

@project_blueprint.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    if request.method == 'POST':
        data = json.dumps(request.json)
        result = n.create_page(payload=data)
        return result

    else:
        result = n.query_db(PROJECT_DB)['results']
    return jsonify(result)

@project_blueprint.route('/<event_name>', methods=['GET'])
@auth.login_required
def get_project(project_name):
    data = json.dumps({"filter": {"and": [{"property": "Name", "title": {"contains": project_name}}]}})
    result = n.query_db(PROJECT_DB, payload=data)['results']
    return jsonify(result)


@project_blueprint.route('/search', methods=['POST'])
@auth.login_required
def search_projects():
    data = json.dumps(request.json)
    print(f"DATA: {data}")
    result = n.query_db(PROJECT_DB, payload=data)['results']
    return jsonify(result)