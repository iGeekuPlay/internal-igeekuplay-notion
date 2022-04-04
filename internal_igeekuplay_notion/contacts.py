import json
from flask import Blueprint, jsonify, request
from internal_igeekuplay_notion.utilities.notion import Notion
import os

CONTACT_DB = os.getenv("CONTACT_DB")


notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
contact_blueprint = Blueprint('contacts', __name__)

@contact_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = json.dumps(request.json)
        result = n.create_page(payload=data)
        return result

    else:
        result = n.query_db(CONTACT_DB)['results']
    return jsonify(result)



@contact_blueprint.route('/<contact_email>', methods=['GET'])
def get_contact(contact_email):
    data = json.dumps({"filter": {"and": [{"property": "Email", "email": {"contains": contact_email}}]}})
    result = n.query_db(CONTACT_DB, payload=data)['results']
    return jsonify(result)


@contact_blueprint.route('/search', methods=['POST'])
def search_contact():
    data = json.dumps(request.json)
    print(f"DATA: {data}")
    result = n.query_db(CONTACT_DB, payload=data)['results']
    return jsonify(result)