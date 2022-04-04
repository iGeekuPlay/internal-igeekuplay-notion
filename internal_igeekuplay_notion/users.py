from flask import Blueprint, jsonify
from utilities.notion import Notion
import os


notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/')
def index():
    result = n.list_users()['results']
    return jsonify(result)