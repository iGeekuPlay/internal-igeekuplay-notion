from flask import Blueprint, jsonify
from internal_igeekuplay_notion.utilities.notion import Notion
import os
from internal_igeekuplay_notion.utilities.auth import auth

notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/')
@auth.login_required
def index():
    result = n.list_users()['results']
    return jsonify(result)