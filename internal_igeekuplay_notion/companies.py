import json
from flask import Blueprint, jsonify, request
from internal_igeekuplay_notion.utilities.notion import Notion
import os
from internal_igeekuplay_notion.utilities.auth import auth

COMPANY_DB = os.getenv("COMPANY_DB")


notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
company_blueprint = Blueprint('companies', __name__)

@company_blueprint.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    if request.method == 'POST':
        data = json.dumps(request.json)
        result = n.create_page(payload=data)
        return result

    else:
        result = n.query_db(COMPANY_DB)['results']
    return jsonify(result)



@company_blueprint.route('/<company_name>', methods=['GET'])
@auth.login_required
def get_company(company_name):
    data = json.dumps({"filter": {"and": [{"property": "Name", "title": {"contains": company_name}}]}})
    result = n.query_db(COMPANY_DB, payload=data)['results']
    return jsonify(result)


@company_blueprint.route('/search', methods=['POST'])
@auth.login_required
def search_companies():
    data = json.dumps(request.json)
    print(f"DATA: {data}")
    result = n.query_db(COMPANY_DB, payload=data)['results']
    return jsonify(result)