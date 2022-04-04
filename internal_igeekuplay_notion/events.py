import json
from flask import Blueprint, jsonify, request
from utilities.notion import Notion
import os

EVENT_DB = os.getenv("EVENT_DB")

notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
event_blueprint = Blueprint('events', __name__)

@event_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = json.dumps(request.json)
        result = n.create_page(payload=data)
        return result

    else:
        result = n.query_db(EVENT_DB)['results']
    return jsonify(result)

@event_blueprint.route('/<event_name>', methods=['GET'])
def get_event(event_name):
    data = json.dumps({"filter": {"and": [{"property": "Name", "title": {"contains": event_name}}]}})
    result = n.query_db(EVENT_DB, payload=data)['results']
    return jsonify(result)


@event_blueprint.route('/search', methods=['POST'])
def search_events():
    data = json.dumps(request.json)
    print(f"DATA: {data}")
    result = n.query_db(EVENT_DB, payload=data)['results']
    return jsonify(result)