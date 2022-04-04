import json
from flask import Blueprint, jsonify, request
from internal_igeekuplay_notion.utilities.notion import Notion
import os


INVOICE_DB = os.getenv("INVOICE_DB")

notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
invoice_blueprint = Blueprint('invoices', __name__)

@invoice_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = json.dumps(request.json)
        result = n.create_page(payload=data)
        return result

    else:
        result = n.query_db(INVOICE_DB)['results']
    return jsonify(result)

@invoice_blueprint.route('/<invoice_name>', methods=['GET'])
def get_invoice(project_name):
    data = json.dumps({"filter": {"and": [{"property": "Name", "title": {"contains": invoice_name}}]}})
    result = n.query_db(INVOICE_DB, payload=data)['results']
    return jsonify(result)


@invoice_blueprint.route('/search', methods=['POST'])
def search_inovices():
    data = json.dumps(request.json)
    print(f"DATA: {data}")
    result = n.query_db(INVOICE_DB, payload=data)['results']
    return jsonify(result)