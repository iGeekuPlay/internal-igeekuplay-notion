from flask import Blueprint, jsonify, request
from internal_igeekuplay_notion.utilities.notion import Notion
import os
from internal_igeekuplay_notion.utilities.auth import auth
import json

notion_token = os.getenv("NOTION_TOKEN")
n = Notion(notion_token)
crm_blueprint = Blueprint('crm', __name__)


@crm_blueprint.route('/discovery', methods=['GET', 'POST'])
@auth.login_required
def discovery_call():
    if request.method == 'POST':
        data = request.json
        # Add Contact to CRM
        contact_data = json.dumps({"object":"page","parent":{"database_id":"44121e1f-f9bd-4581-a0f2-e7227b31b45d","type":"database_id"},"properties":{"Email":{"email":data["contact_email"],"id":"NqQc","type":"email"},"Image":{"files":[],"id":"%3BEkh","type":"files"},"Name":{"id":"title","title":[{"annotations":{"bold":False,"code":False,"color":"default","italic":False,"strikethrough":False,"underline":False},"href":None,"plain_text":data["contact_name"],"text":{"content":data["contact_name"],"link":None},"type":"text"}],"type":"title"},"Phone":{"id":"%7DrN%7D","phone_number":None,"type":"phone_number"},"Title":{"id":"trAd","rich_text":[{"annotations":{"bold":False,"code":False,"color":"default","italic":False,"strikethrough":False,"underline":False},"href":None,"plain_text":data["contact_title"],"text":{"content":data["contact_title"],"link":None},"type":"text"}],"type":"rich_text"}}})
        contact_result = n.create_page(payload=contact_data)
        contact = n.munch(contact_result)
        # # Add Company to CRM
        company_data = json.dumps({"object":"page","parent":{"database_id":"9d0c10ee-aff3-49b4-8c20-862a24ec1dc4","type":"database_id"},"properties":{"Contacts":{"id":"MG%3FO","relation":[{"id":contact.id}],"type":"relation"},"Name":{"id":"title","title":[{"annotations":{"bold":False,"code":False,"color":"default","italic":False,"strikethrough":False,"underline":False},"href":None,"plain_text":data['company_name'],"text":{"content":data['company_name']},"type":"text"}],"type":"title"},"Source":{"id":"h%3B%60K","select":{"color":"orange","id":"8fd88cec-a648-450e-a524-f1d6b0a8553b","name":"Discovery"},"type":"select"},"Status":{"id":"bOci","select":{"color":"yellow","id":"73425feb-12cd-406f-8aac-e72aaf5074cf","name":"Discovery"},"type":"select"},"Website":{"id":"QrqD","type":"url","url":data['company_url']}}})
        company_result = n.create_page(payload=company_data)
        company = n.munch(company_result)
        # # Add Event to Calendar
        event_data = json.dumps({"object":"page","parent":{"database_id":"a88a3d4c-c2c6-430e-85ed-1a6206a0d468","type":"database_id"},"properties":{"Attendees":{"id":"dkk%3E","relation":[{"id":contact.id}],"type":"relation"},"Date":{"date":{"end":None,"start":data['start_date'],"time_zone":None},"id":"yww%40","type":"date"},"Name":{"id":"title","title":[{"annotations":{"bold":False,"code":False,"color":"default","italic":False,"strikethrough":False,"underline":False},"href":None,"plain_text":f"Discovery Call with {data['contact_name']} from {data['company_name']}","text":{"content":f"Discovery Call with {data['contact_name']} from {data['company_name']}","link":None},"type":"text"}],"type":"title"},"Type":{"id":"vGg%3D","select":{"color":"orange","id":"8ba6d823-82e6-457a-8da0-494673c4957c","name":"Discovery Call"},"type":"select"}}})
        event_result = n.create_page(payload=event_data)
        event = n.munch(event_result)
        # Add Prep Task to User Stories
        task_data = json.dumps({"object":"page","parent":{"database_id":"c26edf2b-1c4b-4315-b625-5d5393a06905","type":"database_id"},"icon":{"external": {"url": "https://raw.githubusercontent.com/eirikmadland/notion-icons/master/v5/icon3/mi-notes.svg"},"type": "external"}, "properties":{"Due Date":{"date":{"end": None,"start": data['start_date'],"time_zone": None},"id":"twDa","type":"date"},"Name":{"id":"title","title":[{"annotations":{"bold":False,"code":False,"color":"default","italic":False,"strikethrough":False,"underline":False},"href":None,"plain_text":f"Prep for Discovery with {data['contact_name']}","text":{"content":f"Prep for Discovery with {data['contact_name']}","link":None},"type":"text"}],"type":"title"},"Priority":{"id":"OMHA","select":None,"type":"select"},"Status":{"id":"~L%3A~","select":{"color":"orange","id":"8ead110a-43f8-4699-8356-1694e0a3045a","name":"Selected"},"type":"select"},"Story Points":{"id":"gUhB","number":1,"type":"number"},"Type":{"id":"clVc","select":{"color":"default","id":"3aa7ee4f-8612-4603-b19f-cf4f34023be0","name":"🗒 User Story"},"type":"select"}}})
        task_result = n.create_page(payload=task_data)
        task = n.munch(task_result)
        result = {"contact_result": contact_result, "company_result": company_result, "event_result": event_result, "task_result":task_result}
    else:
        result = {}
    return jsonify(result)

@crm_blueprint.route('/discovery/won', methods=['GET', 'POST'])
@auth.login_required
def discovery_call_won():
    if request.method == 'POST':
        data = json.dumps(request.json)
        # Add Epic to Calendar
        result = n.create_page(payload=data)
        return result

    else:
        result = {}
    return jsonify(result)
